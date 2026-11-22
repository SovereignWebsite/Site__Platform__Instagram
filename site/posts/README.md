# Posts

One folder per post: `site/posts/<yyyy-mm-dd>__<slug>/`, holding the media (JPEG, or MP4 for a Reel) and `post.json`. The folder is served by this site's Pages, which is where Instagram fetches the media from.

```json
{
  "kind": "reel",
  "media": ["video.mp4"],
  "caption": "The caption, at most 2200 characters.",
  "source": "where the media came from and its licence",
  "approved": { "by": "Dinis Cruz", "at": "2026-11-22T22:30Z", "where": "session URL" }
}
```

Nothing is posted without `approved`, the owner's yes for that post. The Instagram post workflow runs only by hand, with the post id; its default is a dry run that checks the post and sends nothing.
