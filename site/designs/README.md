# Five designs of instagram.platform.sovereignweb.site

Round 1 by design.c@SovereignWebsite.dinis (account C), 23 November 2026. The same facts as the home page at dev a0145a2, in five ideas from the Instagram agent's own world (guidelines 2a and 12 of SovereignWebsite/Site__Agent__Design). The owner (Dinis Cruz) picks one; the keeper (instagram.c) applies it. Until then the home page stays as it is.

Each design is a static page with its own CSS inline, no script, no request to another host, light and dark, and the same seed links (start, agents, admin, policy, llms.txt). "Choose a design" and our family links sit in two small menus at the top right.

## Round 2 (23 November 2026, 02:44 UTC)

The account is RiskMandate's, connected to Sovereign Website (Dinis Cruz, as relayed by instagram.c). All five now carry RiskMandate's look from riskmandate.ai: paper #F7F6F2, ink #161615, green #1A7F5A, with a lighter green #3fbf8c for text on ink (the brand green on ink is 3.65:1, under AA). RiskMandate's mark (CC BY 4.0, copied to `assets/riskmandate-mark.svg` so nothing loads from another host) sits in each header, the new profile photo in design 2, and a line "RiskMandate, part of Sovereign Website" at the top. The words are the home page's own until instagram.c rewords them.

## The five

1. **Contact Sheet.** Philosophy: an Instagram account is a run of frames, chosen by a person. Narrative: the headline, then the account as a dark contact sheet, each post a numbered frame with a grease-pencil mark (circled and marked "Sent" once it has gone out; a post still waiting would carry "Yes?"), an empty next frame ready for the next post. Then agent, roles, posts, log, steps and API as captioned sheets. RiskMandate paper (#F7F6F2), ink (#161615) sheet, green (#1A7F5A) pencil, serif headlines.
2. **Approval Board** (dark first). Philosophy: the site exists to show that nothing goes out without a person's yes. Narrative: the five steps are the page's spine, as columns; each post sits in its column (today the welcome post and the welcome Reel in "Instagram", the team Reel in "Workflow" until Buffer sends it at 02:06; a post waiting for the owner sits in the gold "Yes" column). Agent, roles and log follow as the shift record. RiskMandate ink (#161615) with its green; light on its paper.
3. **Logbook.** Philosophy: trust comes from a signed history. Narrative: a cover, then pages: the keeper, the crew list (a table), the numbered log, the posts as entries, the five steps as standing orders, and the API as regulations. RiskMandate paper and ink, green as the ledger ink.
4. **On Air** (dark first, way out there). Philosophy: posting is broadcasting. Narrative: a gallery of monitors: the live post on the red programme monitor with the headline, the two Reels on green preview monitors; then the rundown (the five steps, the human yes in red), the agent, the credits, the transmission log and the technical standards. RiskMandate ink, with tally red, RiskMandate green as preview, and amber.
5. **Brief.** Everything on one plain page for reading fast or printing.

## Rating (Site__Agent__Design docs/rating.md)

Checked locally on 23 November 2026, at 320, 390 and 1366 px, light and dark: axe-core 4.10.2 (WCAG 2.2 AA plus best practice) finds nothing serious or critical; no sideways scroll; no request to another host; no em or en dashes.

| Design | Rating | What holds it |
|---|---|---|
| 1. Contact Sheet | 3 (candidate) | Synthetic users not yet run; the empty frame needs the owner's next post. |
| 2. Approval Board | 3 (candidate) | Synthetic users not yet run; on a phone the columns stack, so the board reads as a list. |
| 3. Logbook | 3 (candidate) | Synthetic users not yet run; quietest of the four, closest to a Brief. |
| 4. On Air | 3 (candidate) | Synthetic users not yet run; the strongest first screen, the busiest on a phone. |
| 5. Brief | 3 (candidate) | The plain version by design. |

Level 4 needs the hand checks, the synthetic users and the owner's "wow"; those come in round 2.

## Recommendation

**2, Approval Board.** It puts the site's one promise, a person's yes before every post, at the centre of the page, and the same board can become the "awaiting approval" and "live on Instagram" areas the owner asked for on the studio site. On Air is the second choice if the owner wants the most striking first screen.

## How to rebuild

The pages are generated from `_build/content.py` by `_build/build.py` (run `python3 site/designs/_build/build.py site` from the repository root). A change to the home page's facts means a new round, not a hand edit here.
