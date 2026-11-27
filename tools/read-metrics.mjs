// Reads, for every post this site sent through Buffer, Buffer's own record: status, public link and metrics
// (counts only: impressions, reactions, comments, shares and the like). No names, no comment text.
// Run by .github/workflows/read-metrics.yml; prints JSON between markers. The key comes from the environment and is never printed.
import { readdirSync, readFileSync, existsSync } from 'node:fs';
const key = process.env.BUFFER_API_KEY;
if (!key) { console.error('BUFFER_API_KEY not set'); process.exit(1); }
async function gql(query, variables) {
  const r = await fetch('https://api.buffer.com', { method: 'POST', headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' }, body: JSON.stringify({ query, variables }) });
  const j = await r.json().catch(() => ({}));
  return { ok: r.ok && !j.errors, data: j.data, error: (j.errors || []).map((e) => e.message).join('; ') || (r.ok ? '' : `HTTP ${r.status}`) };
}
const out = { read_at: new Date().toISOString().slice(0, 16) + 'Z', posts: [] };
for (const id of readdirSync('site/posts').sort()) {
  const f = `site/posts/${id}/post.json`;
  if (!existsSync(f)) continue;
  const p = JSON.parse(readFileSync(f, 'utf8'));
  const pub = p.published;
  const chans = { ...(pub ? (pub.channels || { instagram: pub }) : {}) };
  for (const [ch, rec] of Object.entries((p.drafts && p.drafts.channels) || {})) chans[`${ch} (draft)`] = rec;
  for (const [channel, rec] of Object.entries(chans)) {
    if (!rec.buffer_post_id) continue;
    const draft = channel.endsWith('(draft)');
    const q = draft
      ? 'query P($id: PostId!) { post(input: { id: $id }) { id status dueAt channelService text assets { type thumbnail ... on VideoAsset { video { durationMs width height thumbnailOffset } } } metadata { ... on YoutubePostMetadata { title type isAiGenerated privacy } ... on InstagramPostMetadata { type isAiGenerated shouldShareToFeed } } } }'
      : 'query P($id: PostId!) { post(input: { id: $id }) { id status sentAt externalLink metricsUpdatedAt metrics { type name value unit } } }';
    const r = await gql(q, { id: rec.buffer_post_id });
    if (draft) { out.posts.push({ id, channel, buffer: r.ok ? r.data.post : null, error: r.ok ? null : r.error }); continue; }
    const post = r.ok && r.data && r.data.post;
    out.posts.push({ id, channel, buffer_post_id: rec.buffer_post_id, status: post ? post.status : null, sent_at: post ? post.sentAt : null, link: post ? post.externalLink : null, metrics_updated: post ? post.metricsUpdatedAt : null, metrics: post && post.metrics ? Object.fromEntries(post.metrics.map((m) => [m.type, m.value])) : null, error: r.ok ? null : r.error });
  }
}
console.log('=== METRICS JSON ===');
console.log(JSON.stringify(out));
console.log('=== END ===');
