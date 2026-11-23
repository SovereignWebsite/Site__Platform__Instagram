#!/usr/bin/env python3
"""Builds site/designs/ for instagram.platform.sovereignweb.site: five designs of the same facts.
design.c@SovereignWebsite.dinis, round 1. Usage: build.py <site dir>"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *

OUT = os.path.join(sys.argv[1], "designs")

FAMILY = [("https://sovereignwebsite.ai/", "Sovereign Website"), ("https://sovereignwebsite.org/", "Principles"),
          ("https://sovereignwebsite.site/", "Hosted"), ("https://hub.sovereignweb.site/", "Hub"),
          ("https://agents.sovereignweb.site/", "Agents"), ("https://vault.sovereignwebsite.site/", "Vault"),
          ("https://agenticcells.ai/", "AgentiCCells"), ("https://riskmandate.ai/", "RiskMandate"),
          ("https://newsroom.sgit.ai/", "Newsroom")]

BASE_CSS = """
*{box-sizing:border-box}
html{color-scheme:light dark;-webkit-text-size-adjust:100%}
body{margin:0;font:1.0625rem/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--fg);overflow-wrap:break-word}
img{max-width:100%;height:auto;display:block}
a{color:var(--link)}
a:hover{text-decoration-thickness:2px}
:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.skip{position:absolute;left:-999px;top:.5rem;z-index:99;background:var(--bg);color:var(--fg);padding:.5rem .9rem;border:2px solid var(--focus)}
.skip:focus{left:1rem}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.92em;overflow-wrap:anywhere}
.chrome{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;justify-content:flex-end;position:relative;z-index:5}
.chrome details{position:relative}
.chrome summary{cursor:pointer;list-style:none;min-height:44px;display:inline-flex;align-items:center;padding:.35rem .8rem;border:1px solid var(--ctl);border-radius:999px;font-size:.9rem;background:var(--bg);color:var(--fg)}
.chrome summary::-webkit-details-marker{display:none}
.chrome summary::after{content:"";width:.45rem;height:.45rem;margin-left:.5rem;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg) translateY(-2px)}
.chrome details[open] summary::after{transform:rotate(-135deg)}
.chrome ul{position:absolute;right:0;top:calc(100% + .35rem);margin:0;padding:.4rem;list-style:none;min-width:15rem;max-width:calc(100vw - 2rem);background:var(--bg);color:var(--fg);border:1px solid var(--ctl);border-radius:.6rem;box-shadow:0 .6rem 1.6rem rgba(0,0,0,.25)}
.chrome li a{display:block;padding:.55rem .7rem;border-radius:.4rem;color:var(--fg);text-decoration:none;font-size:.95rem}
.chrome li a:hover,.chrome li a:focus-visible{background:var(--hover)}
.chrome li a[aria-current]{font-weight:700;text-decoration:underline}
.chrome .gap{border-top:1px solid var(--ctl);margin-top:.3rem;padding-top:.3rem}
.chrome small{display:block;font-size:.85rem;color:var(--muted);font-weight:400}
main *{min-width:0}
dd,.agent,.roles h3{overflow-wrap:anywhere}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media print{.chrome,.skip{display:none}}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
"""


def head(n, name, idea, css):
    title = f"{name}, design {n} of Instagram"
    desc = f"Design {n} of instagram.platform.sovereignweb.site, {name}: {idea} Unofficial, not made or endorsed by Instagram or Meta."
    url = f"{SITE}/designs/{n}/"
    img = f"{SITE}/assets/share/card-1200x630.jpg"
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Instagram">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Instagram">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">
<link rel="canonical" href="{url}">
<style>{BASE_CSS}{css}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def chrome(n):
    d = "".join(
        f'<li><a href="/designs/{i}/"{" aria-current=\"page\"" if i == n else ""}>{i}. {nm}<small>{idea}</small></a></li>'
        for i, nm, idea in DESIGNS)
    fam = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in FAMILY)
    return f"""<div class="chrome">
<details class="choose"><summary>Choose a design</summary><ul>{d}<li class="gap"><a href="/designs/">All five, side by side</a></li><li><a href="/">The site as it is now</a></li></ul></details>
<details class="family"><summary>Sovereign Website</summary><ul><li><a href="/start/">Start here</a></li><li><a href="/agents/">Use with your AI</a></li><li><a href="/admin/">How this site was made</a></li><li class="gap"><a href="/policy/">How this site is governed</a></li>{fam}</ul></details>
</div>"""


def owner_links(cls=""):
    return f'<nav class="{cls}" aria-label="This site"><a href="#agent">The agent</a><a href="#watch">Watch it work</a><a href="/start/">Start here</a><a href="/agents/">Use with your AI</a><a href="/admin/">How it was made</a></nav>'


def footer(cls=""):
    return f"""<footer class="{cls}">
