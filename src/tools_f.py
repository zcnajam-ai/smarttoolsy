"""Tool registry part F: SEO and website tools.

These two tools are the exception to the "everything stays in your browser" rule:
the SEO checker sends the URL to our own serverless function (api/seo-check.js),
and the speed test sends it to Google PageSpeed Insights. The page copy says so.
"""

URL_FORM = """<form id="{p}-form" class="url-form" novalidate>
<label for="{p}-url" class="lbl">{label}</label>
<div class="url-row"><input id="{p}-url" type="text" inputmode="url" autocomplete="url" spellcheck="false" placeholder="example.com/page" aria-describedby="{p}-msg"><button class="btn" id="{p}-go" type="submit">{btn}</button></div>
{extra}</form>
<p id="{p}-msg" class="count-note" aria-live="polite"></p>"""

TOOLS_F = [
# ---------------------------------------------------------------- SEO checker
dict(
slug="seo-checker", name="SEO Checker", cat="seo", ico="SE", scripts=["/assets/seo-tools.js"],
title="Free SEO Checker – Analyze Any Web Page and Get an SEO Score",
desc="Check any web page for 40+ SEO factors: title, meta description, headings, keywords, links, images, schema, robots.txt, sitemap, HTTPS and speed. Free, unlimited, no sign-up.",
short="Score any page on 40+ SEO checks, with clear fixes.",
ui=URL_FORM.format(p="seo", label="Web page to check", btn="Check SEO", extra="") + """
<div id="seo-out" class="seo-out" hidden></div>
""",
content="""
<p>The SEO checker reviews a single web page the way a search engine sees it and gives it a score out of 100. It runs more than 40 checks across the page’s title and description, headings, content, links, images, social tags, structured data, crawling rules, security and speed, then tells you in plain English what passed, what needs attention and how to fix it.</p>
<p>It’s free with no daily limit and no account. Check your own pages as often as you like while you fix them, or look at a competitor’s page to see what they do differently.</p>
<h2>How to use the SEO checker</h2>
<ol>
<li>Enter the address of the page you want to check, such as <code>example.com</code> or a full link to a blog post.</li>
<li>Click “Check SEO”. The report is usually ready in a few seconds.</li>
<li>Start with the red <strong>Failed</strong> items, then the amber <strong>Warnings</strong>. Use the filter buttons to show only one type.</li>
<li>Fix the issues on your site, then run the check again to see your score improve.</li>
</ol>
<h2>What the checker looks at</h2>
<ul>
<li><strong>Title, description and keywords:</strong> whether the title and meta description exist, how long they are, and whether the words used most on the page also appear in them. A Google preview shows roughly how the page could look in search results.</li>
<li><strong>Headings and content:</strong> one clear H1, subheadings, and how much readable text the page has.</li>
<li><strong>Links and images:</strong> missing alt text, internal links and links with no text.</li>
<li><strong>Social sharing and structured data:</strong> Open Graph and X (Twitter) card tags, schema.org markup and a favicon.</li>
<li><strong>Crawling and indexing:</strong> the HTTP status, redirects, noindex tags, the canonical tag, robots.txt, the XML sitemap, how missing pages respond, URL format, the page language, and whether the www and non-www versions point to one place.</li>
<li><strong>Security:</strong> HTTPS, the HTTP-to-HTTPS redirect, mixed content, HSTS, exposed server versions, plain-text email addresses and the domain’s SPF record.</li>
<li><strong>Mobile and HTML code:</strong> the mobile viewport, doctype, character encoding and outdated HTML.</li>
<li><strong>Speed:</strong> server response time, HTML size, compression, render-blocking scripts, the number of files and the size of the page structure. For a full speed audit, use the <a href="/page-speed-test">page speed test</a>.</li>
</ul>
<h2>How the SEO score works</h2>
<p>Each check has a weight based on how much it matters. Problems that can stop a page ranking at all, such as a noindex tag, a missing title or an error status, count the most. A pass earns full points, a warning half, and a failure none. The score is the share of available points the page earns.</p>
<p>Treat the score as a to-do list, not a grade. A page can score 100 and still not rank if the content doesn’t match what people are searching for, and a page with a few warnings can rank well if it’s the best answer. Useful, original content and links from other sites matter most.</p>
<h2>What this tool can’t see</h2>
<p>The checker reads the HTML your server sends. Content added later by JavaScript, pages behind a login, and sites that block automated visitors may show fewer details than a browser would. It also checks one page at a time, so run it on your most important pages individually. For data on which searches you already appear in, use Google Search Console.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is the SEO checker really free?</summary><p>Yes. There’s no sign-up, no daily limit and no paid plan. Check as many pages as you like.</p></details>
<details><summary>What happens to the address I enter?</summary><p>Unlike our other tools, this one can’t run entirely in your browser, because browsers don’t allow one website to read another. The address is sent to our server, which downloads that public page, its robots.txt and sitemap, and sends the findings back to you. We don’t save your reports.</p></details>
<details><summary>Why does my page fail the 404 check?</summary><p>The checker requests a made-up address on your site. If it comes back as a normal page (status 200) instead of “not found” (404), search engines may treat empty pages as real ones. Ask your host or developer to return a proper 404 status for missing pages.</p></details>
<details><summary>How long should a title and meta description be?</summary><p>Aim for about 30–60 characters for the title and 70–160 for the description. Google measures width in pixels rather than characters, so these are guides rather than strict limits. Put the most important words first.</p></details>
<details><summary>Can I check a competitor’s website?</summary><p>Yes. Any public page works. Comparing your page with the one ranking above you is a quick way to spot missing headings, thin content or absent structured data.</p></details>
</div>
"""),
# ---------------------------------------------------------------- page speed
dict(
slug="page-speed-test", name="Page Speed Test", cat="seo", ico="PS", scripts=["/assets/seo-tools.js"],
title="Page Speed Test – Check Website Speed & Core Web Vitals Free",
desc="Test any website’s speed on mobile and desktop. See Core Web Vitals (LCP, INP, CLS), performance, SEO and accessibility scores, and what to fix first. Powered by Google PageSpeed Insights.",
short="Mobile and desktop speed scores, Core Web Vitals and fixes.",
ui="""<div data-psi-key="{PSI_KEY}">""" + URL_FORM.format(p="ps", label="Web page to test", btn="Test speed", extra="""<div class="seg" role="group" aria-label="Device"><button type="button" data-strategy="mobile" aria-pressed="true">Mobile</button><button type="button" data-strategy="desktop" aria-pressed="false">Desktop</button></div>""") + """
<div id="ps-out" class="seo-out" hidden></div></div>
""",
content="""
<p>The page speed test loads a web page in a test browser and measures how quickly it appears and becomes usable, on a simulated mid-range phone or on a desktop computer. You get a performance score out of 100, the Core Web Vitals that Google uses as a ranking signal, scores for accessibility, best practices and SEO, and a list of the changes that would speed the page up the most.</p>
<p>The test is run by Google PageSpeed Insights, the same engine (Lighthouse) used in Chrome’s developer tools, so the numbers match what Google reports.</p>
<h2>How to test your page speed</h2>
<ol>
<li>Enter the page address and choose <strong>Mobile</strong> or <strong>Desktop</strong>. Start with mobile: most visitors use phones, and Google ranks pages using their mobile version.</li>
<li>Click “Test speed” and wait 15 to 40 seconds while the page loads in Google’s test browser.</li>
<li>Read the scores, then work through “What to fix first”, which is sorted by the time each fix could save.</li>
</ol>
<h2>Core Web Vitals explained</h2>
<p>Core Web Vitals are three measurements of real-world experience. Google considers a page good when at least 75% of visits meet these targets:</p>
<table>
<thead><tr><th>Metric</th><th>What it measures</th><th>Good</th><th>Poor</th></tr></thead>
<tbody>
<tr><td>Largest Contentful Paint (LCP)</td><td>How long the main content takes to appear</td><td>2.5 s or less</td><td>Over 4 s</td></tr>
<tr><td>Interaction to Next Paint (INP)</td><td>How quickly the page responds to taps and clicks</td><td>200 ms or less</td><td>Over 500 ms</td></tr>
<tr><td>Cumulative Layout Shift (CLS)</td><td>How much the layout jumps while loading</td><td>0.1 or less</td><td>Over 0.25</td></tr>
</tbody>
</table>
<h2>Real-user data vs lab results</h2>
<p>The report has two parts. <strong>What real users experience</strong> comes from the Chrome User Experience Report: anonymous timings from real Chrome visitors over the last 28 days. It’s what Google uses for rankings, but it only exists for pages and sites with enough traffic, so new sites often see “not enough data”.</p>
<p>The <strong>lab test</strong> is a single load in a controlled environment. It’s available for every page and is the best way to check whether a change helped, but the score can move a few points between runs because of network and server variation.</p>
<h2>How to speed up a page</h2>
<ul>
<li><strong>Compress and resize images.</strong> Images are usually the heaviest part of a page. Serve them at the size they’re displayed, in WebP or AVIF, and lazy-load images below the fold. Our <a href="/image-compressor">image compressor</a> helps.</li>
<li><strong>Cut unused JavaScript.</strong> Every script must be downloaded and run. Remove plugins and trackers you don’t need, and load the rest with defer.</li>
<li><strong>Reserve space for images, ads and embeds</strong> with width and height attributes, so the layout doesn’t shift as they load.</li>
<li><strong>Use caching and a CDN</strong> so returning visitors and distant visitors get files faster.</li>
<li><strong>Pick a fast host.</strong> If the server takes over half a second to respond, everything else waits.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Why is my mobile score lower than desktop?</summary><p>The mobile test simulates a mid-range phone on a slower connection, with a slower processor. The same page has to do more work with fewer resources, so mobile scores are almost always lower. That’s also closer to what many real visitors experience.</p></details>
<details><summary>Why did my score change when I tested again?</summary><p>Lab results vary slightly with server load, network conditions and ads or third-party scripts that change between loads. Run the test two or three times and look at the typical result rather than a single number.</p></details>
<details><summary>Does page speed affect Google rankings?</summary><p>Yes, but modestly. Core Web Vitals are part of Google’s page experience signals. Relevant, helpful content matters far more, but when pages are similar, the faster one has an edge, and speed affects how many visitors stay.</p></details>
<details><summary>What happens to the address I enter?</summary><p>It’s sent from your browser to Google’s PageSpeed Insights service, which loads the public page and returns the results. SmartToolsy doesn’t store your tests.</p></details>
<details><summary>Why does it say there’s no real-user data?</summary><p>Chrome only publishes real-user timings for pages and sites with enough visitors. Until then, use the lab results, which measure the same things in a test environment.</p></details>
</div>
"""),
]
