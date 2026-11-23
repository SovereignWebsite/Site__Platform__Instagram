# Two voiced Reels for Instagram: welcome and team introduction

From studio.c@SovereignWebsite.dinis (https://claude.ai/code/session_01Kw9UwC3pdjxjDeK5WaZYUD), 22 November 2026, for instagram.c. Not posted, not approved: each post.json has no `approved` line, which only Dinis gives, post by post.

## The pieces
| Folder | Length | Size | Format |
|---|---|---|---|
| 2026-11-22__welcome-reel | 39.4 s | 2.8 MB | MP4, H.264 High 1080x1920 30 fps, AAC stereo 48 kHz, about -16 LUFS |
| 2026-11-22__team-intro | 53.9 s | 3.9 MB | same |

Each folder: video.mp4, cover.jpg (1080x1920 frame), post.json (caption, alt text, source and audio record, in the form of site/posts/README.md), script.txt, voice-direction.txt.

## Licence of every part
- Picture: own work, drawn frame by frame with Pillow and encoded with ffmpeg; text CC BY 4.0, like the rest of the site. Colours follow instagram.c's welcome image.
- Font: Inter (SIL Open Font License 1.1, as the system package records).
- Voice: AI-generated with OpenAI gpt-audio, stock synthetic voice "marin" (no real person's voice or likeness), through OpenRouter on Dinis's key. OpenAI's terms assign the output to the user; OpenRouter's terms pass that through. The video's footer and both captions say the voice is AI-generated.
- Music: none. Images or footage from anyone else: none.
- Caption timing only: word timings from faster-whisper (MIT) with the base.en Whisper model (MIT), run locally; nothing of it is in the media.

## Facts used
Only from sovereignwebsite.ai, .org, .site (read 22 Nov 2026, 23:0x UTC), the Instagram site and team/keys.json roles on Factory dev. No price, customer or private person. Dinis Cruz is named in the team piece as the person who decides what the agents work on, as the public sites name him; please confirm he is happy with that line.

## Voice notes
- The team script was voiced in two halves and joined with a 0.25 s pause: two whole takes stopped speaking before the last line although the model's text transcript said it was read. Each used take was checked word for word against the script with the model's transcript and a local Whisper transcription.
- Voice direction written by anthropic/claude-sonnet-5.5 from a short brief (voice-direction.txt).

## OpenRouter calls and cost
| UTC | Model | Voice | Output | Seconds | Cost (USD) | Use |
|---|---|---|---|---|---|---|
| 2026-11-22T23:03:01Z | openai/gpt-audio-mini | alloy | test-mini-alloy.wav | 5.0 | 0.0003 | test take (not used) |
| 2026-11-22T23:03:30Z | anthropic/claude-sonnet-5.5 | - | voice-directions.txt | - | 0.0127 | voice directions (used) |
| 2026-11-22T23:03:42Z | openai/gpt-audio | marin | voice-marin.wav | 37.15 | 0.0492 | take 1 (welcome used; team take cut short, not used) |
| 2026-11-22T23:03:52Z | openai/gpt-audio | marin | voice-marin.wav | 47.05 | 0.0624 | take 1 (welcome used; team take cut short, not used) |
| 2026-11-22T23:19:01Z | openai/gpt-audio | marin | voice-marin-2.wav | 49.9 | 0.0660 | team take 2 (cut short, not used) |
| 2026-11-22T23:19:40Z | openai/gpt-audio | marin | p1.wav | 36.5 | 0.0483 | team part 1 (used) |
| 2026-11-22T23:19:43Z | openai/gpt-audio | marin | p2.wav | 15.1 | 0.0203 | team part 2 (used) |
| | | | | | **0.2592** | total |
