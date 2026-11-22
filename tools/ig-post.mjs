// Publish one approved post to Instagram through the official API
// (Instagram API with Instagram Login). Run only by .github/workflows/instagram-post.yml.
// Usage: node tools/ig-post.mjs <post-id> [--dry-run]
// Reads site/posts/<post-id>/post.json. The media must already be served by this site's Pages.
// Secrets come from the environment (IG_TOKEN, IG_USER_ID) and are never printed.
import { readFileSync, existsSync } from 'node:fs';

const API = 'https://graph.instagram.com/v21.0';
const SITE = 'https://instagram.platform.sovereignweb.site';
const [id, flag] = process.argv.slice(2);
const dry = flag === '--dry-run';
if (!/^[0-9]{4}-[0-9]{2}-[0-9]{2}__[a-z0-9-]{1,40}$/.test(id || '')) fail('post id must be <yyyy-mm-dd>__<slug>');

const file = `site/posts/${id}/post.json`;
if (!existsSync(file)) fail(`no ${file}`);
const post = JSON.parse(readFileSync(file, 'utf8'));

// The owner's yes is recorded in the post itself: who, when and where.
if (!post.approved || !post.approved.by || !post.approved.at || !post.approved.where) fail('post has no approval line (approved.by, .at, .where)');
if (post.published) fail(`already published: ${post.published.media_id}`);
const kind = post.kind;
if (!['image', 'reel', 'carousel'].includes(kind)) fail('kind must be image, reel or carousel');
const caption = String(post.caption || '');
if (caption.length > 2200) fail('caption over 2200 characters');
if (/[\u2013\u2014]/.test(caption)) fail('caption has an en or em dash');
const media = (post.media || []).map(m => `${SITE}/posts/${id}/${m}`);
if (!media.length) fail('no media');
if (kind === 'carousel' && (media.length < 2 || media.length > 10)) fail('a carousel has 2 to 10 items');

console.log(`post ${id}: ${kind}, ${media.length} item(s), caption ${caption.length} chars`);
for (const u of media) {
  const r = await fetch(u, { method: 'HEAD' });
  if (!r.ok) fail(`media not public yet: ${u} (${r.status})`);
}
if (dry) { console.log('dry run: checks passed, nothing sent'); process.exit(0); }

const token = process.env.IG_TOKEN, user = process.env.IG_USER_ID;
if (!token || !user) fail('IG_TOKEN and IG_USER_ID secrets are not set');

async function call(path, params) {
  const r = await fetch(`${API}/${path}`, {
    method: params ? 'POST' : 'GET',
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: params ? JSON.stringify(params) : undefined,
  });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || j.error) fail(`API ${path.split('?')[0]}: ${r.status} ${j.error ? j.error.message : ''}`);
  return j;
}
async function ready(container) {
  for (let i = 0; i < 60; i++) {
    const s = await call(`${container}?fields=status_code`);
    if (s.status_code === 'FINISHED') return;
    if (s.status_code === 'ERROR' || s.status_code === 'EXPIRED') fail(`container ${s.status_code}`);
    await new Promise(r => setTimeout(r, 5000));
  }
  fail('container not ready after 5 minutes');
}
const item = (u, extra = {}) => /\.mp4$/i.test(u) ? { media_type: kind === 'reel' ? 'REELS' : 'VIDEO', video_url: u, ...extra } : { image_url: u, ...extra };

let creation;
if (kind === 'carousel') {
  const children = [];
  for (const u of media) { const c = await call(`${user}/media`, item(u, { is_carousel_item: true })); await ready(c.id); children.push(c.id); }
  creation = (await call(`${user}/media`, { media_type: 'CAROUSEL', children: children.join(','), caption })).id;
} else {
  creation = (await call(`${user}/media`, { ...item(media[0]), caption })).id;
}
await ready(creation);
const done = await call(`${user}/media_publish`, { creation_id: creation });
console.log(`published: media id ${done.id}`);

function fail(m) { console.error(`ig-post: ${m}`); process.exit(1); }
