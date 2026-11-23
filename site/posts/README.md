# Posts

One folder per post: `site/posts/<yyyy-mm-dd>__<slug>/`, holding the media (JPEG, or MP4 for a Reel) and `post.json`. The folder is served by this site's Pages, which is where Instagram fetches the media from.

```json
{
  "kind": "reel",
  "due_at": "optional, a future UTC time; without it the post goes now",
  "thumbnail_offset_ms": "optional, for a Reel: the frame Instagram shows as the cover, in milliseconds (default 600, inside a cover held from the first frame)",
  "media": ["video.mp4"],
  "caption": "The caption, at most 2200 characters.",
  "source": "where the media came from and its licence",
  "audio": { "file": "track.mp3", "made_by": "the agent or person", "prompt": "the prompt used", "date": "2026-11-22", "plan": "the service plan it was made under, which sets the rights" },
  "approved": { "by": "Dinis Cruz", "at": "2026-11-22T22:30Z", "where": "session URL" }
}
```

Nothing is posted without `approved`, the owner's yes for that post. Posts go through Buffer's API (a Meta partner, publishing through Instagram's official API) with the owner's key, held only as the `BUFFER_API_KEY` secret of the `instagram` environment. The Instagram post workflow runs only by hand, with the post id; its default is a dry run that checks the post and sends nothing.

Audio: the Instagram API takes no separate audio track, so a track is mixed into the Reel's MP4 before posting; the track file and its `audio` record (prompt, date, plan) stay in the folder as the rights record.

Approval, either way (site/policy/abp.json, posting_rules):
- the owner's yes for the post, as `approved` in post.json; or
- for the studio's videos, three clear reviews in the folder: `review-keeper.json`, `review-security.json` and `review-counsel.json`, each `{ "agent": "<agent name>", "at": "<UTC time>", "verdict": "clear", "red_flags": [], "private_data": false, "notes": "..." }`, each committed signed by its own agent. Any red flag or private data stops the post until the owner says yes.