<nav aria-label="Seed pages"><a href="/start/">Start here</a> <a href="/agents/">Use with your AI</a> <a href="/admin/">How this site was made</a> <a href="/policy/">How this site is governed</a> <a href="/llms.txt">llms.txt</a></nav>
<p>A sovereign website: no cookies, no tracking, static files only. Source: <a href="{REPO}">github.com/SovereignWebsite/Site__Platform__Instagram</a>. {UNOFFICIAL}</p>
</footer>
</body>
</html>
"""


def identity_dl(cls="id"):
    return f'<dl class="{cls}">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in IDENTITY) + "</dl>"


def mandate(cls="mandate"):
    do = "".join(f"<li>{x}</li>" for x in MANDATE_DO)
    nv = "".join(f"<li>{x}</li>" for x in MANDATE_NEVER)
    return f'<div class="{cls}"><div><h3>It does</h3><ul>{do}</ul></div><div><h3>It never</h3><ul>{nv}</ul></div></div><p><a href="/policy/">The full policy for this site</a></p>'


def api_dl(cls="api"):
    return f'<dl class="{cls}">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in API) + "</dl>"


def log_items(cls="log"):
    out = []
    for t, h, p, link in LOG:
        extra = f' <a href="{link[0]}">{link[1]}</a>' if link else ""
        out.append(f'<li><time>{t}</time><div><h3>{h}</h3><p>{p}{extra}</p></div></li>')
    return f'<ol class="{cls}">' + "".join(out) + "</ol>"


def steps_ol(cls="steps"):
    return f'<ol class="{cls}">' + "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in STEPS) + "</ol>"


def roles_list(cls="roles"):
    out = []
    for role, who, agent, did in ROLES:
        a = f"<p class=\"agent\"><code>{agent}</code></p>" if agent else ""
        out.append(f'<li><p class="role">{role}</p><h3>{who}</h3>{a}<p>{did}</p></li>')
    return f'<ul class="{cls}">' + "".join(out) + "</ul>"


def post_fig(p, lazy=True, cls="post"):
    ld = ' loading="lazy"' if lazy else ""
    return (f'<article class="{cls} {p["state"]}"><img src="{p["img"]}" alt="{p["alt"]}" width="{p["w"]}" height="{p["h"]}"{ld}>'
            f'<div class="body"><p class="state"><span>{p["label"]}</span></p><h3>{p["title"]}</h3><p>{p["text"]}</p>'
            f'<p><a href="{p["rec"]}">{p["link"]}<span class="vh">: {p["title"]}</span></a></p></div></article>')


# ---------------------------------------------------------------- 1. Contact Sheet
CSS1 = """
:root{--bg:#f4efe6;--fg:#1d1a16;--muted:#5a5249;--link:#a3271b;--focus:#a3271b;--ctl:#8a8076;--hover:#e8e0d2;--sheet:#25211d;--on-sheet:#f4efe6;--pencil:#a3271b;--line:#d9cfbf;--card:#fffdf8}
@media (prefers-color-scheme:dark){:root{--bg:#171512;--fg:#efe9df;--muted:#bdb3a6;--link:#ff8a78;--focus:#ff8a78;--ctl:#8f857a;--hover:#2a2622;--sheet:#0b0a09;--on-sheet:#efe9df;--pencil:#ff8a78;--line:#3a352f;--card:#211e1a}}
.wrap{max-width:68rem;margin:0 auto;padding:0 1rem}
.mast{display:flex;flex-wrap:wrap;gap:.75rem;align-items:center;justify-content:space-between;padding:.75rem 0}
.brand{font:700 1.25rem/1.1 Georgia,"Iowan Old Style","Times New Roman",serif;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.own{display:flex;flex-wrap:wrap;gap:.25rem 1rem;font-size:.95rem;padding-bottom:.5rem}
.own a{color:var(--fg);min-height:44px;display:inline-flex;align-items:center}
.hero{padding:clamp(1.5rem,6vw,4rem) 0 1rem}
.eyebrow{text-transform:uppercase;letter-spacing:.12em;font-size:.85rem;color:var(--muted);margin:0 0 .5rem}
h1,h2{font-family:Georgia,"Iowan Old Style","Times New Roman",serif;line-height:1.1}
h1{font-size:clamp(2.1rem,6.5vw,3.9rem);margin:0 0 1rem;max-width:18ch}
h2{font-size:clamp(1.45rem,3.6vw,2rem);margin:0 0 .5rem}
h3{font-size:1.1rem;margin:0 0 .25rem}
.lede{font-size:1.15rem;max-width:42rem}
.small{color:var(--muted);font-size:.95rem}
.sheet{background:var(--sheet);color:var(--on-sheet);padding:clamp(1rem,4vw,2rem);margin:1.5rem 0;border-radius:.3rem;position:relative}
.sheet .edge{display:flex;justify-content:space-between;font:700 .85rem/1 ui-monospace,Menlo,Consolas,monospace;letter-spacing:.1em;color:#e8c27a;margin-bottom:.75rem;flex-wrap:wrap;gap:.5rem}
.frames{list-style:none;margin:0;padding:0;display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,14rem),1fr))}
.frames li{position:relative;background:#000;padding:.5rem .5rem 2.2rem}
.frames img{aspect-ratio:4/5;object-fit:cover;width:100%}
.frames .num{position:absolute;left:.6rem;bottom:.55rem;font:700 .85rem ui-monospace,Menlo,Consolas,monospace;color:#e8c27a}
.frames .mark{position:absolute;right:.5rem;bottom:.4rem;font:700 .95rem Georgia,serif;color:#fff;background:#a3271b;padding:.1rem .55rem;border-radius:999px;transform:rotate(-4deg)}
.frames li.live::after{content:"";position:absolute;inset:.1rem;border:3px solid #ff6b57;border-radius:46% 54% 50% 50%/52% 48% 52% 48%;pointer-events:none;transform:rotate(-1.5deg)}
.frames .empty{display:grid;place-items:center;aspect-ratio:4/5;color:#cfc6b8;font-size:.95rem;text-align:center;border:1px dashed #6d655b}
.cta{display:flex;flex-wrap:wrap;gap:.75rem;margin:1.25rem 0}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:.6rem 1.1rem;border-radius:.3rem;font-weight:600;text-decoration:none}
.btn.primary{background:var(--pencil);color:#fff}
@media (prefers-color-scheme:dark){.btn.primary{color:#1a0f0d}}
.btn.ghost{border:2px solid var(--fg);color:var(--fg)}
.stats{display:flex;gap:1.5rem;margin:.5rem 0 0;flex-wrap:wrap}
.stats div{font-size:.95rem}.stats b{font:700 1.6rem Georgia,serif;display:block}
section{padding:clamp(2.2rem,6vw,4rem) 0;border-top:1px solid var(--line)}
.kicker{font:700 .85rem ui-monospace,Menlo,Consolas,monospace;color:var(--pencil);letter-spacing:.08em;margin:0 0 .4rem}
.intro{max-width:42rem}
.two{display:grid;gap:2rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,22rem),1fr))}
.id{margin:0;display:grid;gap:.1rem}
.id div{display:grid;grid-template-columns:8.5rem 1fr;gap:.75rem;padding:.55rem 0;border-bottom:1px dashed var(--line)}
.id dt{color:var(--muted);font-size:.95rem}.id dd{margin:0}
@media (max-width:30rem){.id div{grid-template-columns:1fr;gap:0}}
.mandate{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,16rem),1fr))}
.mandate ul{padding-left:1.1rem;margin:.25rem 0}
.mandate li{margin:.35rem 0}
.roles{list-style:none;margin:1.5rem 0 0;padding:0;display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,16rem),1fr))}
.roles li{background:var(--card);border:1px solid var(--line);padding:1rem;border-radius:.3rem}
.roles .role{margin:0;font:700 .85rem ui-monospace,Menlo,Consolas,monospace;color:var(--pencil);text-transform:uppercase;letter-spacing:.08em}
.roles .agent{margin:0 0 .4rem;color:var(--muted);font-size:.9rem}
.roles p{margin:.3rem 0}
.posts{display:grid;gap:1.25rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,18rem),1fr));margin-top:1.5rem}
.post{background:var(--card);border:1px solid var(--line);border-radius:.3rem;overflow:hidden}
.post img{aspect-ratio:4/5;object-fit:cover;width:100%}
.post .body{padding:1rem}.post .body p{margin:.35rem 0}
.state span{font:700 .85rem ui-monospace,Menlo,Consolas,monospace;padding:.15rem .5rem;border-radius:999px;border:2px solid currentColor}
.post.live .state{color:#1f6b45}.post.review .state,.post.scheduled .state{color:#8a4b00}
@media (prefers-color-scheme:dark){.post.live .state{color:#7fdcae}.post.review .state,.post.scheduled .state{color:#ffc46b}}
.log{list-style:none;margin:1.5rem 0 0;padding:0;columns:2 22rem;column-gap:2rem}
.log li{break-inside:avoid;display:grid;grid-template-columns:7.5rem 1fr;gap:.75rem;padding:.6rem 0;border-bottom:1px dashed var(--line)}
.log time{font:700 .9rem ui-monospace,Menlo,Consolas,monospace;color:var(--pencil)}
.log p{margin:.2rem 0 0}
@media (max-width:30rem){.log li{grid-template-columns:1fr;gap:.2rem}}
.steps{counter-reset:s;list-style:none;margin:1.5rem 0 0;padding:0;display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,11rem),1fr))}
.steps li{counter-increment:s;border-top:4px solid var(--fg);padding-top:.6rem}
.steps li:nth-child(3){border-top-color:var(--pencil)}
.steps li::before{content:"Frame " counter(s);font:700 .85rem ui-monospace,Menlo,Consolas,monospace;color:var(--muted)}
.steps p{margin:.25rem 0}
.api{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,18rem),1fr));margin:1.5rem 0 0}
.api div{border-left:4px solid var(--pencil);padding-left:.9rem}
.api dt{font-weight:700}.api dd{margin:.2rem 0 0}
footer{border-top:1px solid var(--line);padding:2rem 0 3rem;font-size:.95rem}
footer nav{display:flex;flex-wrap:wrap;gap:.25rem 1.25rem}
footer nav a{min-height:44px;display:inline-flex;align-items:center}
"""


def d1():
    n = 1
    frames = []
    for i, p in enumerate(POSTS, 1):
        mark = {"live": "Sent", "scheduled": "02:06"}.get(p["state"], "Yes?")
        frames.append(f'<li class="{p["state"]}"><img src="{p["img"]}" alt="{p["alt"]}" width="{p["w"]}" height="{p["h"]}"><span class="num">{i:02d}A</span><span class="mark">{mark}</span></li>')
    frames.append('<li><div class="empty">Next frame: the next post, once there is one</div><span class="num">04A</span></li>')
    stats = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in STATS)
    return head(n, "Contact Sheet", DESIGNS[0][2], CSS1) + f"""<div class="wrap">
{chrome(n)}
<header class="mast"><a class="brand" href="/">Instagram</a>{owner_links("own")}</header>
</div>
<main id="main">
<div class="wrap hero">
<p class="eyebrow">instagram.platform.sovereignweb.site</p>
<h1>{H1}</h1>
<p class="lede">{LEDE}</p>
<div class="cta"><a class="btn primary" href="#watch">See what it has done</a><a class="btn ghost" href="#agent">Meet the agent</a></div>
<p class="small">{UNOFFICIAL}</p>
<div class="sheet" role="group" aria-label="The account as a contact sheet">
<p class="edge"><span>{ACCOUNT[0].upper()}</span><span>{ACCOUNT[1].upper()}</span></p>
<ul class="frames">{''.join(frames)}</ul>
<div class="stats">{stats}</div>
</div>
</div>
<section id="agent"><div class="wrap">
<p class="kicker">The agent</p>
<h2>What is the Instagram agent?</h2>
<p class="intro">{AGENT_INTRO}</p>
<div class="two">{identity_dl()}<div><h2>Its mandate</h2>{mandate()}</div></div>
</div></section>
<section id="roles"><div class="wrap">
<p class="kicker">The roles in action</p>
<h2>Who does what</h2>
<p class="intro">{ROLES_INTRO}</p>
{roles_list()}
</div></section>
<section id="watch"><div class="wrap">
<p class="kicker">Watch it work</p>
<h2>What the Instagram agent has been doing on account C</h2>
<p class="intro">{WATCH_INTRO}</p>
<div class="posts">{''.join(post_fig(p) for p in POSTS)}</div>
</div></section>
<section id="log"><div class="wrap">
<p class="kicker">The log</p>
<h2>Every change, in order</h2>
<p class="intro">{LOG_INTRO}</p>
{log_items()}
</div></section>
<section id="how"><div class="wrap">
<p class="kicker">How a post goes out</p>
<h2>Five steps, one of them human</h2>
<p class="intro">{STEPS_INTRO}</p>
{steps_ol()}
</div></section>
<section id="api"><div class="wrap">
<p class="kicker">What the platform allows</p>
<h2>Instagram's official API, in brief</h2>
<p class="intro">{API_INTRO}</p>
{api_dl()}
</div></section>
</main>
<div class="wrap">{footer()}</div>"""


# ---------------------------------------------------------------- 2. Approval Board (dark first)
CSS2 = """
:root{--bg:#0f1a2b;--fg:#eef1f6;--muted:#b3bfd0;--link:#ffcf6e;--focus:#ffcf6e;--ctl:#7d8ca3;--hover:#1c2a42;--col:#16243a;--card:#1f3150;--line:#2c4064;--gold:#ffcf6e;--on-gold:#1a1300;--ok:#7fdcae;--wait:#ffcf6e}
@media (prefers-color-scheme:light){:root{--bg:#eef2f8;--fg:#0f1a2b;--muted:#46536a;--link:#7a4e00;--focus:#7a4e00;--ctl:#6a7890;--hover:#dfe6f1;--col:#ffffff;--card:#f6f8fc;--line:#c9d3e3;--gold:#7a4e00;--on-gold:#ffffff;--ok:#1d6b45;--wait:#7a4e00}}
.wrap{max-width:84rem;margin:0 auto;padding:0 1rem}
.mast{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.5rem 1rem;padding:.75rem 0;border-bottom:1px solid var(--line)}
.brand{font-weight:800;font-size:1.2rem;color:var(--fg);text-decoration:none;display:inline-flex;align-items:center;gap:.6rem;min-height:44px}
.brand img{width:2rem;height:2rem;border-radius:50%}
.own{display:flex;flex-wrap:wrap;gap:.25rem 1rem;font-size:.95rem}
.own a{color:var(--fg);min-height:44px;display:inline-flex;align-items:center}
.hero{display:grid;gap:1.5rem;padding:clamp(1.5rem,5vw,3rem) 0;grid-template-columns:repeat(auto-fit,minmax(min(100%,24rem),1fr));align-items:end}
.eyebrow{font-size:.85rem;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);margin:0 0 .5rem}
h1{font-size:clamp(2.1rem,6vw,3.6rem);line-height:1.05;margin:0 0 1rem;letter-spacing:-.02em}
h2{font-size:clamp(1.45rem,3.4vw,2rem);line-height:1.15;margin:0 0 .5rem}
h3{font-size:1.05rem;margin:0 0 .25rem}
.lede{font-size:1.1rem;max-width:42rem;margin:0}
.facts{display:flex;flex-wrap:wrap;gap:.75rem}
.facts div{background:var(--col);border:1px solid var(--line);border-radius:.6rem;padding:.75rem 1rem;min-width:7rem}
.facts b{display:block;font-size:2rem;line-height:1}
.facts .small{font-size:.9rem;color:var(--muted)}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:.6rem 1.1rem;border-radius:.5rem;font-weight:700;text-decoration:none;background:var(--gold);color:var(--on-gold);margin-top:1rem}
.note{color:var(--muted);font-size:.95rem}
.board-h{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:.5rem}
.board{list-style:none;margin:1rem 0 0;padding:0 0 1rem;display:grid;gap:.75rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,13.5rem),1fr));counter-reset:c}
.board>li{counter-increment:c;background:var(--col);border:1px solid var(--line);border-radius:.75rem;padding:.9rem;display:flex;flex-direction:column;gap:.6rem}
.board>li.human{border:2px solid var(--gold)}
.board .colh{display:flex;justify-content:space-between;align-items:baseline;gap:.5rem}
.board .colh h3::before{content:counter(c) ". ";color:var(--muted)}
.board .count{font-size:.85rem;color:var(--muted)}
.board>li>p{margin:0;font-size:.95rem;color:var(--muted)}
.ticket{background:var(--card);border:1px solid var(--line);border-radius:.6rem;overflow:hidden}
.ticket img{aspect-ratio:1/1;object-fit:cover;width:100%}
.ticket .body{padding:.7rem}.ticket .body p{margin:.3rem 0;font-size:.95rem}
.ticket h4{margin:.2rem 0;font-size:1rem}
.pill{display:inline-block;font-size:.85rem;font-weight:700;border:2px solid currentColor;border-radius:999px;padding:.05rem .55rem}
.ticket.live .pill{color:var(--ok)}.ticket.review .pill,.ticket.scheduled .pill{color:var(--wait)}
.lane-empty{border:1px dashed var(--ctl);border-radius:.6rem;padding:.7rem;font-size:.95rem;color:var(--muted)}
section{padding:clamp(2.2rem,6vw,4rem) 0;border-top:1px solid var(--line)}
.intro{max-width:42rem}
.shift{display:grid;gap:1.5rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,22rem),1fr))}
.id{margin:0;background:var(--col);border:1px solid var(--line);border-radius:.75rem;padding:.5rem 1rem}
.id div{display:grid;grid-template-columns:8rem 1fr;gap:.75rem;padding:.55rem 0;border-bottom:1px solid var(--line)}
.id div:last-child{border:0}
.id dt{color:var(--muted);font-size:.95rem}.id dd{margin:0}
@media (max-width:30rem){.id div{grid-template-columns:1fr;gap:0}}
.mandate{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,15rem),1fr))}
.mandate>div{background:var(--col);border:1px solid var(--line);border-radius:.75rem;padding:1rem}
.mandate>div:last-child{border-color:var(--gold)}
.mandate ul{margin:.3rem 0;padding-left:1.1rem}.mandate li{margin:.35rem 0}
.roles{list-style:none;margin:1.25rem 0 0;padding:0;display:grid;gap:.75rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,15rem),1fr))}
.roles li{background:var(--col);border:1px solid var(--line);border-radius:.75rem;padding:1rem}
.roles li:first-child{border:2px solid var(--gold)}
.roles .role{margin:0;font-size:.85rem;text-transform:uppercase;letter-spacing:.1em;color:var(--gold);font-weight:700}
.roles .agent{margin:0;color:var(--muted);font-size:.9rem}
.roles p{margin:.3rem 0}
.log{list-style:none;margin:1.25rem 0 0;padding:0;display:grid;gap:.5rem}
.log li{display:grid;grid-template-columns:8rem 1fr;gap:1rem;background:var(--col);border:1px solid var(--line);border-radius:.6rem;padding:.7rem 1rem}
.log time{font-family:ui-monospace,Menlo,Consolas,monospace;color:var(--gold);font-size:.95rem}
.log p{margin:.2rem 0 0}
@media (max-width:30rem){.log li{grid-template-columns:1fr;gap:.2rem}}
.api{display:grid;gap:.75rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,17rem),1fr));margin:1.25rem 0 0}
.api div{background:var(--col);border:1px solid var(--line);border-radius:.6rem;padding:.9rem}
.api dt{font-weight:700;color:var(--gold)}.api dd{margin:.2rem 0 0}
footer{border-top:1px solid var(--line);padding:2rem 0 3rem;font-size:.95rem}
footer nav{display:flex;flex-wrap:wrap;gap:.25rem 1.25rem}
footer nav a{min-height:44px;display:inline-flex;align-items:center}
"""


def ticket(p):
    return (f'<article class="ticket {p["state"]}"><img src="{p["img"]}" alt="{p["alt"]}" width="{p["w"]}" height="{p["h"]}" loading="lazy">'
            f'<div class="body"><span class="pill">{p["label"]}</span><h4>{p["title"]}</h4><p>{p["text"]}</p>'
            f'<p><a href="{p["rec"]}">{p["link"]}<span class="vh">: {p["title"]}</span></a></p></div></article>')


def d2():
    n = 2
    live = [p for p in POSTS if p["state"] == "live"]
    rev = [p for p in POSTS if p["state"] == "review"]
    sched = [p for p in POSTS if p["state"] == "scheduled"]
    cols = []
    for i, (h, txt) in enumerate(STEPS):
        cards = ""
        cnt = 0
        if h == "Yes":
            cards = "".join(ticket(p) for p in rev); cnt = len(rev)
        elif h == "Instagram":
            cards = "".join(ticket(p) for p in live); cnt = len(live)
        elif h == "Workflow" and sched:
            cards = "".join(ticket(p) for p in sched); cnt = len(sched)
        else:
            cards = '<p class="lane-empty">Nothing waiting here now.</p>'
        cls = ' class="human"' if h == "Yes" else ""
        cols.append(f'<li{cls}><div class="colh"><h3>{h}</h3><span class="count">{cnt} {"post" if cnt == 1 else "posts"}</span></div><p>{txt}</p>{cards}</li>')
    facts = "".join(f'<div><b>{a}</b><span class="small">{b}</span></div>' for a, b in STATS)
    return head(n, "Approval Board", DESIGNS[1][2], CSS2) + f"""<div class="wrap">
{chrome(n)}
<header class="mast"><a class="brand" href="/"><img src="/assets/instagram/profile-1080.jpg" alt="" width="1080" height="1080">Instagram</a>{owner_links("own")}</header>
</div>
<main id="main">
<div class="wrap">
<div class="hero">
<div><p class="eyebrow">instagram.platform.sovereignweb.site</p><h1>{H1}</h1><p class="lede">{LEDE}</p><a class="btn" href="#watch">See what it has done</a></div>
<div><p class="note">{ACCOUNT[0]}, {ACCOUNT[1]}</p><div class="facts">{facts}</div><p class="note">{UNOFFICIAL}</p></div>
</div>
<div id="watch">
<div class="board-h"><h2>Watch it work: the board</h2><p class="note">{WATCH_INTRO}</p></div>
<p class="intro">{STEPS_INTRO} Five steps, one of them human: the gold column.</p>
<ol class="board" aria-label="How a post goes out, with each post in its step">{''.join(cols)}</ol>
</div>
</div>
<section id="agent"><div class="wrap">
<h2>Who is on shift: the Instagram agent</h2>
<p class="intro">{AGENT_INTRO}</p>
<div class="shift">{identity_dl()}<div><h3>Its mandate</h3>{mandate()}</div></div>
</div></section>
<section id="roles"><div class="wrap">
<h2>Who does what</h2>
<p class="intro">{ROLES_INTRO}</p>
{roles_list()}
</div></section>
<section id="log"><div class="wrap">
<h2>The log</h2>
<p class="intro">{LOG_INTRO}</p>
{log_items()}
</div></section>
<section id="api"><div class="wrap">
<h2>What the platform allows: Instagram's official API, in brief</h2>
<p class="intro">{API_INTRO}</p>
{api_dl()}
</div></section>
</main>
<div class="wrap">{footer()}</div>"""


# ---------------------------------------------------------------- 3. Logbook
CSS3 = """
:root{--bg:#f3ecdc;--fg:#231d14;--muted:#5b5141;--link:#1f4f7a;--focus:#1f4f7a;--ctl:#857a66;--hover:#e7dcc5;--rule:#c9b993;--ink:#1f4f7a;--paper:#fbf6ea;--seal:#8c2a1c}
@media (prefers-color-scheme:dark){:root{--bg:#1a1712;--fg:#efe7d6;--muted:#c2b7a2;--link:#9cc8f0;--focus:#9cc8f0;--ctl:#8d826e;--hover:#2a251d;--rule:#4a4234;--ink:#9cc8f0;--paper:#221e17;--seal:#f09a8a}}
body{font-size:1.0625rem}
.wrap{max-width:62rem;margin:0 auto;padding:0 1rem}
.mast{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.5rem;padding:.75rem 0;border-bottom:3px double var(--rule)}
.brand{font:italic 700 1.35rem Georgia,"Iowan Old Style","Times New Roman",serif;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.own{display:flex;flex-wrap:wrap;gap:.25rem 1rem;font-size:.95rem}
.own a{color:var(--fg);min-height:44px;display:inline-flex;align-items:center}
h1,h2,h3{font-family:Georgia,"Iowan Old Style","Times New Roman",serif}
.cover{padding:clamp(2rem,7vw,5rem) 0 2rem;text-align:center}
.cover .vol{font:600 .9rem ui-monospace,Menlo,Consolas,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.cover h1{font-size:clamp(2.1rem,6.4vw,3.8rem);line-height:1.08;margin:.75rem auto 1rem;max-width:20ch}
.cover .lede{max-width:40rem;margin:0 auto;font-size:1.12rem}
.cover .small{color:var(--muted);font-size:.95rem}
.cover .open{display:inline-flex;align-items:center;min-height:44px;margin-top:1.25rem;padding:.55rem 1.2rem;border:2px solid var(--ink);color:var(--ink);font-weight:700;text-decoration:none;border-radius:.2rem}
.page{background:var(--paper);border:1px solid var(--rule);box-shadow:0 1px 0 var(--rule),0 .4rem 0 -.2rem var(--paper),0 .4rem 0 -.15rem var(--rule);padding:clamp(1rem,4vw,2.5rem);margin:2rem 0}
.page>h2{font-size:clamp(1.45rem,3.6vw,2rem);margin:0 0 .25rem;border-bottom:1px solid var(--rule);padding-bottom:.4rem}
.page>.sub{color:var(--muted);margin:.4rem 0 1rem;font-size:.98rem}
.crew{width:100%;border-collapse:collapse}
.crew th,.crew td{text-align:left;vertical-align:top;padding:.55rem .5rem;border-bottom:1px solid var(--rule)}
.crew th{font:700 .85rem ui-monospace,Menlo,Consolas,monospace;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.crew td code{font-size:.85rem;color:var(--muted)}
.tablebox{overflow-x:auto}
@media (max-width:40rem){.crew thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}.crew tr{display:block;border-bottom:1px solid var(--rule);padding:.5rem 0}.crew td{display:block;border:0;padding:.15rem 0}.crew td:first-child{font:700 .85rem ui-monospace,Menlo,Consolas,monospace;color:var(--seal);text-transform:uppercase;letter-spacing:.08em}}
.ledger{list-style:none;margin:0;padding:0;counter-reset:e}
.ledger li{counter-increment:e;display:grid;grid-template-columns:3rem 8.5rem 1fr;gap:.75rem;padding:.75rem 0;border-bottom:1px solid var(--rule);align-items:baseline}
.ledger li::before{content:counter(e,decimal-leading-zero);font:700 .9rem ui-monospace,Menlo,Consolas,monospace;color:var(--muted)}
.ledger time{font:700 .95rem ui-monospace,Menlo,Consolas,monospace;color:var(--ink)}
.ledger h3{font-size:1.1rem;margin:0}
.ledger p{margin:.2rem 0 0}
.ledger .sig{display:inline-block;margin-top:.3rem;font:italic .9rem Georgia,serif;color:var(--seal)}
@media (max-width:34rem){.ledger li{grid-template-columns:2.25rem 1fr}.ledger li>div{grid-column:2}}
.entries{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,16rem),1fr))}
.post{border:1px solid var(--rule);background:var(--bg);padding:.6rem}
.post img{aspect-ratio:4/5;object-fit:cover;width:100%;filter:saturate(.9)}
.post .body p{margin:.3rem 0}
.state span{font:700 .85rem ui-monospace,Menlo,Consolas,monospace;text-transform:uppercase;letter-spacing:.08em}
.post.live .state{color:#1d6b45}.post.review .state{color:var(--seal)}
@media (prefers-color-scheme:dark){.post.live .state{color:#86ddb3}}
.id{margin:0}
.id div{display:grid;grid-template-columns:9rem 1fr;gap:.75rem;padding:.45rem 0;border-bottom:1px dotted var(--rule)}
.id dt{font-style:italic;color:var(--muted)}.id dd{margin:0}
@media (max-width:30rem){.id div{grid-template-columns:1fr;gap:0}}
.mandate{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,15rem),1fr));margin-top:1rem}
.mandate h3{font-size:1.1rem;margin:0}
.mandate ul{margin:.3rem 0;padding-left:1.1rem}.mandate li{margin:.3rem 0}
.steps{counter-reset:s;list-style:none;margin:0;padding:0}
.steps li{counter-increment:s;display:grid;grid-template-columns:3rem 1fr;gap:.75rem;padding:.6rem 0;border-bottom:1px solid var(--rule)}
.steps li::before{content:"\\00A7 " counter(s);font:700 1rem Georgia,serif;color:var(--seal)}
.steps h3{margin:0;font-size:1.05rem}.steps p{margin:.15rem 0 0;grid-column:2}
.steps li>*{grid-column:2}
.api{margin:0}
.api div{display:grid;grid-template-columns:8rem 1fr;gap:.75rem;padding:.5rem 0;border-bottom:1px dotted var(--rule)}
.api dt{font-weight:700}.api dd{margin:0}
@media (max-width:30rem){.api div{grid-template-columns:1fr;gap:0}}
footer{border-top:3px double var(--rule);padding:2rem 0 3rem;font-size:.95rem}
footer nav{display:flex;flex-wrap:wrap;gap:.25rem 1.25rem}
footer nav a{min-height:44px;display:inline-flex;align-items:center}
"""


def d3():
    n = 3
    rows = "".join(f"<tr><td>{r}</td><td><strong>{w}</strong>{'<br><code>' + a + '</code>' if a else ''}</td><td>{d}</td></tr>" for r, w, a, d in ROLES)
    led = []
    for t, h, p, link in LOG:
        extra = f' <a href="{link[0]}">{link[1]}</a>' if link else ""
        led.append(f'<li><time>{t}</time><div><h3>{h}</h3><p>{p}{extra}</p><span class="sig">Signed in the repository\'s history</span></div></li>')
    stats = ", ".join(f"{a} {b}" for a, b in STATS)
    return head(n, "Logbook", DESIGNS[2][2], CSS3) + f"""<div class="wrap">
{chrome(n)}
<header class="mast"><a class="brand" href="/">Instagram</a>{owner_links("own")}</header>
</div>
<main id="main">
<div class="wrap">
<div class="cover">
<p class="vol">The logbook of instagram.platform.sovereignweb.site</p>
<h1>{H1}</h1>
<p class="lede">{LEDE}</p>
<a class="open" href="#log">Open the log</a>
<p class="small">{ACCOUNT[0]}: {stats}. {UNOFFICIAL}</p>
</div>
<div class="page" id="agent">
<h2>The keeper</h2>
<p class="sub">{AGENT_INTRO}</p>
{identity_dl()}
<h2 class="vh">Its mandate</h2>
{mandate()}
</div>
<div class="page" id="roles">
<h2>The crew list</h2>
<p class="sub">{ROLES_INTRO}</p>
<div class="tablebox" tabindex="0" role="region" aria-label="The crew list"><table class="crew"><thead><tr><th scope="col">Role</th><th scope="col">Who</th><th scope="col">What it has done</th></tr></thead><tbody>{rows}</tbody></table></div>
</div>
<div class="page" id="log">
<h2>The log</h2>
<p class="sub">{LOG_INTRO}</p>
<ol class="ledger">{''.join(led)}</ol>
</div>
<div class="page" id="watch">
<h2>The posts, as entered</h2>
<p class="sub">{WATCH_INTRO}</p>
<div class="entries">{''.join(post_fig(p) for p in POSTS)}</div>
</div>
<div class="page" id="how">
<h2>Standing orders: five steps, one of them human</h2>
<p class="sub">{STEPS_INTRO}</p>
{steps_ol()}
</div>
<div class="page" id="api">
<h2>Regulations: Instagram's official API, in brief</h2>
<p class="sub">{API_INTRO}</p>
{api_dl()}
</div>
</div>
</main>
<div class="wrap">{footer()}</div>"""


# ---------------------------------------------------------------- 4. On Air (dark first, way out there)
CSS4 = """
:root{--bg:#07090d;--fg:#f2f4f8;--muted:#b4bccb;--link:#7fe0ff;--focus:#7fe0ff;--ctl:#7a8597;--hover:#151b26;--panel:#10151f;--bezel:#1b2230;--line:#2a3344;--tally:#ff4d4d;--prev:#3ee08f;--amber:#ffc24d}
@media (prefers-color-scheme:light){:root{--bg:#e9ecf1;--fg:#0a0d12;--muted:#46505f;--link:#00557a;--focus:#00557a;--ctl:#6a7486;--hover:#d9dee7;--panel:#ffffff;--bezel:#cfd5df;--line:#bcc4d1;--tally:#b3141b;--prev:#0f6b3d;--amber:#7a4e00}}
.wrap{max-width:86rem;margin:0 auto;padding:0 1rem}
.mast{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.5rem 1rem;padding:.6rem 0}
.brand{font:800 1.1rem/1 ui-monospace,Menlo,Consolas,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center;gap:.6rem}
.brand .dot{width:.8rem;height:.8rem;border-radius:50%;background:var(--tally);box-shadow:0 0 .8rem var(--tally)}
.own{display:flex;flex-wrap:wrap;gap:.25rem 1rem;font-size:.95rem}
.own a{color:var(--fg);min-height:44px;display:inline-flex;align-items:center}
.gallery{display:grid;gap:1rem;grid-template-columns:1fr;padding:1rem 0 2rem}
@media (min-width:60rem){.gallery{grid-template-columns:1.6fr 1fr}}
.pgm{background:var(--panel);border:2px solid var(--tally);border-radius:.6rem;padding:1rem;position:relative}
.pgm .tag,.pvw .tag{display:inline-flex;gap:.5rem;align-items:center;font:800 .85rem ui-monospace,Menlo,Consolas,monospace;letter-spacing:.14em;text-transform:uppercase;padding:.25rem .6rem;border-radius:.3rem}
.pgm .tag{background:var(--tally);color:#1a0000}
@media (prefers-color-scheme:light){.pgm .tag{color:#fff}}
.pgm-grid{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,17rem),1fr));align-items:center;margin-top:1rem}
.pgm img{border-radius:.3rem;aspect-ratio:4/5;object-fit:cover;width:100%}
.eyebrow{font:700 .85rem ui-monospace,Menlo,Consolas,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 .5rem}
h1{font-size:clamp(2.1rem,5.6vw,3.6rem);line-height:1.04;margin:0 0 1rem;letter-spacing:-.02em}
h2{font-size:clamp(1.45rem,3.4vw,2rem);margin:0 0 .5rem;line-height:1.15}
h3{font-size:1.05rem;margin:0 0 .25rem}
.lede{font-size:1.08rem;margin:0}
.small{color:var(--muted);font-size:.95rem}
.onair{margin-top:.75rem;padding:.75rem;border-left:4px solid var(--tally);background:var(--bezel)}
.onair p{margin:.2rem 0}
.pvws{display:grid;gap:1rem}
.pvw{background:var(--panel);border:2px solid var(--prev);border-radius:.6rem;padding:1rem}
.pvw .tag{background:var(--prev);color:#04140b}
@media (prefers-color-scheme:light){.pvw .tag{color:#fff}}
.pvw .row{display:grid;grid-template-columns:6.5rem 1fr;gap:.9rem;margin-top:.75rem;align-items:start}
.pvw img{aspect-ratio:9/16;object-fit:cover;width:100%;border-radius:.3rem}
.pvw p{margin:.25rem 0;font-size:.95rem}
.meters{display:flex;flex-wrap:wrap;gap:.5rem;margin:.75rem 0 0}
.meters div{font:700 .9rem ui-monospace,Menlo,Consolas,monospace;border:1px solid var(--line);border-radius:.3rem;padding:.35rem .6rem;background:var(--bezel)}
.meters b{color:var(--amber);font-size:1.2rem;margin-right:.3rem}
.cta{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:.55rem 1rem;border-radius:.4rem;font-weight:700;text-decoration:none;border:2px solid var(--fg);color:var(--fg)}
.btn.primary{background:var(--fg);color:var(--bg)}
section{padding:clamp(2.2rem,6vw,4rem) 0;border-top:1px solid var(--line)}
.intro{max-width:44rem}
.rundown{list-style:none;margin:1.25rem 0 0;padding:0;counter-reset:r;display:grid;gap:.5rem}
.rundown li{counter-increment:r;display:grid;grid-template-columns:3rem 1fr;gap:.75rem;background:var(--panel);border:1px solid var(--line);border-radius:.5rem;padding:.75rem}
.rundown li::before{content:counter(r,decimal-leading-zero);font:800 1.2rem ui-monospace,Menlo,Consolas,monospace;color:var(--amber)}
.rundown li:nth-child(3){border:2px solid var(--tally)}
.rundown li:nth-child(3)::before{color:var(--tally)}
.rundown p{margin:.15rem 0 0}
.rundown li>*{grid-column:2}
.credits{list-style:none;margin:1.25rem 0 0;padding:0;display:grid;gap:1px;background:var(--line);border:1px solid var(--line);grid-template-columns:repeat(auto-fit,minmax(min(100%,18rem),1fr))}
.credits li{background:var(--panel);padding:1rem}
.credits .role{margin:0;font:800 .85rem ui-monospace,Menlo,Consolas,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--amber)}
.credits .agent{margin:0;color:var(--muted);font-size:.9rem}
.credits p{margin:.3rem 0}
.split{display:grid;gap:1.5rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,22rem),1fr))}
.id{margin:0;background:var(--panel);border:1px solid var(--line);border-radius:.5rem;padding:.4rem 1rem}
.id div{display:grid;grid-template-columns:8rem 1fr;gap:.75rem;padding:.5rem 0;border-bottom:1px solid var(--line)}
.id div:last-child{border:0}
.id dt{font:700 .85rem ui-monospace,Menlo,Consolas,monospace;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}.id dd{margin:0}
@media (max-width:30rem){.id div{grid-template-columns:1fr;gap:0}}
.mandate{display:grid;gap:1rem}
.mandate>div{background:var(--panel);border:1px solid var(--line);border-radius:.5rem;padding:1rem}
.mandate>div:last-child{border-color:var(--tally)}
.mandate ul{margin:.3rem 0;padding-left:1.1rem}.mandate li{margin:.3rem 0}
.log{list-style:none;margin:1.25rem 0 0;padding:0;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.95rem;background:var(--panel);border:1px solid var(--line);border-radius:.5rem}
.log li{display:grid;grid-template-columns:8.5rem 1fr;gap:1rem;padding:.7rem 1rem;border-bottom:1px solid var(--line)}
.log li:last-child{border:0}
.log time{color:var(--prev)}
.log h3{font-size:1rem;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.log p{margin:.2rem 0 0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
@media (max-width:30rem){.log li{grid-template-columns:1fr;gap:.2rem}}
.api{display:grid;gap:.75rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,17rem),1fr));margin:1.25rem 0 0}
.api div{background:var(--panel);border:1px solid var(--line);border-radius:.5rem;padding:.9rem}
.api dt{font:800 .85rem ui-monospace,Menlo,Consolas,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--amber)}.api dd{margin:.25rem 0 0}
footer{border-top:1px solid var(--line);padding:2rem 0 3rem;font-size:.95rem}
footer nav{display:flex;flex-wrap:wrap;gap:.25rem 1.25rem}
footer nav a{min-height:44px;display:inline-flex;align-items:center}
@media (prefers-reduced-motion:no-preference){.brand .dot{animation:pulse 2.4s ease-in-out infinite}@keyframes pulse{50%{opacity:.45}}}
"""


def d4():
    n = 4
    live = POSTS[0]
    pv = "".join(
        f'<div class="pvw"><span class="tag">Reel: {p["label"]}</span><div class="row"><img src="{p["img"]}" alt="{p["alt"]}" width="{p["w"]}" height="{p["h"]}"><div><h3>{p["title"]}</h3><p>{p["text"]}</p><p><a href="{p["rec"]}">{p["link"]}<span class="vh">: {p["title"]}</span></a></p></div></div></div>'
        for p in POSTS[1:])
    meters = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in STATS)
    credits = "".join(f'<li><p class="role">{r}</p><h3>{w}</h3>{"<p class=agent><code>" + a + "</code></p>" if a else ""}<p>{d}</p></li>' for r, w, a, d in ROLES)
    rundown = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in STEPS)
    return head(n, "On Air", DESIGNS[3][2], CSS4) + f"""<div class="wrap">
{chrome(n)}
<header class="mast"><a class="brand" href="/"><span class="dot" aria-hidden="true"></span>Instagram</a>{owner_links("own")}</header>
</div>
<main id="main">
<div class="wrap">
<div class="gallery" id="watch">
<div class="pgm">
<span class="tag">Programme: {live["label"]}</span>
<div class="pgm-grid">
<img src="{live["img"]}" alt="{live["alt"]}" width="{live["w"]}" height="{live["h"]}">
<div>
<p class="eyebrow">instagram.platform.sovereignweb.site</p>
<h1>{H1}</h1>
<p class="lede">{LEDE}</p>
<div class="onair"><h2 class="vh">Watch it work</h2><p><strong>{live["title"]}</strong></p><p>{live["text"]}</p><p><a href="{live["rec"]}">{live["link"]}<span class="vh">: {live["title"]}</span></a></p></div>
<div class="meters" role="group" aria-label="{ACCOUNT[0]}">{meters}</div>
<div class="cta"><a class="btn primary" href="#how">How a post goes out</a><a class="btn" href="#agent">Meet the agent</a></div>
</div>
</div>
</div>
<div class="pvws">{pv}<p class="small">{WATCH_INTRO} {UNOFFICIAL}</p></div>
</div>
</div>
<section id="how"><div class="wrap">
<h2>The rundown: five steps, one of them human</h2>
<p class="intro">{STEPS_INTRO}</p>
<ol class="rundown">{rundown}</ol>
</div></section>
<section id="agent"><div class="wrap">
<h2>In the gallery: the Instagram agent</h2>
<p class="intro">{AGENT_INTRO}</p>
<div class="split">{identity_dl()}<div><h3>Its mandate</h3>{mandate()}</div></div>
</div></section>
<section id="roles"><div class="wrap">
<h2>Credits: who does what</h2>
<p class="intro">{ROLES_INTRO}</p>
<ul class="credits">{credits}</ul>
</div></section>
<section id="log"><div class="wrap">
<h2>Transmission log</h2>
<p class="intro">{LOG_INTRO}</p>
{log_items()}
</div></section>
<section id="api"><div class="wrap">
<h2>Technical standards: Instagram's official API, in brief</h2>
<p class="intro">{API_INTRO}</p>
{api_dl()}
</div></section>
</main>
<div class="wrap">{footer()}</div>"""


# ---------------------------------------------------------------- 5. Brief
CSS5 = """
:root{--bg:#ffffff;--fg:#111111;--muted:#4a4a4a;--link:#0b4f8a;--focus:#0b4f8a;--ctl:#767676;--hover:#f0f0f0;--line:#d6d6d6}
@media (prefers-color-scheme:dark){:root{--bg:#121212;--fg:#f1f1f1;--muted:#bdbdbd;--link:#8cc4ff;--focus:#8cc4ff;--ctl:#8a8a8a;--hover:#222;--line:#333}}
.wrap{max-width:42rem;margin:0 auto;padding:0 1rem}
.mast{padding:.5rem 0 0}
.brand{font:700 1.1rem Georgia,"Times New Roman",serif;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.own{display:flex;flex-wrap:wrap;gap:0 1rem;font-size:.95rem}
.own a{min-height:44px;display:inline-flex;align-items:center}
h1,h2{font-family:Georgia,"Times New Roman",serif;line-height:1.15}
h1{font-size:clamp(2rem,6vw,2.8rem);margin:1.5rem 0 1rem}
h2{font-size:1.45rem;margin:2.25rem 0 .5rem;padding-top:1rem;border-top:1px solid var(--line)}
h3{font-size:1.05rem;margin:1rem 0 .2rem}
.small{color:var(--muted);font-size:.95rem}
.id,.api{margin:0}
.id div,.api div{padding:.3rem 0}
.id dt,.api dt{font-weight:700;display:inline}
.id dt::after,.api dt::after{content:": "}
.id dd,.api dd{display:inline;margin:0}
.mandate ul{padding-left:1.2rem}
.roles{padding-left:1.2rem}
.roles li{margin:.5rem 0}
.roles .role,.roles .agent{display:inline;margin:0}
.roles .role::after{content:": "}
.roles h3{display:inline;font-size:1rem}
.roles .agent{color:var(--muted);font-size:.9rem}
.roles .agent::before{content:" ("}.roles .agent::after{content:")"}
.roles li p:last-child{margin:.15rem 0 0}
.plist{padding-left:1.2rem}
.plist li{margin:.4rem 0}
.log{padding-left:1.2rem}
.log li{margin:.4rem 0}
.log time{font-weight:700}
.log time::after{content:", "}
.log h3,.log div,.log p{display:inline;font-size:1rem;margin:0}
.log h3::after{content:". "}
.steps{padding-left:1.4rem}.steps h3{display:inline;font-size:1rem}.steps h3::after{content:": "}.steps p{display:inline}
footer{border-top:1px solid var(--line);margin-top:2.5rem;padding:1rem 0 3rem;font-size:.95rem}
footer nav{display:flex;flex-wrap:wrap;gap:0 1rem}
footer nav a{min-height:44px;display:inline-flex;align-items:center}
@media print{body{font-size:11pt}a{color:inherit}h2{break-after:avoid}}
"""


def d5():
    n = 5
    pl = "".join(f'<li><strong>{p["label"]}: {p["title"]}.</strong> {p["text"]} <a href="{p["rec"]}">Folder record<span class="vh">: {p["title"]}</span></a></li>' for p in POSTS)
    stats = ", ".join(f"{a} {b}" for a, b in STATS)
    return head(n, "Brief", DESIGNS[4][2], CSS5) + f"""<div class="wrap">
{chrome(n)}
<header class="mast"><a class="brand" href="/">Instagram</a>{owner_links("own")}</header>
<main id="main">
<h1>{H1}</h1>
<p>{LEDE}</p>
<p class="small">{ACCOUNT[0]} ({ACCOUNT[1]}): {stats}. {UNOFFICIAL}</p>
<h2 id="watch">Watch it work</h2>
<p>{WATCH_INTRO}</p>
<ul class="plist">{pl}</ul>
<h2 id="agent">The agent</h2>
<p>{AGENT_INTRO}</p>
{identity_dl()}
<h3>Its mandate</h3>
{mandate()}
<h2 id="roles">Who does what</h2>
<p>{ROLES_INTRO}</p>
{roles_list()}
<h2 id="how">How a post goes out: five steps, one of them human</h2>
<p>{STEPS_INTRO}</p>
{steps_ol()}
<h2 id="log">The log</h2>
<p>{LOG_INTRO}</p>
{log_items()}
<h2 id="api">Instagram's official API, in brief</h2>
<p>{API_INTRO}</p>
{api_dl()}
</main>
{footer()}
</div>""".replace("</body>\n</html>\n</div>", "</div>\n</body>\n</html>\n")


# ---------------------------------------------------------------- index: all five side by side
CSSI = """
:root{--bg:#f6f4ef;--fg:#16202e;--muted:#4d5866;--link:#7f570e;--focus:#7f570e;--ctl:#7b8592;--hover:#ebe7de;--card:#fff;--line:#ddd7cb}
@media (prefers-color-scheme:dark){:root{--bg:#0d1420;--fg:#ecebe6;--muted:#aeb8c6;--link:#f2b84b;--focus:#f2b84b;--ctl:#7d8ca3;--hover:#1a2638;--card:#152033;--line:#273550}}
.wrap{max-width:76rem;margin:0 auto;padding:0 1rem}
.mast{padding:.5rem 0}
.brand{font-weight:800;font-size:1.15rem;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
h1{font:700 clamp(2rem,5.5vw,3.2rem)/1.1 Georgia,"Iowan Old Style","Times New Roman",serif;margin:1rem 0 .75rem}
.lede{max-width:44rem}
.cards{list-style:none;margin:1.5rem 0 3rem;padding:0;display:grid;gap:1.25rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,20rem),1fr))}
.cards li{background:var(--card);border:1px solid var(--line);border-radius:.6rem;overflow:hidden}
.cards img{aspect-ratio:16/10;object-fit:cover;object-position:top;width:100%;border-bottom:1px solid var(--line)}
.cards .body{padding:1rem}
.cards h2{font-size:1.2rem;margin:0 0 .3rem}
.cards p{margin:.3rem 0}
.cards .pick{font-weight:700}
footer{border-top:1px solid var(--line);padding:2rem 0 3rem;font-size:.95rem}
footer nav{display:flex;flex-wrap:wrap;gap:.25rem 1.25rem}
footer nav a{min-height:44px;display:inline-flex;align-items:center}
"""


def index(recommend):
    cards = "".join(
        f'<li><img src="/designs/{i}/shot-1366.webp" alt="Design {i}, {nm}, at desktop width" width="1366" height="854" loading="lazy"><div class="body"><h2><a href="/designs/{i}/">{i}. {nm}</a></h2><p>{idea}</p>{"<p class=pick>Recommended by the designer.</p>" if i == recommend else ""}</div></li>'
        for i, nm, idea in DESIGNS)
    h = head(0, "", "", CSSI).replace(", design 0 of Instagram", "").replace("<title></title>", "<title>Five designs, Instagram</title>")
    h = h.replace('content="Design 0 of instagram.platform.sovereignweb.site, :  Unofficial', 'content="Five designs of instagram.platform.sovereignweb.site, the same facts in five ideas, side by side. Unofficial')
    h = h.replace("/designs/0/", "/designs/").replace('content=""', 'content="Five designs, Instagram"')
    return h + f"""<div class="wrap">
{chrome(0)}
<header class="mast"><a class="brand" href="/">Instagram</a></header>
<main id="main">
<h1>Five designs of this site</h1>
<p class="lede">The same facts, in five ideas from the Instagram agent's own world. The owner picks one; the keeper makes it the site. Until then, the site stays as it is.</p>
<ul class="cards">{cards}</ul>
</main>
{footer()}
</div>""".replace("</body>\n</html>\n</div>", "</div>\n</body>\n</html>\n")


def fix(s):
    return s.replace("</body>\n</html>\n", "").rstrip() + "\n</body>\n</html>\n"


if __name__ == "__main__":
    rec = int(os.environ.get("RECOMMEND", "2"))
    pages = {1: d1, 2: d2, 3: d3, 4: d4, 5: d5}
    for i, f in pages.items():
        os.makedirs(f"{OUT}/{i}", exist_ok=True)
        open(f"{OUT}/{i}/index.html", "w").write(fix(f()))
    open(f"{OUT}/index.html", "w").write(fix(index(rec)))
    print("built", OUT)
