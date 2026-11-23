# Notes: two animated Reels with synthetic presenters (round 2)

Made by studio.c@SovereignWebsite.dinis (https://claude.ai/code/session_01Kw9UwC3pdjxjDeK5WaZYUD), 23 November 2026, after Dinis's review of round 1 in that session: use the team's characters and animation, speak as one character, a different character each time, and make it much more visual; the content and descriptions stay. Not approved: post.json has no approved line, which only Dinis gives, post by post, recorded by instagram.c.

| Reel | Presenter | Voice | Length |
|---|---|---|---|
| 2026-11-22__welcome-reel | The Guide (`guide`) | gpt-audio `cedar` | 64.3 s, 1,929 frames (ends with three "a moment in time" pages of the Reel's own facts, at Dinis's request) |
| 2026-11-22__team-intro | Conductor (`conductor`) | gpt-audio `ash` | 75.1 s, 2,255 frames |

Both carry a SovereignWebsite.ai wordmark at the top (Dinis's request); the welcome Reel's end card and both captions point to hub.sovereignweb.site for examples.

## Licence and credit of every part
- Presenters: the PrompTugal.news presenters library v0.1.0 (PrompTugal/PrompTugal__News__Bulletins, src/lib/presenters/v0.1.0), made by bulletins.b@PrompTugal.dinis. Code Apache-2.0; text and data CC BY 4.0; three.js 0.160.1 MIT. The Guide is a new model in the hatched style of storyboards.sgit.ai and Conductor a new model in the flat robot style of the-ultimate-insider.book.sgit.ai, as the library credits them. Each is a character made by code, not a real person; the library's fixed corner label ("synthetic presenter, made by code, no real person") is in every frame, and the top-right chip names the character as synthetic.
- The library's own note: until its pins pass security@'s review, a version is a preview for the lab, not for a published web page. These Reels do not serve the library on any page: it ran only inside a local headless browser to draw frames, which became the MP4. Reuse was also asked of its keepers (bulletins.d, bulletins.b) and studio.d through conductor.c and conductor.d; their answer is recorded on conductor.c's board.
- Scenes, drawings, captions and timing: own work by studio.c, text CC BY 4.0. Font Inter (SIL OFL 1.1).
- Voice: AI-generated, OpenAI gpt-audio stock voices through OpenRouter; OpenAI's terms assign the output to the user. Disclosed on screen and in each caption. No real person's voice.
- Lip sync: mouth shapes from the voice's loudness (own code); word timings for subtitles from faster-whisper (MIT) with Whisper base.en (MIT), run locally. Subtitles show the script's own words.
- Music: none.

## Voice notes
Each script was voiced in halves. The model twice read a preamble ("Understood, let's get started") and once dropped a last short sentence; those were cut out or re-voiced, and every used take was checked word for word against the script with a local Whisper transcript. The AI voice may say "Dinis" as "Dennis"; the subtitles and caption spell it correctly.

## OpenRouter calls and cost (both rounds)
| UTC | Model | Voice | Round | Output | Seconds | Cost (USD) |
|---|---|---|---|---|---|---|
| 2026-11-22T23:03:01Z | openai/gpt-audio-mini | alloy | 1 (first drafts) | test-mini-alloy.wav | 5.0 | 0.0003 |
| 2026-11-22T23:03:30Z | anthropic/claude-sonnet-5.5 | - | 1 (first drafts) | voice-directions.txt | - | 0.0127 |
| 2026-11-22T23:03:42Z | openai/gpt-audio | marin | 1 (first drafts) | voice-marin.wav | 37.15 | 0.0492 |
| 2026-11-22T23:03:52Z | openai/gpt-audio | marin | 1 (first drafts) | voice-marin.wav | 47.05 | 0.0624 |
| 2026-11-22T23:19:01Z | openai/gpt-audio | marin | 1 (first drafts) | voice-marin-2.wav | 49.9 | 0.0660 |
| 2026-11-22T23:19:40Z | openai/gpt-audio | marin | 1 (first drafts) | p1.wav | 36.5 | 0.0483 |
| 2026-11-22T23:19:43Z | openai/gpt-audio | marin | 1 (first drafts) | p2.wav | 15.1 | 0.0203 |
| 2026-11-23T00:57:48Z | anthropic/claude-sonnet-5.5 | - | 2 (characters) | voice-directions.txt | - | 0.0040 |
| 2026-11-23T00:58:01Z | openai/gpt-audio | cedar | 2 (characters) | p1.wav | 29.9 | 0.0394 |
| 2026-11-23T00:58:07Z | openai/gpt-audio | cedar | 2 (characters) | p2.wav | 30.05 | 0.0396 |
| 2026-11-23T00:58:15Z | openai/gpt-audio | ash | 2 (characters) | p1.wav | 40.35 | 0.0530 |
| 2026-11-23T00:58:21Z | openai/gpt-audio | ash | 2 (characters) | p2.wav | 32.9 | 0.0432 |
| 2026-11-23T00:59:08Z | openai/gpt-audio | ash | 2 (characters) | end.wav | 10.6 | 0.0142 |
| | | | | | **all** | **0.4527** |
