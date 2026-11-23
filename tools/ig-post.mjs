// Publish one approved post to Instagram through Buffer's API (developers.buffer.com).
// Buffer is a Meta partner and publishes through Instagram's official API.
// Run only by .github/workflows/instagram-post.yml.
// Usage: node tools/ig-post.mjs <post-id> [--dry-run]
// Reads site/posts/<post-id>/post.json. The media must already be served by this site's Pages.
// The secret BUFFER_API_KEY comes from the environment and is never printed.
import { readFileSync, existsSync } from 'node:fs';

const API = 'https://api.buffer.com';
const SITE = 'https://instagram.platform.sovereignweb.site';
const [id, flag] = process.argv.slice(2);
const dry = flag === '--dry-run';
if (!/^[0-9]{4}-[0-9]{2}-[0-9]{2}__[a-z0-9-]{1,40}$/.test(id || '')) fail('post id must be <yyyy-mm-dd>__<slug>');

const file = `site/posts/${id}/post.json`;
if (!existsSync(file)) fail(`no ${file}`);
const post = JSON.parse(readFileSync(file, 'utf8'));

// The owner's yes is recorded in the post itself: who, when and where.
// Either the owner's yes for this post, or the standing review rule (site/policy/abp.json posting_rules):
// three clear reviews, by the keeper, a security agent and a counsel agent, each in its own file.
let a = post.approved;
if (!a || !a.by || !a.at || !a.where) {
  const roles = { keeper: /^instagram\./, security: /^security\./, counsel: /^counsel\./ };
  const why = [];
  for (const [role, re] of Object.entries(roles)) {
    const f = `site/posts/${id}/review-${role}.json`;
    if (!existsSync(f)) { why.push(`no review-${role}.json`); continue; }
    const r = JSON.parse(readFileSync(f, 'utf8'));
    if (!re.test(r.agent || '')) why.push(`review-${role}.json is not by a ${role} agent`);
    else if (r.verdict !== 'clear' || r.private_data !== false || !Array.isArray(r.red_flags) || r.red_flags.length) why.push(`review-${role}.json is not clear`);
    else if (!r.at) why.push(`review-${role}.json has no time`);
  }
  if (why.length) fail(`no approval line, and the standing review rule is not met: ${why.join('; ')}`);
  a = { by: 'standing review rule (keeper, security, counsel)', at: new Date().toISOString().slice(0, 16) + 'Z' };
}
const wanted = Array.isArray(post.channels) && post.channels.length ? post.channels : ['instagram'];
for (const c of wanted) if (!['instagram', 'youtube', 'linkedin'].includes(c)) fail(`unknown channel ${c}`);
// Older records hold one Instagram send; newer ones hold one record per channel.
const sent = post.published ? (post.published.channels || { instagram: post.published }) : {};
const todo = wanted.filter((c) => !sent[c]);
if (!todo.length) fail(`already sent to ${wanted.join(', ')}: ${JSON.stringify(post.published)}`);
if (todo.includes('youtube') && post.kind !== 'reel') fail('YouTube takes a reel (one MP4) only');
const kind = post.kind;
if (!['image', 'reel', 'carousel'].includes(kind)) fail('kind must be image, reel or carousel');
const caption = String(post.caption || '');
if (caption.length > 2200) fail('caption over 2200 characters');
if (/[–—]/.test(caption)) fail('caption has an en or em dash');
const media = post.media || [];
if (!media.length) fail('no media');
if (kind === 'carousel' && (media.length < 2 || media.length > 10)) fail('a carousel has 2 to 10 items');
if (kind === 'reel' && (media.length !== 1 || !/\.mp4$/i.test(media[0]))) fail('a reel is one MP4');
for (const m of media) {
  if (!/^[a-z0-9._-]+\.(jpe?g|mp4)$/i.test(m)) fail(`media must be JPEG or MP4 in the post folder: ${m}`);
  const s = readFileSync(`site/posts/${id}/${m}`);
  if (/\.jpe?g$/i.test(m)) {
    if (s.length > 8 * 1024 * 1024) fail(`${m} over 8 MB`);
    const d = jpegSize(s);
    if (!d) fail(`${m} is not a readable JPEG`);
    const r = d.w / d.h;
    if (d.w < 320 || d.w > 1440) fail(`${m} is ${d.w} px wide; Instagram takes 320 to 1440`);
    if (r < 0.8 - 1e-3 || r > 1.91 + 1e-3) fail(`${m} ratio ${r.toFixed(2)}; Instagram takes 4:5 to 1.91:1`);
  }
}
if (post.thumbnail_offset_ms !== undefined && !(Number.isInteger(post.thumbnail_offset_ms) && post.thumbnail_offset_ms >= 0)) fail('thumbnail_offset_ms must be a whole number of milliseconds');
// The schedule: shareNow unless the post names a time (UTC, ISO 8601).
const mode = post.due_at ? 'customScheduled' : 'shareNow';
if (post.due_at && !(Date.parse(post.due_at) > Date.now()) && !(post.published && todo.every((c) => c === 'youtube' && post.youtube_due_at))) fail('due_at must be a future UTC time');
if (post.youtube_due_at && todo.includes('youtube') && !(Date.parse(post.youtube_due_at) > Date.now())) fail('youtube_due_at must be a future UTC time');

