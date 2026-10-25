"""Tool registry part G: image metadata remover and SEO generators."""
from tools_c import drop

GEN = "/assets/seo-gen.js"

TOOLS_G = [
# ---------------------------------------------------------------- metadata remover
dict(
slug="image-metadata-remover", name="Image Metadata Remover", cat="image", ico="MR", scripts=["/assets/metadata.js"],
title="Image Metadata Remover – Remove EXIF & GPS Location from Photos Free",
desc="Remove EXIF data, GPS location, camera details, XMP, IPTC and AI-generation tags from JPG, PNG and WebP photos. See what’s hidden first. Free, no upload, no quality loss.",
short="Strip GPS location, EXIF and hidden data from photos without uploading.",
ui=drop("mr-file", "image/jpeg,image/png,image/webp,.jpg,.jpeg,.png,.webp,.heic", "Choose photos", "JPG, PNG or WebP. Select several at once. Files stay on your device.", True) + """
<p id="mr-msg" class="count-note" aria-live="polite"></p>
<ul id="mr-list" class="mr-list"></ul>
<div class="btns"><button class="btn" id="mr-all" type="button" hidden>Download all as ZIP</button></div>
""",
content="""
<p>Every photo you take carries hidden information. A picture from a phone usually records the exact GPS location where it was taken, the date and time, the phone or camera model, and sometimes its serial number or the owner’s name. Edited images can include the software used, and AI-generated images often carry the full prompt and settings. When you send the original file to someone or post it online, all of that can go with it.</p>
<p>The Image Metadata Remover shows you exactly what’s inside each photo, then removes it. It works entirely in your browser, so your photos are never uploaded, and it strips the data without re-compressing the image, so the picture looks exactly the same.</p>
<h2>How to remove metadata from a photo</h2>
<ol>
<li>Click “Choose photos” and select one or more JPG, PNG or WebP images.</li>
<li>Check the report for each file. Risky items such as GPS location, serial numbers and owner names are highlighted.</li>
<li>Click “Download clean file”, or “Download all as ZIP” for several photos.</li>
</ol>
<h2>What gets removed</h2>
<ul>
<li><strong>EXIF data:</strong> GPS coordinates, date and time, camera make and model, lens, serial numbers, owner and artist names, and editing software.</li>
<li><strong>XMP and IPTC:</strong> descriptions, keywords, author and copyright fields, and editing history added by Photoshop, Lightroom and other apps.</li>
<li><strong>Content Credentials (C2PA)</strong> and similar provenance records.</li>
<li><strong>AI generation data:</strong> prompts and settings that Stable Diffusion, ComfyUI and other generators write into PNG files.</li>
<li><strong>Comments and other hidden blocks</strong>, plus extra data some apps append after the image.</li>
</ul>
<h2>What is kept</h2>
<p>The image itself is copied byte for byte, so there’s no loss of quality and the file usually gets slightly smaller. The colour profile is kept so colours look the same. For JPG photos, the rotation setting is kept in a tiny new record that contains nothing else, so portrait photos don’t suddenly appear sideways.</p>
<h2>Why remove photo metadata?</h2>
<p>The main reason is location. A photo taken at home can reveal your address to anyone who opens the file’s details, and a series of photos can show where you work, where your children go to school, or when you’re away. Sellers listing items online, people sharing photos with strangers, journalists protecting sources and businesses publishing images on their websites all have good reasons to strip it first.</p>
<p>Some social networks remove much of this data when you upload a photo, but files sent by email, shared as documents in messaging apps, attached to forums or posted from cloud storage usually keep everything.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Are my photos uploaded?</summary><p>No. The files are read and cleaned by JavaScript in your browser, and the clean copies are created on your device. Nothing is sent to SmartToolsy or anyone else.</p></details>
<details><summary>Does removing metadata reduce image quality?</summary><p>No. Many tools redraw the image and save it again, which re-compresses it. This tool removes only the metadata blocks and leaves the image data untouched, so the picture is identical.</p></details>
<details><summary>Can I remove metadata from iPhone HEIC photos?</summary><p>Not yet. Convert them to JPG first, or set your iPhone to Settings → Camera → Formats → Most Compatible so new photos are saved as JPG. When sharing from the Photos app, you can also tap Options and turn off Location.</p></details>
<details><summary>How do I check whether a photo has location data?</summary><p>Open it in this tool. If the photo contains GPS coordinates, they appear in red in the report. On a computer you can also right-click the file and look at its properties or info panel.</p></details>
<details><summary>Will this hide a photo’s origin completely?</summary><p>It removes the data stored inside the file. It can’t change what’s visible in the picture itself, such as street signs, faces or reflections, so check those before sharing too.</p></details>
</div>
"""),
# ---------------------------------------------------------------- meta tag generator
dict(
slug="meta-tag-generator", name="Meta Tag Generator", cat="seo", ico="MT", scripts=[GEN],
title="Meta Tag Generator – Free SEO, Open Graph & Twitter Meta Tags",
desc="Generate title, meta description, robots, canonical, Open Graph and X (Twitter) card tags with a live Google and social preview. Copy-ready HTML. Free.",
short="Title, description, Open Graph and X card tags with live previews.",
ui="""
<div class="field"><label for="mt-title">Page title</label><input id="mt-title" type="text" maxlength="200" placeholder="Free Mortgage Calculator – Monthly Payment with Taxes" value=""><div class="meter" id="mt-tm"></div></div>
<div class="field"><label for="mt-desc">Meta description</label><textarea id="mt-desc" rows="3" maxlength="400" placeholder="Work out your monthly mortgage payment with taxes, insurance and PMI. Free, no sign-up."></textarea><div class="meter" id="mt-dm"></div></div>
<div class="row">
<div class="field"><label for="mt-url">Page URL (canonical)</label><input id="mt-url" type="url" placeholder="https://example.com/page/"></div>
<div class="field"><label for="mt-site">Site name</label><input id="mt-site" type="text" placeholder="Example"></div>
</div>
<div class="row">
<div class="field"><label for="mt-img">Share image URL</label><input id="mt-img" type="url" placeholder="https://example.com/share.jpg"></div>
<div class="field"><label for="mt-tw">X (Twitter) username</label><input id="mt-tw" type="text" placeholder="@example"></div>
</div>
<div class="row">
<div class="field"><label for="mt-type">Page type</label><select id="mt-type"><option value="website">Website / page</option><option value="article">Article / blog post</option><option value="product">Product</option></select></div>
<div class="field"><label for="mt-index">Search engines</label><select id="mt-index"><option value="index">Allow indexing</option><option value="noindex">Don’t index (noindex)</option></select></div>
<div class="field"><label for="mt-follow">Links</label><select id="mt-follow"><option value="follow">Follow links</option><option value="nofollow">Don’t follow (nofollow)</option></select></div>
<div class="field"><label for="mt-lang">Language</label><input id="mt-lang" type="text" value="en-US"></div>
</div>
<label class="check"><input id="mt-basic" type="checkbox" checked> Include charset and mobile viewport tags</label>
<ul class="warn-list" id="mt-warn" aria-live="polite"></ul>
<label for="mt-out" class="lbl" style="margin-top:14px">Your meta tags</label>
<textarea id="mt-out" class="code-out" rows="12" readonly spellcheck="false"></textarea>
<div class="btns"><button class="btn" id="mt-copy" type="button">Copy tags</button></div>
<p class="lbl" style="margin-top:18px">Preview</p>
<div id="mt-prev" class="previews"></div>
""",
content="""
<p>Meta tags are short pieces of HTML in a page’s <code>&lt;head&gt;</code> that tell search engines and social networks what the page is about. They don’t appear on the page itself, but they decide the headline and summary people see in Google and the card that appears when your link is shared on Facebook, LinkedIn, WhatsApp, Slack or X.</p>
<p>This meta tag generator writes all the important tags for you, checks the length of your title and description, and shows a live preview of the Google result and the social card. Copy the code and paste it into your page’s <code>&lt;head&gt;</code>, or into your CMS’s SEO settings.</p>
<h2>How to use the meta tag generator</h2>
<ol>
<li>Write a page title and meta description. The bars turn amber or red if they’re likely to be cut off.</li>
<li>Add the page’s full URL, your site name and a share image (1200 × 630 pixels works well everywhere).</li>
<li>Choose whether search engines may index the page and follow its links. Leave the defaults for normal public pages.</li>
<li>Click “Copy tags” and paste them inside the <code>&lt;head&gt;</code> of your page.</li>
</ol>
<h2>Which meta tags matter for SEO</h2>
<ul>
<li><strong>Title tag:</strong> the most important. It’s the clickable headline in search results and a strong signal of what the page is about. Keep it to about 50–60 characters and put the main keyword near the start.</li>
<li><strong>Meta description:</strong> doesn’t directly affect rankings, but a clear, specific description earns more clicks. Google may rewrite it if it doesn’t match the search.</li>
<li><strong>Robots:</strong> controls indexing. You only need it when you want to keep a page out of search (noindex) or stop links being followed.</li>
<li><strong>Canonical link:</strong> tells search engines which URL is the main version when the same content is reachable at several addresses.</li>
<li><strong>Viewport:</strong> makes the page display properly on phones. Google indexes the mobile version of pages, so it’s essential.</li>
</ul>
<p>The old <code>meta keywords</code> tag is ignored by Google and isn’t included.</p>
<h2>Open Graph and X (Twitter) cards</h2>
<p>Open Graph tags (<code>og:title</code>, <code>og:description</code>, <code>og:image</code>) were created by Facebook and are now read by LinkedIn, WhatsApp, Slack, Discord, iMessage and most other apps that show link previews. X reads its own <code>twitter:</code> tags and falls back to Open Graph. Without them, apps guess, and often pick the wrong image or none at all.</p>
<p>To check what your live page already has, run it through the <a href="/seo-checker">SEO checker</a>, or test title and description lengths in the <a href="/serp-preview-tool">SERP preview tool</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Where do I put meta tags?</summary><p>Inside the <code>&lt;head&gt;</code> section of the page, before <code>&lt;/head&gt;</code>. In WordPress, Shopify, Wix and Squarespace, use the page’s SEO settings or an SEO plugin rather than editing code; they create these tags for you.</p></details>
<details><summary>How long should a meta description be?</summary><p>About 120–160 characters. Google cuts longer descriptions at roughly 920 pixels on desktop, which is usually around 155–160 characters.</p></details>
<details><summary>What size should the share image be?</summary><p>1200 × 630 pixels (a 1.91:1 ratio) works for Facebook, LinkedIn and X’s large card. Keep important text away from the edges, since some apps crop to a square.</p></details>
<details><summary>Is anything I type sent anywhere?</summary><p>No. The tags are generated in your browser. The preview only loads your share image from the address you enter.</p></details>
</div>
"""),
# ---------------------------------------------------------------- SERP preview
dict(
slug="serp-preview-tool", name="SERP Preview Tool", cat="seo", ico="SP", scripts=[GEN],
title="SERP Preview Tool – Google Title & Meta Description Length Checker",
desc="See how your page title and meta description look in Google on desktop and mobile. Pixel-width checker shows what will be cut off. Load any live page’s tags. Free.",
short="Preview your Google result and check title and description length in pixels.",
ui="""
<div class="field"><label for="sp-url">Page URL</label><div class="url-row"><input id="sp-url" type="text" inputmode="url" placeholder="https://example.com/blog/my-post/"><button class="btn ghost" id="sp-fetch" type="button">Load from page</button></div><p id="sp-msg" class="count-note" aria-live="polite"></p></div>
<div class="field"><label for="sp-title">Title <span class="count-note" id="sp-tc"></span></label><input id="sp-title" type="text" maxlength="200" value="How to Calculate Roofing Squares and Shingle Bundles (With Examples)"><div class="meter" id="sp-tm"></div></div>
<div class="field"><label for="sp-desc">Meta description <span class="count-note" id="sp-dc"></span></label><textarea id="sp-desc" rows="3" maxlength="400">Learn what a roofing square is, how to measure your roof from the ground, how roof pitch changes the area, and how many bundles of shingles to buy.</textarea><div class="meter" id="sp-dm"></div></div>
<div class="row">
<div class="field"><label for="sp-name">Site name shown in results</label><input id="sp-name" type="text" placeholder="SmartToolsy"></div>
<div class="field"><label class="check" style="margin-top:30px"><input id="sp-date" type="checkbox"> Show a date (like a blog post)</label></div>
</div>
<div class="seg" role="group" aria-label="Device"><button type="button" data-mode="desktop" aria-pressed="true">Desktop</button><button type="button" data-mode="mobile" aria-pressed="false">Mobile</button></div>
<div id="sp-out" class="serp-wrap desktop" aria-live="polite"></div>
<ul class="warn-list" id="sp-tips"></ul>
""",
content="""
<p>The SERP preview tool shows how a page will look in Google’s search results before you publish it. Type a title and meta description, or load them from any live page, and see the result on desktop and mobile. The length bars measure the text in pixels, the same way Google does, so you can see exactly where a long title will be cut off with “…”.</p>
<h2>How to use the SERP preview tool</h2>
<ol>
<li>Enter your page’s title and meta description, or paste a URL and click “Load from page” to pull in the current ones.</li>
<li>Watch the bars: green fits, amber is short, red will be truncated.</li>
<li>Switch between Desktop and Mobile, then rewrite until the important words are visible in both.</li>
</ol>
<h2>Why Google measures pixels, not characters</h2>
<p>Search results have a fixed width, so Google truncates titles when they run out of space, not after a set number of characters. A title full of wide letters like W and M is cut sooner than one with narrow letters like i and l. On desktop, titles are shown at about 600 pixels wide, which is roughly 50–60 characters. Descriptions get about 920 pixels on desktop, around 155–160 characters, and noticeably less on mobile.</p>
<p>These limits are approximate and Google changes its layout from time to time, so put the words that matter most at the start, where they’re never cut.</p>
<h2>Writing titles and descriptions that get clicks</h2>
<ul>
<li><strong>Lead with the topic.</strong> Put the main keyword in the first few words of the title.</li>
<li><strong>Add a reason to click:</strong> a number, a year, “free”, “step by step”, or the specific answer the searcher wants.</li>
<li><strong>Make every page unique.</strong> Duplicate titles make it hard for Google to tell pages apart.</li>
<li><strong>Write the description as a promise.</strong> Say what the reader will get, in plain language, in one or two sentences.</li>
<li><strong>Don’t stuff keywords.</strong> Google may rewrite titles and descriptions that look spammy or don’t match the page.</li>
</ul>
<p>Once you’re happy with the text, the <a href="/meta-tag-generator">meta tag generator</a> turns it into ready-to-paste HTML, and the <a href="/seo-checker">SEO checker</a> reviews the rest of the page.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Why does Google show a different title from mine?</summary><p>Google rewrites titles when it thinks another heading on the page describes it better, often when the title is too long, stuffed with keywords or doesn’t match the content. A clear, accurate title close to your H1 is rewritten less often.</p></details>
<details><summary>Why does Google ignore my meta description?</summary><p>Google picks a snippet from the page when it fits the search better than your description. That’s normal. A specific, well-written description is still used for many searches.</p></details>
<details><summary>Does the “Load from page” button work for any site?</summary><p>It works for public pages. Our server fetches the page and reads its title and meta description. Pages behind a login, or sites that block automated visitors, can’t be loaded.</p></details>
</div>
"""),
# ---------------------------------------------------------------- robots.txt
dict(
slug="robots-txt-generator", name="Robots.txt Generator", cat="seo", ico="RT", scripts=[GEN],
title="Robots.txt Generator – Create a robots.txt File (Block AI Bots Option)",
desc="Create a correct robots.txt file in seconds: allow or block crawlers, disallow folders, add your sitemap, and optionally block AI crawlers like GPTBot and ClaudeBot. Free.",
short="Build a robots.txt with sitemap, blocked folders and AI-bot rules.",
ui="""
<div class="row">
<div class="field"><label for="rb-default">All search engines</label><select id="rb-default"><option value="allow">Allow crawling</option><option value="block">Block the whole site</option></select></div>
<div class="field"><label for="rb-delay">Crawl-delay (seconds, optional)</label><input id="rb-delay" type="number" min="0" max="60" step="1" placeholder="Leave empty"></div>
</div>
<div class="field"><label for="rb-sitemap">Sitemap URL</label><input id="rb-sitemap" type="url" placeholder="https://example.com/sitemap.xml"></div>
<div class="row">
<div class="field"><label for="rb-disallow">Folders or pages to block (one per line)</label><textarea id="rb-disallow" rows="4" placeholder="/admin/&#10;/cart/&#10;/search"></textarea></div>
<div class="field"><label for="rb-allow">Exceptions to allow (optional)</label><textarea id="rb-allow" rows="4" placeholder="/admin/public/"></textarea></div>
</div>
<label class="check"><input id="rb-ai" type="checkbox"> Block AI training crawlers (GPTBot, ClaudeBot, Google-Extended, CCBot and others)</label>
<label class="check"><input id="rb-ais" type="checkbox"> Also block AI search crawlers (OAI-SearchBot, ChatGPT-User, PerplexityBot)</label>
<ul class="warn-list" id="rb-warn" aria-live="polite"></ul>
<label for="rb-out" class="lbl" style="margin-top:14px">Your robots.txt</label>
<textarea id="rb-out" class="code-out" rows="12" readonly spellcheck="false"></textarea>
<div class="btns"><button class="btn" id="rb-copy" type="button">Copy</button><button class="btn ghost" id="rb-dl" type="button">Download robots.txt</button></div>
""",
content="""
<p>A robots.txt file sits at the root of a website (for example <code>example.com/robots.txt</code>) and tells crawlers which parts of the site they may visit. It’s one of the first files Google requests. A good one points crawlers to your sitemap and keeps them out of pages that shouldn’t appear in search, such as admin areas, carts and internal search results.</p>
<p>This robots.txt generator builds a correctly formatted file from a few choices, warns you about common mistakes, and can add rules to block AI crawlers.</p>
<h2>How to create a robots.txt file</h2>
<ol>
<li>Leave “Allow crawling” selected for a normal public website.</li>
<li>Add your sitemap’s full URL.</li>
<li>List any folders or pages crawlers should skip, one per line, starting with a slash.</li>
<li>Choose whether to block AI crawlers.</li>
<li>Download the file and upload it to the root folder of your site, so it opens at <code>yourdomain.com/robots.txt</code>.</li>
</ol>
<h2>How robots.txt rules work</h2>
<ul>
<li><strong>User-agent</strong> names the crawler a group of rules applies to. <code>*</code> means every crawler.</li>
<li><strong>Disallow</strong> blocks a path and everything under it. <code>Disallow: /admin/</code> blocks the admin folder; <code>Disallow: /</code> blocks the whole site; an empty <code>Disallow:</code> allows everything.</li>
<li><strong>Allow</strong> makes an exception inside a blocked folder.</li>
<li><strong>Sitemap</strong> gives the full address of your XML sitemap.</li>
<li>A crawler follows the most specific group that matches its name, so a bot with its own group ignores the <code>*</code> rules.</li>
</ul>
<h2>Robots.txt doesn’t hide pages</h2>
<p>Blocking a page in robots.txt stops crawling, not indexing. If other sites link to a blocked page, Google can still list its URL without a description. To keep a page out of search results, let Google crawl it and add a <code>noindex</code> robots meta tag, which you can create with the <a href="/meta-tag-generator">meta tag generator</a>. And never rely on robots.txt for privacy: the file is public, so it can point curious visitors straight to the folders you list.</p>
<h2>Should you block AI crawlers?</h2>
<p>AI companies use crawlers to collect training data and to fetch pages for AI search answers. Blocking <strong>training crawlers</strong> such as GPTBot (OpenAI), ClaudeBot (Anthropic), Google-Extended (Google’s AI models; it doesn’t affect Google Search) and CCBot (Common Crawl) asks them not to use your content for training. Blocking <strong>AI search crawlers</strong> like OAI-SearchBot and PerplexityBot can remove your pages from those tools’ answers and the visitors they send. Many publishers block training but allow search. Respectable crawlers obey robots.txt, but it’s a request, not a lock.</p>
<p>After uploading, check the file with the <a href="/seo-checker">SEO checker</a>, which confirms that robots.txt is found and lists your sitemap.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Where do I upload robots.txt?</summary><p>To the root of your domain, the same folder as your homepage. Subdomains need their own file. In WordPress, Shopify and similar platforms, use the platform’s robots.txt setting or an SEO plugin instead.</p></details>
<details><summary>Does Google support Crawl-delay?</summary><p>No. Google ignores it. Bing and some other crawlers respect it. If Googlebot is overloading your server, contact your host; Google slows down automatically when a server responds slowly or with errors.</p></details>
<details><summary>Do I need a robots.txt file at all?</summary><p>No, a site works without one and everything is crawlable by default. But a simple file that lists your sitemap is good practice and avoids 404 errors in your logs.</p></details>
</div>
"""),
# ---------------------------------------------------------------- keyword density
dict(
slug="keyword-density-checker", name="Keyword Density Checker", cat="seo", ico="KD", scripts=[GEN],
title="Keyword Density Checker – Free Keyword Frequency & Phrase Counter",
desc="Check keyword density and the most-used words and 2–3 word phrases in any text or web page. Find over-used keywords and check a target keyword. Free.",
short="Most-used words and phrases with density, from text or a URL.",
ui="""
<div class="field"><label for="kd-url">Check a web page (optional)</label><div class="url-row"><input id="kd-url" type="text" inputmode="url" placeholder="https://example.com/blog/post/"><button class="btn ghost" id="kd-fetch" type="button">Load page text</button></div><p id="kd-msg" class="count-note" aria-live="polite"></p></div>
<div class="field"><label for="kd-text">Or paste your text</label><textarea id="kd-text" rows="9" placeholder="Paste an article, product description or any text…"></textarea></div>
<div class="row">
<div class="field"><label for="kd-target">Target keyword (optional)</label><input id="kd-target" type="text" placeholder="e.g. roof pitch"></div>
<div class="field"><label class="check" style="margin-top:30px"><input id="kd-stop" type="checkbox" checked> Ignore common words (the, and, of…)</label></div>
</div>
<div class="stats"><div class="stat"><b id="kd-words">0</b><span>Words</span></div><div class="stat"><b id="kd-unique">0</b><span>Unique words</span></div></div>
<div id="kd-tgt" class="kd-target" aria-live="polite"></div>
<div id="kd-out" class="kd-grid"></div>
""",
content="""
<p>The keyword density checker counts how often each word and phrase appears in a piece of text and shows it as a percentage of all the words. Paste your own draft or load any web page, and you’ll see the most-used single words, two-word phrases and three-word phrases at a glance. Add a target keyword to see exactly how often it appears and whether it’s in the opening.</p>
<h2>How to check keyword density</h2>
<ol>
<li>Paste your text, or enter a URL and click “Load page text”.</li>
<li>Read the three tables. Words above 4% density are highlighted.</li>
<li>Optionally type the keyword you’re targeting to see its count and density.</li>
</ol>
<h2>How keyword density is calculated</h2>
<div class="formula">Keyword density = (times the phrase appears × words in the phrase) ÷ total words × 100</div>
<p>For example, if “roof pitch” appears 6 times in a 1,200-word article, its density is 6 × 2 ÷ 1,200 × 100 = 1%.</p>
<h2>Is there an ideal keyword density?</h2>
<p>No. Google doesn’t use a target percentage, and pages don’t rank better for hitting a number like 2%. Search engines understand topics, synonyms and related terms, so a page about roof pitch that also talks about rafters, slope and multipliers is seen as more relevant than one that repeats “roof pitch” over and over.</p>
<p>Use the checker for two practical jobs instead:</p>
<ul>
<li><strong>Spot stuffing.</strong> If one word stands far above everything else, the text probably reads unnaturally. Rewrite some mentions with synonyms or pronouns.</li>
<li><strong>Confirm the topic is clear.</strong> The phrases you want to rank for should appear among the top terms, and in the title, first paragraph and headings. If they’re missing, the page may not say what you think it says.</li>
</ul>
<p>To see how your title and description will look in Google, use the <a href="/serp-preview-tool">SERP preview tool</a>. For a full on-page review, run the <a href="/seo-checker">SEO checker</a>. To count words, sentences and reading time, use the <a href="/word-counter">word counter</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Why do menu words show up when I load a page?</summary><p>“Load page text” reads all visible text, including navigation, sidebars and footers. For an exact count of the article only, paste the article text instead.</p></details>
<details><summary>What counts as a common word?</summary><p>Very frequent words that carry little meaning, such as the, and, of, to and is. Hiding them makes the useful keywords easier to see. Untick the box to include them.</p></details>
<details><summary>Is my text sent anywhere?</summary><p>Pasted text is analysed in your browser and never leaves your device. If you load a URL, our server fetches that public page and returns its text.</p></details>
</div>
"""),
]
