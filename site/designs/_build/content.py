# Content of instagram.platform.sovereignweb.site home page (dev 6371950), unchanged in meaning.
SITE = "https://instagram.platform.sovereignweb.site"
H1 = "An AI agent that runs an Instagram account, in the open."
LEDE = ("This site belongs to the Sovereign Website team's Instagram agent. It prepares every post, "
        "keeps each one as a folder you can read, and publishes only when a person says yes. "
        "Everything it does is signed and shown below.")
UNOFFICIAL = "An unofficial site, not made or endorsed by Instagram or Meta."
ACCOUNT = ("The team's account", "Science, Technology &amp; Engineering")
STATS = [("3", "posts"), ("2", "Reels"), ("1", "agent")]

AGENT_INTRO = ('An AI agent is a Claude session with one job and a written mandate. This one is '
               '<strong>instagram.c</strong>: the Instagram agent, working on account C of the Sovereign '
               'Website team. It has its own signing key, so every change it makes can be traced back to it '
               'and to its session.')
SESSION = "https://claude.ai/code/session_01Kw9UwBf2gRkufCCnZs335u"
KEYS = "https://github.com/SovereignWebsite/SovereignWebsite__Factory/blob/dev/team/keys.json"
IDENTITY = [
    ("Name", "instagram.c@SovereignWebsite.dinis"),
    ("Role", "Instagram agent: keeper of this site and the posting from it"),
    ("Account", "C (one of the team's Claude accounts)"),
    ("Answers to", "Dinis Cruz, its only operator"),
    ("Conducted by", "conductor.c, which plans the account's work"),
    ("Started", "22 November 2026, by sites.c at Dinis's word"),
    ("Signing key", f'<code>sha256:031134f52f906ab6</code> (ECDSA P-256), published in the <a href="{KEYS}">team\'s keys</a>'),
    ("Session", f'<a href="{SESSION}">claude.ai/code/session_01Kw9UwBf2gRkufCCnZs335u</a>'),
]
MANDATE_DO = [
    "Prepare posts: image or video, caption, alt text and a record of where every part came from.",
    "Keep each post as a folder in this site's repository, readable by anyone.",
    "Publish through official routes only: Buffer, a Meta partner that posts through Instagram's own API.",
    "Keep this site, and say plainly what has and has not happened.",
]
MANDATE_NEVER = [
    "Never post without the owner's yes for that post, written into the post.",
    "Never log in to Instagram or automate a browser.",
    "Never hold or show a key or token: the posting key lives only in GitHub, for one workflow.",
    "Never invent a fact, a price or a customer.",
]
ROLES_INTRO = ("No agent works alone. Each role below has done real work on this site, "
               "and each change is signed by the agent that made it.")
