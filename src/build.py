#!/usr/bin/env python3
"""Build the SmartToolsy static site into ../dist.

Edit CONFIG below, then run:  python3 src/build.py
"""
import html, json, os, re, shutil, sys
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))
from tools_a import TOOLS_A
from tools_b import TOOLS_B
from articles import ARTICLES

# ------------------------------------------------------------------ CONFIG
CONFIG = dict(
    SITE_NAME="SmartToolsy",
    SITE_URL="https://smarttoolsy.tech",      # no trailing slash
    CONTACT_EMAIL="contact@smarttoolsy.tech",  # create this inbox before applying to AdSense
    OWNER="SmartToolsy",                       # your name or business name for the About/Terms pages
    COUNTRY="Pakistan",                        # governing-law country in Terms
    ADSENSE_CLIENT="",                         # e.g. "ca-pub-1234567890123456" — paste after AdSense gives it to you
    GA_ID="",                                  # optional Google Analytics 4 ID, e.g. "G-XXXXXXX"
    UPDATED=date.today().isoformat(),
)
# --------------------------------------------------------------------------

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "docs")   # GitHub Pages serves this folder (Settings → Pages → main /docs)
SLASH_RE = re.compile(r'((?:href|content)="(?:' + re.escape(CONFIG["SITE_URL"]) + r')?)(/[A-Za-z0-9\-/]*[A-Za-z0-9])"')


def slashify(text):
    """GitHub Pages serves folders at /path/ — link there directly to avoid a redirect hop."""
    return SLASH_RE.sub(lambda m: m.group(1) + m.group(2) + '/"', text)
TOOLS = TOOLS_A + TOOLS_B
BY_SLUG = {t["slug"]: t for t in TOOLS}
CATS = [("text", "Text tools"), ("calc", "Calculators"), ("convert", "Converters"),
        ("generate", "Generators"), ("dev", "Developer tools"), ("image", "Image tools")]
CAT_NAME = dict(CATS)
C = CONFIG
e = html.escape

LOGO = """<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#2F5BEA"/><path d="M9 21.5c1.4 1.3 3.3 2 5.4 2 3 0 5-1.5 5-3.8 0-2.2-1.6-3.1-4.4-3.8-2.2-.5-3-1-3-2 0-1 .9-1.6 2.4-1.6 1.4 0 2.6.5 3.6 1.3" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><circle cx="23.5" cy="9" r="3" fill="#F2B33D"/></svg>"""
FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#2F5BEA"/><path d="M9 21.5c1.4 1.3 3.3 2 5.4 2 3 0 5-1.5 5-3.8 0-2.2-1.6-3.1-4.4-3.8-2.2-.5-3-1-3-2 0-1 .9-1.6 2.4-1.6 1.4 0 2.6.5 3.6 1.3" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><circle cx="23.5" cy="9" r="3" fill="#F2B33D"/></svg>"""


