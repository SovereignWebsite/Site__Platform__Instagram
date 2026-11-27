// Builds site/data/reels.json: one entry per Reel post folder, newest first, for other sites
// (the YouTube platform site reads it in the browser). No handles or channel IDs.
// Usage: node tools/build-reels-feed.mjs
import { readdirSync, readFileSync, existsSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
const SITE = 'https://instagram.platform.sovereignweb.site';
const pages = { '2026-11-22__welcome-reel': 'welcome', '2026-11-22__team-intro': 'team' };
const out = [];
for (const id of readdirSync('site/posts').sort().reverse()) {
  const f = `site/posts/${id}/post.json`;
  if (!existsSync(f)) continue;
  const p = JSON.parse(readFileSync(f, 'utf8'));
  if (p.kind !== 'reel') continue;
  const video = existsSync(`site/posts/${id}/video-v2.mp4`) ? 'video-v2.mp4' : p.media[0];
  let duration = null;
  try { duration = Math.round(Number(execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', `site/posts/${id}/${video}`], { encoding: 'utf8' }))); } catch {}
  const slug = pages[id] || id.split('__')[1];
  const pub = p.published || null;
  const ch = pub ? (pub.channels || { instagram: pub }) : {};
  const state = pub ? (!ch.youtube && (p.channels || []).includes('youtube') ? 'sent to Instagram; YouTube scheduled' + (p.youtube_due_at ? ' for ' + p.youtube_due_at : '') : 'sent') : (p.previous_sends || []).length ? 'deleted, to be reposted' : 'waiting';
  out.push({
    id, title: p.caption ? p.caption.split('\n')[0] : ((p.youtube && p.youtube.title) || String(p.captions.instagram).split('. ')[0]),
    caption: String(p.caption || p.captions.instagram).split('\n\n').slice(0, 2).join(' ').slice(0, 280),
    page: existsSync(`site/reels/${slug}/index.html`) ? `${SITE}/reels/${slug}/` : null,
    poster: existsSync(`site/posts/${id}/cover.jpg`) ? `${SITE}/posts/${id}/cover.jpg` : null,
    video: `${SITE}/posts/${id}/${video}`,
    duration_s: duration,
    state,
    published_at: pub ? (() => { const x = pub.channels ? (pub.channels.instagram || pub.channels.youtube) : pub; return x.scheduled_for || x.sent_at || null; })() : null,
    channels: { instagram: (ch.instagram && ch.instagram.url) || null, youtube: (ch.youtube && ch.youtube.url) || null },
    sent_to: { instagram: !!ch.instagram, youtube: !!ch.youtube },
    credits: p.source || null,
    sources: existsSync(`site/posts/${id}/storyboard.json`) ? `${SITE}/posts/${id}/storyboard.json` : (existsSync(`site/posts/${id}/notes.md`) ? `${SITE}/posts/${id}/notes.md` : null),
  });
}
writeFileSync('site/data/reels.json', JSON.stringify({ about: 'Reels from the RiskMandate Instagram and YouTube account, newest first. Built from site/posts/*/post.json by tools/build-reels-feed.mjs.', updated: new Date().toISOString().slice(0, 16) + 'Z', reels: out }, null, 2) + '\n');
console.log(`${out.length} reels`);