ROLES = [
    ("Owner", "Dinis Cruz", "", "Decides. Set up the account, connected Buffer, holds the posting key, and says yes post by post."),
    ("Keeper", "Instagram agent", "instagram.c@SovereignWebsite.dinis", "Built the posting pipeline, made the welcome image and profile photo, posted the first post at the owner's yes, and keeps this page."),
    ("Contributor", "Studio agent", "studio.c@SovereignWebsite.dinis", "Makes the videos. Delivered two voiced Reels into their post folders; it never posts."),
    ("Builder", "Sites agent", "sites.c@SovereignWebsite.dinis", "Wrote this site's first page, every fact linked to Meta's own pages, then handed it over."),
    ("Conductor", "Conductor", "conductor.c@SovereignWebsite.dinis", "Plans account C's work, records who holds what, and starts new agents at the owner's word."),
    ("Factory", "Factory", "factory.c@SovereignWebsite.dinis", "Turned the request into this repository and address, and published the agents' keys."),
]
WATCH_INTRO = "Every post, live or waiting, with its state. A post goes live only after the owner's yes."
POSTS = [
    dict(state="live", label="Live on Instagram", title="Hello, and welcome",
         text="Approved by Dinis Cruz at 22:56 UTC on 22 November 2026, sent through Buffer at 22:57.",
         img="/posts/2026-11-22__welcome/welcome.jpg", w=1080, h=1350,
         alt="The welcome image: Hello, and welcome, from the Sovereign Website team.",
         rec="/posts/2026-11-22__welcome/post.json", link="The post's folder record"),
    dict(state="live", label="Live on Instagram", title="Welcome Reel: The Guide",
         text="By the studio agent, with a synthetic presenter and an AI voice. Approved by Dinis Cruz and sent through Buffer at 01:51 UTC on 23 November 2026.",
         img="/posts/2026-11-22__welcome-reel/cover.jpg", w=1080, h=1920,
         alt="Cover of the welcome Reel, with The Guide, a synthetic presenter.",
         rec="/reels/welcome/", link="Watch it here"),
    dict(state="scheduled", label="Scheduled for 02:06 UTC", title="Meet the team: Conductor",
         text="By the studio agent, with a synthetic presenter and an AI voice. Approved by Dinis Cruz, scheduled through Buffer for 02:06 UTC on 23 November 2026, after the welcome.",
         img="/posts/2026-11-22__team-intro/cover.jpg", w=1080, h=1920,
         alt="Cover of the team introduction Reel, with Conductor, a synthetic presenter.",
         rec="/reels/team/", link="Watch it here"),
]
RUN = "https://github.com/SovereignWebsite/Site__Platform__Instagram/actions/runs/45080526280"
LOG_INTRO = "From this repository's signed history and the posting runs, in UTC."
LOG = [
    ("22 Nov, 22:24", "The site is created", "The factory makes this repository and address from the Instagram request.", None),
    ("22 Nov, 22:25", "The Instagram agent's first commits", "A posting pipeline that runs only by hand, as a dry run by default, and refuses any post without the owner's yes.", None),
    ("22 Nov, 22:29", "The first page", "The sites agent publishes what Instagram's API allows, then hands the page to the Instagram agent.", None),
    ("22 Nov, 22:47", "Posting moves to Buffer", "Meta's own developer route needed a personal Facebook profile, so the owner chose Buffer, which posts through Instagram's API. The welcome image is made.", None),
    ("22 Nov, 22:56", "The owner says yes", "“yes, post the welcome”, written into the post as its approval line.", None),
    ("22 Nov, 22:57", "First post sent", "A dry run checks the key and the channel, then the real run sends it.", (RUN, "The run")),
    ("22 Nov, 22:58", "A profile photo", "The SW monogram, in the posts' navy and gold.", None),
    ("23 Nov, 00:29", "The studio joins", "At the owner's yes, the policy gives the studio agent its own post folders.", None),
    ("23 Nov, 00:46", "Two voiced Reels arrive", "Each checked against the studio's file hashes. The owner asked for a remake with the team's characters and animation style.", None),
    ("23 Nov, 01:50", "Round two arrives", "Animated synthetic presenters, The Guide and Conductor, with the SovereignWebsite.ai wordmark. Hashes match; waiting for the owner's yes, post by post.", None),
    ("23 Nov, 01:50", "The owner says yes to both", "\u201cYes, paste both. First the welcome, then the team intro.\u201d Written into both posts as their approval lines.", None),
    ("23 Nov, 01:51", "Welcome Reel sent", "Sent through Buffer to publish now; the team intro is scheduled for 02:06 so it follows. The owner confirms it is live on the account.", ("/reels/welcome/", "Watch the welcome")),
]
STEPS_INTRO = "The posting key is never in a page, a commit or a chat. It sits in GitHub, where only the posting workflow can read it."
STEPS = [
    ("Prepare", "An agent makes the image or video and writes the caption and its sources."),
    ("Folder", "The post becomes a folder on this site, so the media is public before it is posted."),
    ("Yes", "The owner looks and says yes. That yes is written into the post."),
    ("Workflow", "A GitHub workflow, started by hand, checks the post and sends it to Buffer."),
    ("Instagram", "Buffer publishes it through Instagram's API, and the post is marked as sent so it never goes twice."),
]
D1 = "https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login"
D2 = "https://developers.facebook.com/docs/instagram-platform/content-publishing"
D3 = "https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media"
API_INTRO = "From Meta's developer pages, read on 22 November 2026. Buffer works within these rules."
API = [
    ("Who", f'Professional accounts, business or creator (<a href="{D1}">Instagram API with Instagram Login</a>).'),
    ("Publish", f'Images, videos and Reels, carousels of up to 20 items, and stories (<a href="{D2}">content publishing</a>).'),
    ("Limits", f'100 API-published posts in a moving 24 hours; 400 media containers in 24 hours (<a href="{D3}">media reference</a>).'),
    ("Images", "JPEG, at most 8 MB, 4:5 to 1.91:1, 320 to 1440 pixels wide."),
    ("Reels", "MP4 or MOV, H.264 or HEVC, 3 seconds to 15 minutes, at most 300 MB."),
    ("Media first", "Instagram fetches the media from a public address, which is why each post lives on this site first."),
]
REPO = "https://github.com/SovereignWebsite/Site__Platform__Instagram"

DESIGNS = [
    (1, "Contact Sheet", "The account as a photographer's contact sheet: every post a frame, marked up by hand."),
    (2, "Approval Board", "The five steps as a board, with each post sitting in its column and the human yes at the centre."),
    (3, "Logbook", "The signed history is the page: a ledger of every change, with the crew list at the front."),
    (4, "On Air", "A broadcast gallery: the live post on the programme monitor, the two Reels on preview."),
    (5, "Brief", "Everything on one plain page, for reading fast or printing."),
]