const urls = media.map(m => `${SITE}/posts/${id}/${m}`);
console.log(`post ${id}: ${kind}, ${urls.length} item(s), caption ${caption.length} chars, ${mode}${post.due_at ? ' ' + post.due_at : ''}`);
console.log(`approved by ${a.by} at ${a.at}`);
for (const u of urls) {
  const r = await fetch(u, { method: 'HEAD' });
  if (!r.ok) fail(`media not public yet: ${u} (${r.status})`);
}

const key = process.env.BUFFER_API_KEY;
if (!key) { if (dry) { console.log('dry run: checks passed; BUFFER_API_KEY not set, Buffer not contacted'); process.exit(0); } fail('BUFFER_API_KEY secret is not set'); }

async function gql(query, variables = {}) {
  const r = await fetch(API, {
    method: 'POST',
    headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, variables }),
  });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || j.errors) fail(`Buffer API ${r.status}: ${(j.errors || []).map(e => e.message).join('; ') || 'no body'}`);
  return j.data;
}

// Find the one Instagram channel in the key's organisations.
const orgs = (await gql('query { account { organizations { id } } }')).account.organizations;
const all = [];
for (const o of orgs) {
  const d = await gql('query C($o: OrganizationId!) { channels(input: { organizationId: $o }) { id service isQueuePaused } }', { o: o.id });
  all.push(...d.channels);
}
const channelOf = {};
for (const c of todo) {
  const found = all.filter((x) => x.service === c);
  if (found.length !== 1) fail(`expected one ${c} channel in Buffer, found ${found.length}`);
  if (found[0].isQueuePaused) fail(`the ${c} queue is paused in Buffer`);
  channelOf[c] = found[0];
  console.log(`Buffer: one ${c} channel found`);
}
if (dry) { console.log('dry run: checks passed, nothing sent'); process.exit(0); }

const assets = urls.map((u, i) => /\.mp4$/i.test(u)
  ? { video: { url: u, metadata: { thumbnailOffset: Number.isInteger(post.thumbnail_offset_ms) ? post.thumbnail_offset_ms : 600 } } }
  : { image: { url: u, metadata: { altText: (post.alt && post.alt[i]) || caption.slice(0, 120) } } });
const yt = post.youtube || {};
const ytTitle = String(yt.title || caption.split('\n')[0]).slice(0, 100);
const meta = {
  instagram: { instagram: { type: kind === 'reel' ? 'reel' : 'post', shouldShareToFeed: true } }, // a carousel is a 'post' with several images (Buffer: types are post, story, reel)
  youtube: { youtube: { title: ytTitle, categoryId: String(yt.categoryId || '28'), privacy: yt.privacy || 'public', madeForKids: false, isAiGenerated: yt.isAiGenerated !== false, notifySubscribers: yt.notifySubscribers !== false } },
};
// LinkedIn: the caption plus a footer naming and linking the people and page to tag (tools/linkedin-mentions.json);
// a real tag (annotation) only for entries whose URN is known.
const li = JSON.parse(readFileSync('tools/linkedin-mentions.json', 'utf8'));
const liText = `${caption}\n\n${li.footer}`;
const liAnnotations = li.mentions.filter((m) => m.urn).map((m) => {
  const start = liText.indexOf(m.name);
  return start < 0 ? null : { id: m.urn.split(':').pop(), entity: m.urn, start, length: m.name.length, link: m.link, localizedName: m.name, vanityName: m.vanity };
}).filter(Boolean);
meta.linkedin = { linkedin: liAnnotations.length ? { annotations: liAnnotations } : {} };
const results = {};
for (const c of todo) {
  const input = { text: c === 'linkedin' ? liText : caption, channelId: channelOf[c].id, schedulingType: 'automatic', mode, assets, metadata: meta[c] };
  // A channel may have its own time (YouTube allows 2 scheduled posts a day on this channel).
  const due = (c === 'youtube' && post.youtube_due_at) || post.due_at;
  input.mode = due ? 'customScheduled' : 'shareNow';
  if (due) input.dueAt = due;
  const res = (await gql(`mutation P($input: CreatePostInput!) { createPost(input: $input) {
    ... on PostActionSuccess { post { id dueAt } }
    ... on MutationError { message } } }`, { input })).createPost;
  if (!res.post) fail(`Buffer refused the ${c} post: ${res.message}`);
  results[c] = res.post;
  console.log(`sent to Buffer for ${c}: post ${res.post.id}, due ${res.post.dueAt || 'now'}`);
}

function jpegSize(b) {
  if (b[0] !== 0xff || b[1] !== 0xd8) return null;
  let i = 2;
  while (i < b.length) {
    if (b[i] !== 0xff) return null;
    const m = b[i + 1], len = b.readUInt16BE(i + 2);
    if (m >= 0xc0 && m <= 0xcf && ![0xc4, 0xc8, 0xcc].includes(m)) return { h: b.readUInt16BE(i + 5), w: b.readUInt16BE(i + 7) };
    i += 2 + len;
  }
  return null;
}
function fail(m) { console.error(`ig-post: ${m}`); process.exit(1); }
