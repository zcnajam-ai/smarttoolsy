# SmartToolsy — free online tools site

20 browser-based tools, 3 guide articles, and every page Google AdSense reviewers look for
(About, Contact, Privacy Policy, Terms, Disclaimer, sitemap, robots.txt).
Plain static HTML/CSS/JS — no database, no server, free to host on Vercel.

## Folder layout

| Path | What it is |
|---|---|
| `src/build.py` | Build script. **Edit the `CONFIG` block at the top** (site name, domain, email, AdSense ID). |
| `src/tools_a.py`, `src/tools_b.py` | Each tool's form and its article content (how-to, formula, FAQ). |
| `src/articles.py` | Blog/guide articles. Add new ones here. |
| `static/assets/` | CSS, shared JS, all tool logic (`tools.js`) and the built-in QR encoder (`qr.js`). |
| `docs/` | The finished website, served by GitHub Pages. Always rebuild and commit it after changes. |

Rebuild after any change:

```
python3 src/build.py
```

## Hosting (Vercel, connected to this GitHub repo)

- Vercel project `smarttoolsy` deploys every push to `main`. `vercel.json` tells it to serve the prebuilt `docs/` folder.
- Domain `smarttoolsy.tech` is registered in Vercel, so no DNS records are needed:
  Vercel → smarttoolsy project → Settings → Domains → add `smarttoolsy.tech` (and `www.smarttoolsy.tech` redirecting to it).
- Do not also enable GitHub Pages or add GitHub A records; one host only.
- Create the email inbox you set as `CONTACT_EMAIL` (Zoho Mail free plan, or Google Workspace).

After any change: `python3 src/build.py`, then commit and push (including `docs/`).

## Google Search Console (do this on day 1)

1. Add the domain in https://search.google.com/search-console and verify via DNS.
2. Submit `https://YOURDOMAIN/sitemap.xml`.
3. Use "URL Inspection → Request indexing" for the homepage and a few tools.

## AdSense approval checklist

- [ ] Site live on your own domain (not a vercel.app subdomain) with HTTPS
- [ ] All pages indexed in Search Console, no errors
- [ ] Contact email works
- [ ] **At least 15–20 original articles** published (3 are included — add 1–2 per week).
      Tool-only sites are frequently rejected as "low value content"; articles fix that.
- [ ] Some organic traffic starting (even 20–50 visits/day helps)
- [ ] Apply at https://adsense.google.com → add site → paste the `ca-pub-…` ID into
      `CONFIG["ADSENSE_CLIENT"]`, rebuild and redeploy. This adds the AdSense script,
      the verification meta tag and `ads.txt` automatically.
- [ ] In AdSense → Privacy & messaging, turn on the **European regulations (GDPR) consent
      message** (Google's own certified CMP). This is required to serve ads to EEA/UK users
      and the Privacy Policy already describes it.
- [ ] Turn on **Auto ads** after approval.

## Growing traffic (what actually moves AdSense earnings)

- Earnings depend on visitors from high-paying countries (US, UK, Canada, Australia).
- Each new tool = a new page that can rank. Pick tools people search for with low competition
  (check Google autocomplete, "People also ask", and Search Console queries).
- Write one guide per tool explaining a real problem it solves, and link the two together.
- Share tools where people ask for them (Reddit answers, Quora, Pinterest pins for calculators).