def head(title, desc, path, extra_ld=None, noindex=False):
    url = C["SITE_URL"] + path
    ads = ""
    if C["ADSENSE_CLIENT"]:
        ads = (f'<meta name="google-adsense-account" content="{e(C["ADSENSE_CLIENT"])}">\n'
               f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={e(C["ADSENSE_CLIENT"])}" crossorigin="anonymous"></script>')
    ga = ""
    if C["GA_ID"]:
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={e(C["GA_ID"])}"></script>'
              f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{e(C['GA_ID'])}');</script>")
    ld = ""
    for block in (extra_ld or []):
        ld += '<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False) + "</script>\n"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(C['SITE_NAME'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#2F5BEA">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Bricolage+Grotesque:opsz,wght@12..96,600..800&display=swap">
<link rel="stylesheet" href="/assets/app.css">
{ads}
{ga}
{ld}</head>"""


def header(active=""):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="logo" href="/">{LOGO}<span>{e(C['SITE_NAME'])}</span></a>
<nav class="nav" aria-label="Main">{a('/', 'All tools', 'home')}{a('/blog', 'Guides', 'blog')}{a('/about', 'About', 'about')}{a('/contact', 'Contact', 'contact')}</nav>
<button class="theme-btn" type="button" aria-label="Switch light or dark theme"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor"/></svg></button>
</div></header>"""


def footer():
    y = date.today().year
    return f"""<footer class="site-footer"><div class="wrap foot-grid">
<p style="margin:0">© {y} {e(C['SITE_NAME'])}. Free online tools that run in your browser.</p>
<nav class="foot-links" aria-label="Site information">
<a href="/about">About</a><a href="/contact">Contact</a><a href="/privacy-policy">Privacy Policy</a><a href="/terms">Terms of Use</a><a href="/disclaimer">Disclaimer</a><a href="/sitemap.xml">Sitemap</a>
</nav></div></footer>
<script src="/assets/site.js"></script>"""


def write(path, content):
    full = os.path.join(DIST, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(DIST, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(slashify(content))


def org_ld():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": C["SITE_NAME"], "url": C["SITE_URL"] + "/"}


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": C["SITE_URL"] + p} for i, (n, p) in enumerate(items)]}


# ------------------------------------------------------------------ pages
def build_home():
    chips = '<button class="chip" type="button" data-cat="all" aria-pressed="true">All</button>' + "".join(
        f'<button class="chip" type="button" data-cat="{k}" aria-pressed="false">{v}</button>' for k, v in CATS)
    groups = ""
    for k, label in CATS:
        items = [t for t in TOOLS if t["cat"] == k]
        if not items:
            continue
        lis = "".join(
            f'<li data-cat="{t["cat"]}" data-search="{e((t["name"] + " " + t["short"] + " " + t["slug"].replace("-", " ") + " " + label).lower())}">'
            f'<a class="tool-link" href="/{t["slug"]}"><span class="tool-ico" aria-hidden="true">{e(t["ico"])}</span>'
            f'<span><span class="tool-name">{e(t["name"])}</span><span class="tool-desc">{e(t["short"])}</span></span></a></li>'
            for t in items)
        groups += f'<section class="tool-group" aria-labelledby="g-{k}"><h2 id="g-{k}">{label}</h2><ul class="tool-list">{lis}</ul></section>'
    title = f"{C['SITE_NAME']} – Free Online Tools: Calculators, Converters & Generators"
    desc = f"{len(TOOLS)} free online tools that run in your browser: word counter, QR code generator, image compressor, loan and BMI calculators, unit converter and more. No sign-up."
    page = head(title, desc, "/", [org_ld()]) + f"""
<body>
{header('home')}
<main id="main">
<section class="finder"><div class="wrap">
<h1>Free tools for everyday jobs</h1>
<p class="finder-lede">Count words, compress a photo, make a QR code or work out a loan payment. Every tool runs in your browser, so nothing you type is uploaded.</p>
<div class="finder-box" role="search">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
<input id="finder" type="search" placeholder="What do you need to do? Try “qr”, “age” or “compress”" aria-label="Search tools" autocomplete="off">
</div>
<div class="chips" role="group" aria-label="Filter by category">{chips}</div>
<p class="count-note" id="count-note" aria-live="polite"></p>
</div></section>
<div class="wrap tool-groups">{groups}
<p class="empty" id="empty" hidden>No tool matches that yet. Try a shorter word, or <a href="/contact">suggest a tool</a> you would like us to build.</p>
</div>
<section class="why"><div class="wrap why-grid">
<div><h3>Private by design</h3><p>Your text, images and numbers stay on your device. The tools work with JavaScript in your browser and never send your input to a server.</p></div>
<div><h3>No account, no limits</h3><p>Every tool is free to use as often as you like, with no sign-up, watermarks or daily caps.</p></div>
<div><h3>Explained, not just answered</h3><p>Each tool page shows the formula or method behind the result, so you can check the numbers and learn how they work.</p></div>
</div></section>
<section class="wrap" style="padding:40px 16px 56px">
<h2 style="margin-top:0">Latest guides</h2>
<ul>{''.join(f'<li><a href="/blog/{a["slug"]}">{e(a["title"])}</a></li>' for a in ARTICLES)}</ul>
</section>
</main>
{footer()}
</body></html>"""
    write("/", page)


def related_for(t):
    same = [x for x in TOOLS if x["cat"] == t["cat"] and x["slug"] != t["slug"]]
    other = [x for x in TOOLS if x["cat"] != t["cat"]]
    return (same + other)[:7]


def build_tool(t):
    path = "/" + t["slug"]
    ld = [crumbs_ld([("Home", "/"), (CAT_NAME[t["cat"]], "/"), (t["name"], path)]),
          {"@context": "https://schema.org", "@type": "WebApplication", "name": t["name"], "url": C["SITE_URL"] + path,
           "description": t["desc"], "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any (web browser)",
           "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}]
    rel = "".join(f'<li><a href="/{x["slug"]}">{e(x["name"])}</a></li>' for x in related_for(t))
    guides = [a for a in ARTICLES if t["slug"] in a["tools"]]
    guide_html = ""
    if guides:
        guide_html = '<h2 style="margin-top:24px">Related guides</h2><ul>' + "".join(
            f'<li><a href="/blog/{a["slug"]}">{e(a["title"])}</a></li>' for a in guides) + "</ul>"
    extra_js = '<script src="/assets/qr.js"></script>' if t["slug"] == "qr-code-generator" else ""
    page = head(t["title"], t["desc"], path, ld) + f"""
<body data-tool="{t['slug']}">
{header()}
<main id="main" class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> › {CAT_NAME[t['cat']]} › <span>{e(t['name'])}</span></nav>
<div class="tool-head"><h1>{e(t['name'])}</h1><p>{e(t['short'])}</p></div>
<div class="layout">
<div>
<section class="panel" aria-label="{e(t['name'])}">{t['ui']}</section>
<!-- AD SLOT: in-content. Auto ads place ads automatically once AdSense is approved. -->
<article class="article">{t['content']}</article>
</div>
<aside class="side" aria-label="More tools"><h2>More tools</h2><ul>{rel}</ul>{guide_html}</aside>
</div>
</main>
{footer()}
{extra_js}<script src="/assets/tools.js"></script>
</body></html>"""
    write(path, page)


def plain_page(path, title, desc, h1, body, active=""):
    page = head(title, desc, path, [crumbs_ld([("Home", "/"), (h1, path)])]) + f"""
<body>
{header(active)}
<main id="main" class="wrap"><div class="page article" style="margin-top:0">
<h1>{e(h1)}</h1>
{body}
</div></main>
{footer()}
</body></html>"""
    write(path, page)


def build_static_pages():
    n = C["SITE_NAME"]; mail = C["CONTACT_EMAIL"]; upd = C["UPDATED"]
    plain_page("/about", f"About {n}", f"About {n}: who we are, why we build free browser-based tools and how we keep them accurate.", f"About {n}", f"""
<p>{n} is a collection of free online tools for the small jobs that come up every day: counting the words in an essay, converting a recipe from cups to millilitres, checking a loan payment, making a QR code for a shop window or shrinking a photo before emailing it.</p>
<h2>Why we built it</h2>
<p>Many tool websites are slow, cluttered or ask you to upload files and create an account for a ten-second task. We wanted the opposite: pages that load fast, do one job well and respect your privacy. That is why every tool on {n} runs in your browser. Your text, images and numbers are processed on your own device and are not sent to us.</p>
<h2>How we keep tools accurate</h2>
<p>Each calculator uses standard, published formulas, such as the World Health Organization BMI categories, the standard amortization formula for loans and exact international unit definitions. Every tool page explains its method so you can check the result yourself. We test tools against worked examples before publishing them and fix any issue reported to us.</p>
<h2>Who runs {n}</h2>
<p>{n} is an independent website run by {e(C['OWNER'])}, a small team of web developers and designers based in {e(C['COUNTRY'])}. We build and maintain the tools and write the guides ourselves.</p>
<h2>Suggest a tool</h2>
<p>We add new tools based on what visitors ask for. If there is a tool you would find useful, or you have spotted a mistake, please <a href="/contact">get in touch</a>.</p>
""", "about")

    plain_page("/contact", f"Contact {n}", f"Contact {n} with questions, tool suggestions, bug reports or partnership enquiries.", "Contact us", f"""
<p>We read every message. Whether you have found a bug, want to suggest a new tool or have a business question, email us and we will usually reply within two working days.</p>
<p class="big" style="font-size:1.4rem"><a href="mailto:{e(mail)}">{e(mail)}</a></p>
<h2>Helpful details to include</h2>
<ul>
<li><strong>Bug reports:</strong> the tool’s name, what you entered, what you expected and what happened, plus your browser and device.</li>
<li><strong>Tool suggestions:</strong> what you want to do and how you do it today.</li>
<li><strong>Privacy requests:</strong> see our <a href="/privacy-policy">Privacy Policy</a> for what data we hold and how to ask about it.</li>
</ul>
""", "contact")

    plain_page("/privacy-policy", f"Privacy Policy – {n}", f"How {n} handles data, cookies, Google AdSense advertising and analytics.", "Privacy Policy", f"""
<p class="updated">Last updated: {upd}</p>
<p>This Privacy Policy explains what information {n} (“we”, “us”) collects when you visit {e(C['SITE_URL'])} (the “Site”), how it is used, and the choices you have.</p>
<h2>Information you enter into tools</h2>
<p>Our tools run in your web browser. Text, numbers, files and images you enter into a tool are processed on your device and are not sent to or stored on our servers. When you close or reload the page, that input is gone. A few preferences, such as light or dark theme, may be saved in your browser’s local storage so the Site remembers them; you can clear this at any time through your browser settings.</p>
<h2>Information collected automatically</h2>
<p>Like most websites, our hosting provider automatically records basic technical information when you request a page, such as your IP address, browser type, device type, the page requested and the date and time. This is used to deliver the Site, keep it secure and understand overall traffic. We may use privacy-friendly analytics or Google Analytics to see which pages are popular; this data is aggregated and we do not use it to identify you.</p>
<h2>Cookies and advertising</h2>
<p>We use Google AdSense to show advertisements, which helps keep the tools free. Google and its partners use cookies and similar technologies to serve and measure ads.</p>
<ul>
<li>Third-party vendors, including Google, use cookies to serve ads based on a user’s prior visits to this website or other websites.</li>
<li>Google’s use of advertising cookies enables it and its partners to serve ads to you based on your visit to this Site and/or other sites on the Internet.</li>
<li>You may opt out of personalized advertising by visiting <a href="https://adssettings.google.com" rel="nofollow">Google Ads Settings</a>. You can also opt out of some third-party vendors’ use of cookies for personalized advertising by visiting <a href="https://www.aboutads.info/choices/" rel="nofollow">www.aboutads.info</a>.</li>
<li>To learn more about how Google uses data, see <a href="https://policies.google.com/technologies/partner-sites" rel="nofollow">How Google uses information from sites or apps that use its services</a>.</li>
</ul>
<p>Visitors from the European Economic Area, the United Kingdom and Switzerland are shown a consent message so they can choose whether to allow personalized ads and cookies. You can change your choice at any time using the privacy settings link shown by that message.</p>
<h2>Your rights</h2>
<p>Depending on where you live, you may have the right to access, correct or delete personal data held about you, to object to processing, and to withdraw consent. Because our tools do not collect what you type, we usually hold very little information about individual visitors. Residents of California have rights under the CCPA, including the right to know what personal information is collected and to opt out of its “sale” or “sharing” for targeted advertising, which you can do through the ad settings links above. To make a request, email <a href="mailto:{e(mail)}">{e(mail)}</a>.</p>
<h2>Children</h2>
<p>The Site is intended for a general audience and is not directed at children under 13. We do not knowingly collect personal information from children.</p>
<h2>Links to other sites</h2>
<p>Our pages may link to other websites. We are not responsible for their content or privacy practices.</p>
<h2>Changes to this policy</h2>
<p>We may update this policy from time to time. The “Last updated” date at the top shows when it last changed.</p>
<h2>Contact</h2>
<p>Questions about this policy can be sent to <a href="mailto:{e(mail)}">{e(mail)}</a>.</p>
""")

    plain_page("/terms", f"Terms of Use – {n}", f"The terms that apply when you use {n} and its free online tools.", "Terms of Use", f"""
<p class="updated">Last updated: {upd}</p>
<p>By using {e(C['SITE_URL'])} (the “Site”) you agree to these terms. If you do not agree, please do not use the Site.</p>
<h2>Use of the tools</h2>
<p>The tools are provided free of charge for personal and commercial use. You may use the results, such as QR codes, compressed images and generated text, for any lawful purpose. You may not attempt to disrupt the Site, scrape it at a volume that affects other users, or use it for anything unlawful.</p>
<h2>No warranty</h2>
<p>We work hard to keep the tools accurate, but they are provided “as is” without warranties of any kind. Results are for general information and should be checked before you rely on them for financial, medical, legal or other important decisions. See our <a href="/disclaimer">Disclaimer</a>.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, {e(C['OWNER'])} is not liable for any loss or damage arising from your use of the Site or reliance on its results.</p>
<h2>Intellectual property</h2>
<p>The Site’s design, text and code belong to {e(C['OWNER'])}. You may link to any page. Content you create with the tools belongs to you.</p>
<h2>Advertising and third parties</h2>
<p>The Site shows advertising from Google AdSense and may link to third-party websites. We do not control and are not responsible for third-party content or offers.</p>
<h2>Changes</h2>
<p>We may change these terms or the tools at any time. Continued use of the Site means you accept the current terms.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of {e(C['COUNTRY'])}.</p>
<h2>Contact</h2>
<p>Email <a href="mailto:{e(mail)}">{e(mail)}</a> with any questions.</p>
""")

    plain_page("/disclaimer", f"Disclaimer – {n}", f"Important information about the accuracy and intended use of {n} tools.", "Disclaimer", f"""
<p class="updated">Last updated: {upd}</p>
<p>The tools and articles on {n} are provided for general information and convenience. While we use standard formulas and test our tools carefully, we cannot guarantee that every result is complete, accurate or suitable for your situation.</p>
<h2>Financial results</h2>
<p>Loan, percentage and discount calculators give estimates. Actual figures from banks, lenders and retailers may differ because of fees, rounding, taxes and terms. They are not financial advice.</p>
<h2>Health results</h2>
<p>The BMI calculator is a general screening tool for adults and is not medical advice, diagnosis or treatment. Consult a qualified health professional about your health.</p>
<h2>External links and advertising</h2>
<p>We are not responsible for the content of external websites linked from our pages or for products and services advertised on the Site.</p>
<p>If you find an error, please <a href="/contact">let us know</a> so we can fix it.</p>
""")


def build_blog():
    items = "".join(f'<li style="margin-bottom:18px"><a href="/blog/{a["slug"]}" style="font-weight:700;font-size:1.15rem">{e(a["title"])}</a><br><span style="color:var(--muted)">{e(a["desc"])}</span></li>' for a in ARTICLES)
    plain_page("/blog", f"Guides – {C['SITE_NAME']}", "Practical how-to guides on passwords, images, everyday math and more.", "Guides",
               f'<p>Short, practical guides that go deeper into the jobs our tools help with.</p><ul style="list-style:none;padding:0">{items}</ul>', "blog")
    for a in ARTICLES:
        path = "/blog/" + a["slug"]
        tools = "".join(f'<li><a href="/{s}">{e(BY_SLUG[s]["name"])}</a></li>' for s in a["tools"])
        ld = [crumbs_ld([("Home", "/"), ("Guides", "/blog"), (a["title"], path)]),
              {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
               "datePublished": a["date"], "dateModified": a["date"], "author": {"@type": "Organization", "name": C["SITE_NAME"]},
               "publisher": {"@type": "Organization", "name": C["SITE_NAME"]}, "mainEntityOfPage": C["SITE_URL"] + path}]
        page = head(a["title"], a["desc"], path, ld) + f"""
<body>
{header('blog')}
<main id="main" class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/blog">Guides</a></nav>
<div class="layout" style="margin-top:12px">
<article class="article" style="margin-top:0">
<h1>{e(a['title'])}</h1>
<p class="updated" style="color:var(--muted)">Published {a['date']}</p>
{a['body']}
</article>
<aside class="side" aria-label="Tools in this guide"><h2>Try the tools</h2><ul>{tools}</ul></aside>
</div>
</main>
{footer()}
</body></html>"""
        write(path, page)


def build_misc():
    page = head("Page not found – " + C["SITE_NAME"], "This page could not be found.", "/404", noindex=True) + f"""
<body>{header()}<main id="main" class="wrap"><div class="page"><h1>Page not found</h1>
<p>The page you were looking for has moved or never existed. Find what you need on the <a href="/">tools home page</a>.</p></div></main>{footer()}</body></html>"""
    with open(os.path.join(DIST, "404.html"), "w", encoding="utf-8") as f:
        f.write(slashify(page))
    urls =["/"] + ["/" + t["slug"] for t in TOOLS] + ["/blog"] + ["/blog/" + a["slug"] for a in ARTICLES] + \
           ["/about", "/contact", "/privacy-policy", "/terms", "/disclaimer"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{C['SITE_URL']}{u if u == '/' else u + '/'}</loc><lastmod>{C['UPDATED']}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(DIST, "sitemap.xml"), "w").write(sm)
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {C['SITE_URL']}/sitemap.xml\n")
    pub = C["ADSENSE_CLIENT"].replace("ca-", "") if C["ADSENSE_CLIENT"] else ""
    if pub:
        open(os.path.join(DIST, "ads.txt"), "w").write(f"google.com, {pub}, DIRECT, f08c47fec0942fa0\n")
    open(os.path.join(DIST, "favicon.svg"), "w").write(FAVICON)
    open(os.path.join(DIST, ".nojekyll"), "w").write("")
    open(os.path.join(DIST, "CNAME"), "w").write(C["SITE_URL"].split("://", 1)[1] + "\n")
    return urls


def main():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    shutil.copytree(os.path.join(ROOT, "static"), DIST)
    build_home()
    for t in TOOLS:
        build_tool(t)
    build_static_pages()
    build_blog()
    urls = build_misc()
    print(f"Built {len(urls)} pages into {DIST}")


if __name__ == "__main__":
    main()
