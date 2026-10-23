"""Starter guide articles. Each links to related tools."""

ARTICLES = [
dict(
slug="strong-password-you-can-remember", date="2026-10-24",
title="How to Create a Strong Password You Can Actually Remember",
desc="Practical ways to build passwords that resist cracking but are easy to recall, plus when to let a password manager do the work.",
tools=["password-generator"],
body="""
<p>Most people know they should use strong passwords. The trouble is that “strong” usually means something like <code>q7#Lp!2vXz</code>, and nobody can remember forty of those. The good news is that strength and memorability are not opposites. You just need to understand what actually makes a password hard to crack.</p>

<h2>What attackers really do</h2>
<p>When a website is breached, attackers usually get a database of scrambled (hashed) passwords. They then run guesses through the same scrambling process at enormous speed, often billions of guesses per second on graphics cards. They do not start with random strings. They start with lists of leaked passwords, dictionary words, names, dates and common patterns such as a capital letter at the start and “1!” at the end.</p>
<p>That is why <code>Summer2024!</code> is weak even though it has upper case, lower case, a number and a symbol. It follows exactly the pattern attackers try first.</p>

<h2>Length beats complexity</h2>
<p>Every extra character multiplies the number of possibilities. A random 8-character password using all character types has about 6 quadrillion combinations, which sounds huge but can be exhausted by a determined attacker. A random 16-character password has so many combinations that trying them all is not realistic with any current technology.</p>
<p>For passwords you have to type and remember, the practical lesson is simple: make them long.</p>

<h2>Method 1: the random passphrase</h2>
<p>Pick four to six words <em>at random</em>, not words that form a sentence you would naturally say. For example: <code>orbit-lantern-cactus-violin-pepper</code>. Five random words from a large list are far harder to crack than a short scramble, and you can picture them as a little scene to remember them.</p>
<p>The important word is random. “I love my dog Max” is not random, and phrases from songs, films and books appear in attackers’ lists. Roll dice against a word list, or use a generator, rather than choosing words yourself.</p>

<h2>Method 2: let a password manager remember</h2>
<p>For most accounts you never need to remember the password at all. A password manager stores a unique, fully random password for every site and fills it in for you. You only memorise one strong passphrase to unlock the manager.</p>
<p>Use our <a href="/password-generator">password generator</a> to create those random passwords. Set the length to at least 16, keep all character types turned on unless a site rejects symbols, and paste the result straight into your manager.</p>

<h2>Never reuse a password</h2>
<p>Reuse is the single biggest risk for ordinary people. When one small website leaks its database, attackers try the same email and password on email providers, banks and shopping sites. This is called credential stuffing, and it works because so many people reuse passwords. A unique password for each account turns a leak into a minor nuisance instead of a disaster.</p>

<h2>Add a second factor</h2>
<p>Two-factor authentication (2FA) asks for something besides your password, usually a code from an app or a physical security key. Even if your password is stolen, the attacker cannot sign in without that second factor. Turn it on first for your email account, because email is how every other password gets reset.</p>

<h2>A simple plan</h2>
<ol>
<li>Create one long, random passphrase for your password manager and memorise it.</li>
<li>Use the manager to generate a unique random password for every other account.</li>
<li>Turn on 2FA for email, banking and social media.</li>
<li>Change any password you know has been reused or leaked.</li>
</ol>
<p>That is all it takes to be much safer than the average internet user, and none of it requires remembering dozens of strings of symbols.</p>
"""),
dict(
slug="compress-images-for-website", date="2026-10-24",
title="How to Compress Images for Your Website Without Losing Quality",
desc="A practical guide to image sizes, formats and quality settings that make web pages load fast while photos still look sharp.",
tools=["image-compressor"],
body="""
<p>Images are usually the heaviest thing on a web page. A single photo straight from a phone can be 4 or 5 MB, which is more than many entire well-built pages. Shrinking images is one of the quickest ways to make a site faster, and done properly, visitors cannot see the difference.</p>

<h2>Step 1: resize to the size you actually display</h2>
<p>A modern phone camera produces images around 4000 pixels wide. Most blog content areas are 700 to 1200 pixels wide. Uploading the full camera image means the visitor downloads millions of pixels that are thrown away when the browser scales the picture down.</p>
<p>A good rule is to export images at about twice the width they appear on screen, so they stay crisp on high-resolution displays. For a 800-pixel content column, 1600 pixels wide is plenty. Resizing alone often cuts the file size by 70% or more.</p>

<h2>Step 2: choose the right format</h2>
<ul>
<li><strong>JPG</strong> is the classic choice for photographs. It compresses smooth color gradients very well.</li>
<li><strong>WebP</strong> does the same job as JPG but usually produces files around a quarter to a third smaller at similar visual quality. Every current major browser supports it, so it is the best default for photos on the web today.</li>
<li><strong>PNG</strong> is lossless and supports transparency. Use it for logos, icons and screenshots with sharp text, not for photos, where it creates very large files.</li>
<li><strong>SVG</strong> is the best option for simple logos and icons, because it is vector-based and stays sharp at any size.</li>
</ul>

<h2>Step 3: pick a sensible quality setting</h2>
<p>JPG and WebP let you choose a quality level. The relationship between quality and file size is not linear. Dropping from 100% to around 80% can halve the size with no visible change, while going below about 60% starts to introduce blocky artifacts around edges and in skies.</p>
<p>Try 75% as a starting point, then compare the result with the original at actual size. If you cannot spot a difference, try going a little lower. Our <a href="/image-compressor">image compressor</a> shows the new file size and a preview as you move the slider, all inside your browser.</p>

<h2>Step 4: strip metadata</h2>
<p>Photos carry hidden EXIF data such as camera model, settings and sometimes GPS location. It adds a few kilobytes and can reveal where a photo was taken. Re-saving the image through a compressor that draws it onto a canvas, as ours does, removes this data automatically.</p>

<h2>Step 5: let the browser help</h2>
<p>Once images are compressed, a couple of HTML attributes help them load efficiently:</p>
<ul>
<li>Add <code>loading="lazy"</code> to images further down the page so they load only when the visitor scrolls near them.</li>
<li>Always set <code>width</code> and <code>height</code> attributes so the browser reserves space and the layout does not jump while images load.</li>
</ul>

<h2>Why it matters</h2>
<p>Google’s Core Web Vitals include Largest Contentful Paint, which measures how quickly the main content, often a hero image, appears. Slow pages also lose visitors, especially on mobile data. Spending a minute compressing each image before upload pays off in speed, search visibility and lower hosting bandwidth.</p>

<h2>Quick checklist</h2>
<ol>
<li>Resize to about twice the display width.</li>
<li>Use WebP or JPG for photos, PNG or SVG for graphics.</li>
<li>Start at 75% quality and compare.</li>
<li>Aim for under 200 KB for most content images.</li>
<li>Add lazy loading and dimensions in your HTML.</li>
</ol>
"""),
dict(
slug="percentage-tricks-mental-math", date="2026-10-24",
title="How to Calculate Percentages in Your Head: 6 Quick Tricks",
desc="Simple mental math shortcuts for tips, discounts and percentage changes, with worked examples you can use while shopping.",
tools=["percentage-calculator", "discount-calculator"],
body="""
<p>You do not need a calculator for most everyday percentages. With a handful of shortcuts you can work out a tip, check a sale price or judge a pay rise in a few seconds. Here are six tricks that cover almost every situation.</p>

<h2>1. Find 10% by moving the decimal point</h2>
<p>To get 10% of any number, move the decimal point one place to the left. 10% of 250 is 25. 10% of 47.80 is 4.78. This is the foundation for nearly every other trick.</p>

<h2>2. Build other percentages from 10%</h2>
<ul>
<li><strong>5%</strong> is half of 10%. 5% of 250 is 12.50.</li>
<li><strong>20%</strong> is double 10%. 20% of 250 is 50.</li>
<li><strong>15%</strong> is 10% plus 5%. 15% of 250 is 25 + 12.50 = 37.50.</li>
<li><strong>1%</strong> moves the decimal two places. 1% of 250 is 2.50, so 3% is 7.50.</li>
</ul>
<p>Almost any percentage can be assembled this way. 18% is 20% minus 2%. 35% is 30% plus 5%.</p>

<h2>3. Swap the numbers when it is easier</h2>
<p>X% of Y always equals Y% of X. So 8% of 50 is the same as 50% of 8, which is obviously 4. Whenever one number is awkward and the other is friendly, flip them. 4% of 75 becomes 75% of 4, which is 3.</p>

<h2>4. Work out a sale price in one step</h2>
<p>Instead of finding the discount and subtracting it, find what you <em>pay</em>. 30% off means you pay 70%. On a 60 item, 70% of 60 is 42. That is one calculation instead of two.</p>
<p>For stacked discounts, multiply what you pay at each stage. 30% off then an extra 10% off means 70% of 90%, which is 63%, so the total discount is 37%, not 40%. Our <a href="/discount-calculator">discount calculator</a> handles these combinations for you.</p>

<h2>5. Percentage change: compare the difference to the starting point</h2>
<p>To find how much something changed in percentage terms, divide the change by the original value. If rent goes from 800 to 880, the change is 80, and 80 is 10% of 800, so it rose 10%.</p>
<p>Always divide by the <em>starting</em> value. This is why a fall of 50% needs a rise of 100% to recover: from 100 to 50 is half, but from 50 back to 100 is double.</p>

<h2>6. Estimate, then check</h2>
<p>Round awkward numbers to friendly ones to get a quick estimate. 19% of 412 is close to 20% of 400, which is 80. The real answer is 78.28, so the estimate is good enough to judge whether a deal is worth it. When the exact figure matters, such as on an invoice, use the <a href="/percentage-calculator">percentage calculator</a> to confirm.</p>

<h2>Practice examples</h2>
<ol>
<li>A 15% tip on a bill of 64: 10% is 6.40, 5% is 3.20, total 9.60.</li>
<li>25% off a 120 jacket: you pay 75%, which is 90.</li>
<li>A salary rising from 50,000 to 53,500: the change is 3,500, which is 7% of 50,000.</li>
</ol>
<p>With a little practice these become automatic, and you will spot misleading “deals” much faster.</p>
"""),
]
