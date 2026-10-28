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
dict(
slug="how-to-merge-pdf-files", date="2026-10-24",
title="How to Merge PDF Files on iPhone, Android, Mac and Windows",
desc="Step-by-step ways to combine PDFs into one file on any device, using built-in apps where they exist and a free browser tool where they don’t.",
tools=["merge-pdf", "split-pdf"],
body="""
<p>Job portals, landlords, schools and accountants often ask for “one PDF”. If your documents are spread across several files, you need to merge them. Some devices can do this with built-in apps, and others need help. Here is the quickest method for each one.</p>

<h2>The method that works everywhere</h2>
<p>Our <a href="/merge-pdf">Merge PDF</a> tool runs in any modern browser on a phone, tablet or computer:</p>
<ol>
<li>Open the tool and tap “Choose PDF files”.</li>
<li>Select all the PDFs you want to combine.</li>
<li>Use the arrows to put them in order. The top file becomes the first pages.</li>
<li>Tap “Merge PDFs” and then “Download merged PDF”.</li>
</ol>
<p>The files are combined inside your browser and are not uploaded, so it is safe for bank statements, IDs and contracts. Pages are copied without re-compression, so text stays sharp and searchable.</p>

<h2>On an iPhone or iPad</h2>
<p>Apple’s Files app can combine PDFs without any extra app:</p>
<ol>
<li>Save the PDFs into the same folder in the Files app (from Mail, tap and hold an attachment and choose “Save to Files”).</li>
<li>Tap the “…” button at the top right, then “Select”.</li>
<li>Tap the files in the order you want them combined.</li>
<li>Tap the “…” button at the bottom right and choose “Create PDF”.</li>
</ol>
<p>A new PDF appears in the same folder. If the pages end up in the wrong order, rename the originals with numbers first (1-cover, 2-resume and so on), or use the browser tool above, where you can reorder files freely.</p>

<h2>On an Android phone</h2>
<p>Android does not include a dedicated merge feature in its standard Files app. The simplest option is to open the <a href="/merge-pdf">Merge PDF</a> tool in Chrome, choose your files from Downloads or Google Drive, and merge them there. Nothing needs to be installed.</p>

<h2>On a Mac</h2>
<p>Preview, the built-in PDF viewer, can merge files:</p>
<ol>
<li>Open the first PDF in Preview.</li>
<li>Choose View → Thumbnails to show the page sidebar.</li>
<li>Drag the other PDF files from Finder into the sidebar, dropping them where you want their pages to go.</li>
<li>Choose File → Export as PDF to save the combined document under a new name.</li>
</ol>
<p>Saving as a new file keeps your originals untouched.</p>

<h2>On Windows</h2>
<p>Windows does not include a tool that merges existing PDFs. “Microsoft Print to PDF” can turn a single document into a PDF but cannot join several PDFs. Use the <a href="/merge-pdf">browser tool</a> in Edge or Chrome instead; it works the same way as on a phone.</p>

<h2>Getting the order and size right</h2>
<ul>
<li><strong>Put the most important document first.</strong> Reviewers often only skim the first pages. A cover letter or summary belongs at the front.</li>
<li><strong>Remove pages you do not need first.</strong> If a bank statement has a blank last page or marketing inserts, cut them out with <a href="/split-pdf">Split PDF</a> before merging.</li>
<li><strong>Watch the file size limit.</strong> Upload portals and email services commonly cap attachments somewhere between a few megabytes and about 25 MB. If photos are making your PDF large, compress them before turning them into a PDF.</li>
<li><strong>Name the file clearly.</strong> Something like <code>Lastname-Firstname-Application.pdf</code> is easier for the recipient than <code>merged.pdf</code>.</li>
</ul>

<h2>What does not carry over</h2>
<p>Merging copies the visible pages. Fillable form fields, bookmarks and digital signatures from the originals may not survive, because they belong to each file’s internal structure. If a document has been digitally signed, send it as a separate file so the signature remains valid.</p>

<h2>Password-protected PDFs</h2>
<p>Locked PDFs cannot be merged until they are unlocked. Open the file with its password in your PDF reader and save or print a copy without protection, then merge that copy. Only do this with documents you are entitled to edit.</p>

<h2>Quick summary</h2>
<ul>
<li>iPhone and iPad: Files app → Select → Create PDF.</li>
<li>Mac: Preview → drag files into the thumbnail sidebar → Export as PDF.</li>
<li>Android and Windows: use a browser-based merge tool.</li>
<li>Any device, with full control over order: <a href="/merge-pdf">Merge PDF</a>.</li>
</ul>
"""),
dict(
slug="how-much-house-can-i-afford-70k-salary", date="2026-10-24",
title="How Much House Can I Afford on a $70,000 Salary?",
desc="Worked examples using the 28/36 rule, real monthly costs and different down payments to estimate a realistic home price on a $70k income.",
tools=["mortgage-calculator", "loan-calculator", "percentage-calculator"],
body="""
<p>A $70,000 salary is close to the middle of the US income range, and it can buy a home in many parts of the country. How much house it buys depends less on the salary itself and more on four things: your other debts, your down payment, the interest rate you get, and local property taxes and insurance. This guide walks through the math so you can estimate your own number.</p>

<h2>Start with the 28/36 rule</h2>
<p>Many lenders and financial planners use the 28/36 rule as a starting point:</p>
<ul>
<li>Spend no more than <strong>28%</strong> of your gross (pre-tax) monthly income on housing: mortgage principal and interest, property tax, homeowners insurance, mortgage insurance and HOA dues.</li>
<li>Keep <strong>all</strong> monthly debt payments, including housing, car loans, student loans and credit card minimums, at or below <strong>36%</strong>.</li>
</ul>
<p>On $70,000 a year, your gross monthly income is about $5,833. That gives:</p>
<ul>
<li>A housing budget of about <strong>$1,633 a month</strong> (28%).</li>
<li>A total debt budget of about <strong>$2,100 a month</strong> (36%).</li>
</ul>
<p>If your other debts are more than about $467 a month, the 36% limit becomes the tighter one. With a $700 car and student loan payment, for example, your housing budget drops to $2,100 − $700 = $1,400.</p>

<h2>Turning $1,633 a month into a home price</h2>
<p>The monthly payment is not just the loan. We used the <a href="/mortgage-calculator">mortgage calculator</a> with these assumptions, which are typical but should be replaced with your local figures:</p>
<ul>
<li>30-year fixed-rate mortgage</li>
<li>Property tax of 1.1% of the price per year</li>
<li>Homeowners insurance of $1,800 per year</li>
<li>PMI of 0.6% of the loan per year when the down payment is under 20%</li>
<li>No HOA dues</li>
</ul>
<p>Keeping the total payment at about $1,633 a month gives these maximum prices:</p>
<table class="sched" style="width:100%;border-collapse:collapse">
<thead><tr><th>Interest rate</th><th>5% down</th><th>10% down</th><th>20% down</th></tr></thead>
<tbody>
<tr><td>6.0%</td><td>$209,000</td><td>$219,000</td><td>$260,000</td></tr>
<tr><td>6.5%</td><td>$201,000</td><td>$210,000</td><td>$248,000</td></tr>
<tr><td>7.0%</td><td>$192,000</td><td>$202,000</td><td>$238,000</td></tr>
</tbody></table>
<p>So on a $70k salary with no other large debts, a realistic price range is roughly <strong>$190,000 to $260,000</strong>. That is in the same neighborhood as the older rule of thumb that a home should cost about two and a half to three times your annual income ($175,000 to $210,000 here).</p>

<h2>Why the down payment matters so much</h2>
<p>Look across any row of the table: going from 10% to 20% down adds around $40,000 to your budget. Two things are happening. You borrow less, and you avoid private mortgage insurance (PMI), which lenders usually charge on conventional loans when you put down less than 20%. On a $189,000 loan, PMI at 0.6% adds about $95 a month.</p>
<p>A bigger down payment is not always the right move, though. Keep an emergency fund of several months of expenses after closing, and remember that closing costs typically add a few percent of the loan amount on top of the down payment.</p>

<h2>Why the interest rate matters</h2>
<p>Each half-point increase in the rate cuts your buying power by roughly $8,000 to $12,000 in these examples. Rates depend on the market, your credit score, your down payment and the loan type, so get quotes from at least three lenders. A better credit score before you apply can be worth more than months of extra saving.</p>

<h2>Local costs can change the answer</h2>
<p>Property tax rates differ enormously between states and even neighboring counties. Insurance costs are much higher in areas with hurricane, wildfire or flood risk, and a condo or planned community may charge HOA dues of a few hundred dollars a month. In the examples above, every extra $100 of monthly costs reduces the price you can afford by roughly $12,000 to $15,000. Look up the actual tax bill on listing pages and get an insurance quote before you make an offer.</p>

<h2>A worked example</h2>
<p>Suppose you find a $230,000 home, put 10% down and get a 6.5% rate. Using the same tax and insurance assumptions, the payment comes to about:</p>
<ul>
<li>Principal and interest: $1,308</li>
<li>Property tax: $211</li>
<li>Insurance: $150</li>
<li>PMI: $104</li>
<li><strong>Total: about $1,773 a month</strong>, or roughly 30% of gross income</li>
</ul>
<p>That is slightly above the 28% guideline. A lender may still approve it, but you would have less room for savings and repairs. Options would be a larger down payment, a lower price, or shopping for a lower rate.</p>

<h2>What lenders actually look at</h2>
<p>The 28/36 rule is a guideline, not a law. Lenders look at your debt-to-income ratio, credit score, savings and job history, and some loan programs allow higher ratios. Being approved for a larger loan does not mean the payment will feel comfortable. Budget for maintenance too; many homeowners set aside around 1% of the home’s value each year for repairs.</p>

<h2>Run your own numbers</h2>
<p>Open the <a href="/mortgage-calculator">mortgage calculator</a>, enter your expected rate, local tax rate and insurance, and adjust the home price until the monthly total matches your budget. Try the 15-year term as well to see how much interest you would save.</p>
<p><em>This article is general information, not financial advice. Speak to a lender or housing counselor about your situation.</em></p>
"""),
dict(
slug="convert-pdf-to-jpg-without-software", date="2026-10-24",
title="How to Convert a PDF to JPG Without Installing Software",
desc="Free ways to save PDF pages as images on Windows, Mac, iPhone and Android, plus how to pick the right resolution and format.",
tools=["pdf-to-jpg", "image-compressor"],
body="""
<p>Many apps and websites accept images but not PDFs: social media posts, chat apps that don’t preview documents, some online forms and most slide decks. Converting a PDF page to a JPG solves that. You don’t need to install anything. Here are the options for each device, from quickest to best quality.</p>

<h2>Option 1: a browser-based converter (any device)</h2>
<p>Our <a href="/pdf-to-jpg">PDF to JPG</a> tool works on Windows, Mac, iPhone, Android and Chromebook:</p>
<ol>
<li>Open the tool and choose your PDF.</li>
<li>Pick JPG or PNG and a quality level.</li>
<li>Optionally enter the pages you need, such as <code>1</code> or <code>2-4</code>.</li>
<li>Click “Convert to images” and download each page.</li>
</ol>
<p>The conversion happens in your browser with Mozilla’s open-source PDF.js engine, so the file is never uploaded. Every page comes out as a separate, full-resolution image, which is much sharper than a screenshot.</p>

<h2>Option 2: Preview on a Mac</h2>
<ol>
<li>Open the PDF in Preview.</li>
<li>Select the page you want in the thumbnail sidebar.</li>
<li>Choose File → Export, set Format to JPEG, choose a resolution and save.</li>
</ol>
<p>Preview exports one page at a time this way, so for long documents the browser tool is faster.</p>

<h2>Option 3: a screenshot (quick but lower quality)</h2>
<p>On any device you can zoom the PDF to fill the screen and take a screenshot: Windows key + Shift + S on Windows, Shift + Command + 4 on a Mac, or the usual button combination on a phone. Screenshots are limited to your screen’s resolution and include anything else visible, so they are fine for a quick share but not for printing or official documents.</p>

<h2>Choosing the right resolution</h2>
<p>PDF pages don’t have pixels until they are rendered, so you choose the resolution, measured in dots per inch (DPI):</p>
<ul>
<li><strong>96 DPI</strong> is enough for viewing on a phone or posting online.</li>
<li><strong>150 DPI</strong> is a good default. A US Letter page becomes about 1275 × 1650 pixels, sharp on almost any screen.</li>
<li><strong>300 DPI</strong> is for printing. Files are about four times larger than at 150 DPI.</li>
</ul>

<h2>JPG or PNG?</h2>
<p>JPG produces much smaller files and suits pages that are mostly photos. PNG keeps text, lines and charts perfectly crisp, which makes it the better choice for documents, invoices and slides, at the cost of larger files. If a JPG is still too big to upload, shrink it with the <a href="/image-compressor">Image Compressor</a>.</p>

<h2>Common problems</h2>
<ul>
<li><strong>The image looks blurry.</strong> Choose a higher DPI, or PNG instead of JPG for text-heavy pages.</li>
<li><strong>The file won’t open.</strong> Password-protected PDFs must be unlocked in your PDF reader first.</li>
<li><strong>Only some pages are needed.</strong> Enter a page range rather than converting the whole document.</li>
<li><strong>A form asks for one image of several pages.</strong> Most forms that want multiple pages actually accept a PDF; check the instructions before converting.</li>
</ul>

<h2>Converting on a phone</h2>
<p>On an iPhone or Android phone, open the <a href="/pdf-to-jpg">PDF to JPG</a> tool in Safari or Chrome and choose the PDF from your Files app, Downloads or a cloud drive. After conversion, tap and hold an image preview to save it to your photo library, or tap its download link to save it as a file. This route avoids installing a converter app that may ask for wide permissions or show full-screen ads.</p>

<h2>Is it safe to convert private documents online?</h2>
<p>It depends on the service. Many online converters upload your file to their servers, process it there and keep it for a period of time. That is a concern for tax forms, medical records or anything with an account number. Before using any converter, check whether it uploads files. Our converter does not: the PDF is opened and drawn by your own browser, and you can confirm this by switching off your internet connection after the page has loaded. The tool keeps working.</p>

<h2>Converting many pages at once</h2>
<p>For a long document, decide first which pages you actually need and enter them as a range. Converting a 100-page manual at 300 DPI produces hundreds of megabytes of images and takes a while on older phones. If you need every page as images for an archive, 150 DPI JPG is usually a sensible balance between size and readability.</p>

<h2>Going the other way</h2>
<p>If you have photos that need to become a PDF, use <a href="/jpg-to-pdf">JPG to PDF</a>. It places each image on its own page and can fit them to US Letter or A4 paper.</p>
"""),
dict(
slug="how-to-split-pdf-extract-pages", date="2026-10-24",
title="How to Split a PDF and Extract Only the Pages You Need",
desc="Practical ways to pull specific pages out of a PDF or break it into smaller files, including the built-in print trick and page-range tips.",
tools=["split-pdf", "merge-pdf"],
body="""
<p>You rarely need to send a whole PDF. An application might want only the signature page of a contract, your accountant might need one month from a year-long statement, or a 40 MB scan might be too large to email in one piece. Splitting a PDF lets you keep exactly the pages you need.</p>

<h2>The fastest way: a browser tool</h2>
<p>Use our <a href="/split-pdf">Split PDF</a> tool on any phone or computer:</p>
<ol>
<li>Choose your PDF. The tool shows how many pages it contains.</li>
<li>Type the pages you want, for example <code>2, 5-7</code>.</li>
<li>Choose whether you want one combined file, one file per range, or one file per page.</li>
<li>Click “Split PDF” and download the results.</li>
</ol>
<p>The document is processed entirely in your browser and is not uploaded, which matters for financial and legal paperwork.</p>

<h2>How to write page ranges</h2>
<ul>
<li><code>3</code> takes a single page.</li>
<li><code>4-9</code> takes pages 4 to 9, including both.</li>
<li><code>12-</code> takes page 12 through the last page.</li>
<li><code>1, 3, 5</code> takes three separate pages.</li>
<li><code>5, 1</code> puts page 5 before page 1, a quick way to reorder pages.</li>
</ul>

<h2>The built-in “print to PDF” trick</h2>
<p>If you only need one continuous range, most devices can do it through the print dialog:</p>
<ol>
<li>Open the PDF in Chrome, Edge or your PDF viewer.</li>
<li>Choose Print.</li>
<li>Set the printer to “Save as PDF” (or “Microsoft Print to PDF” on Windows).</li>
<li>Under Pages, enter the range you want, such as 3-5, and save.</li>
</ol>
<p>This works well for simple cases. Two drawbacks: it can flatten fillable form fields, and some printers’ drivers re-render the pages, which may increase the file size or make text less sharp. The split tool copies pages exactly instead.</p>

<h2>On a Mac</h2>
<p>In Preview, show the thumbnail sidebar (View → Thumbnails), select the pages you want, and drag them onto the desktop. Preview creates a new PDF containing just those pages.</p>

<h2>Common reasons to split a PDF</h2>
<ul>
<li><strong>Sending only what is asked for.</strong> A landlord may need proof of income, not every page of your tax return. Sharing less personal data is safer.</li>
<li><strong>Meeting upload limits.</strong> Splitting a long scan into two or three files can bring each one under a portal’s size limit.</li>
<li><strong>Separating a batch scan.</strong> If you scanned a stack of receipts as one file, the “every page as its own PDF” option gives you one file per receipt.</li>
<li><strong>Building a new document.</strong> Extract the pages you need from several files, then join them with <a href="/merge-pdf">Merge PDF</a>.</li>
</ul>

<h2>Example: getting a large scan under an upload limit</h2>
<p>Say a portal accepts files up to 5 MB and your scanned lease is a 12 MB, 18-page PDF. First check whether the portal allows several files. If it does:</p>
<ol>
<li>Open the lease in <a href="/split-pdf">Split PDF</a> and choose “Each range as a separate PDF”.</li>
<li>Enter three ranges, such as <code>1-6, 7-12, 13-18</code>.</li>
<li>Check the size shown next to each download. Scanned pages are usually similar in size, so equal ranges give similar files. If one part is still too big, split that range again.</li>
<li>Name the parts in order, such as <code>Lease-part-1-of-3.pdf</code>, so the reviewer reads them correctly.</li>
</ol>
<p>If the portal accepts only one file, splitting will not help. In that case you need to reduce the size of the images inside the pages, for example by rescanning at 150–200 DPI instead of 600 DPI, or by photographing the pages and rebuilding the PDF from compressed images with <a href="/jpg-to-pdf">JPG to PDF</a>.</p>

<h2>Keeping track of what you removed</h2>
<p>When you send only part of a document, it can help to tell the recipient. A short note such as “Attached are pages 1–3 and the signature page, 12, of the agreement” avoids confusion and shows you did not leave anything out by accident. Keep the original full PDF in a safe place, because splitting creates new files and never changes the original.</p>

<h2>Does splitting reduce quality?</h2>
<p>No. A proper split copies each page as it is: text stays selectable, images keep their resolution and the page size does not change. If your split files are still large, the size comes from high-resolution images inside the pages; splitting can’t shrink those.</p>

<h2>What about password-protected PDFs?</h2>
<p>A PDF with an open password must be unlocked before any tool can read its pages. Open it in your PDF reader with the password and save an unprotected copy, provided you have the right to do so.</p>
"""),
dict(
slug="photos-to-pdf-for-applications", date="2026-10-24",
title="How to Turn Photos Into a PDF for Applications and Forms",
desc="Take clear photos of documents, combine them into one PDF and keep the file under upload limits, on your phone or computer.",
tools=["jpg-to-pdf", "image-compressor", "merge-pdf"],
body="""
<p>College admissions, job applications, rental applications, visa forms and insurance claims often ask you to upload documents as a PDF. If all you have is a phone, you can still produce a clean, professional-looking PDF in a few minutes. The trick is to take good photos first and then combine them correctly.</p>

<h2>Step 1: take photos that are easy to read</h2>
<ul>
<li><strong>Use daylight or bright, even light.</strong> Avoid the camera flash, which causes glare on glossy paper.</li>
<li><strong>Place the document on a dark, plain surface.</strong> The contrast makes edges clear and looks better when cropped.</li>
<li><strong>Hold the phone directly above the page</strong>, parallel to it, so the page is a rectangle rather than a trapezoid.</li>
<li><strong>Fill the frame</strong> with the page, leaving a small border, and make sure all four corners are visible.</li>
<li><strong>Check focus</strong> by zooming in on small print before moving to the next page.</li>
</ul>
<p>Many phones also include a document scanner that straightens and crops pages automatically. On an iPhone it is in the Notes app (create a note, tap the camera icon, then “Scan Documents”); on Android, the Google Drive app has a Scan button. If you use these, they can save directly as a PDF.</p>

<h2>Step 2: combine the photos into one PDF</h2>
<p>Use <a href="/jpg-to-pdf">JPG to PDF</a> in your phone or computer browser:</p>
<ol>
<li>Choose all the photos. JPG, PNG and WebP all work.</li>
<li>Put them in the right order with the arrow buttons.</li>
<li>Choose US Letter for US forms (or A4 for most other countries) so the PDF prints at a normal paper size.</li>
<li>Leave orientation on Automatic, so tall photos get portrait pages and wide photos get landscape pages.</li>
<li>Click “Create PDF” and download.</li>
</ol>
<p>The tool respects the rotation your phone recorded, so pages appear the right way up, and it adds no watermark. Your images are processed on your device, not uploaded.</p>

<h2>Step 3: check the file size</h2>
<p>Upload portals often set limits of a few megabytes per file. Phone photos are large, typically several megabytes each, so a five-page PDF can easily exceed a limit. If yours is too big:</p>
<ol>
<li>Run the photos through the <a href="/image-compressor">Image Compressor</a> first. Set the maximum width to about 1600 pixels and quality to around 75%. Text remains readable and each photo usually drops to a few hundred kilobytes.</li>
<li>Create the PDF again from the compressed images.</li>
</ol>
<p>As a rule of thumb, aim for around 150–300 KB per page for documents that will only be viewed on screen.</p>

<h2>Step 4: name and review the file</h2>
<ul>
<li>Open the PDF and scroll through every page before you upload it. Check that nothing is cut off and that the order is right.</li>
<li>Name it clearly, for example <code>Garcia-Maria-Proof-of-Address.pdf</code>. Reviewers handle hundreds of files named <code>scan.pdf</code>.</li>
<li>If the form wants a single file containing several documents, create a PDF for each and then combine them with <a href="/merge-pdf">Merge PDF</a>.</li>
</ul>

<h2>Common mistakes to avoid</h2>
<ul>
<li><strong>Uploading a photo of a screen.</strong> If you have the original digital document, save it as a PDF directly instead.</li>
<li><strong>Cropping off edges.</strong> Some reviewers reject documents where page numbers, dates or signatures are cut off.</li>
<li><strong>Mixing up front and back.</strong> For IDs and cards, put the front first, then the back, and say so in the form if there is a notes field.</li>
<li><strong>Sharing more than needed.</strong> Cover or remove information that was not requested, such as full account numbers, if the instructions allow it.</li>
</ul>

<h2>Doing it on a computer</h2>
<p>The same steps work on Windows and Mac: transfer the photos from your phone (by cable, AirDrop, or a cloud drive), then use <a href="/jpg-to-pdf">JPG to PDF</a> in your browser. A larger screen makes it easier to spot blurry pages before you submit.</p>
"""),
dict(
slug="how-to-combine-pdf-files-on-mac", date="2026-10-24",
title="How to Combine PDF Files on a Mac (3 Free Ways)",
desc="Merge PDFs on macOS with Finder Quick Actions, Preview or a browser tool. Step-by-step instructions, page-order tips and fixes for common problems.",
tools=["merge-pdf", "delete-pdf-pages", "add-pages-to-pdf"],
body="""
<p>Macs come with everything you need to combine PDF files, no paid software required. There are three good ways to do it, and which one is best depends on whether you want speed, control over individual pages, or a method that works the same on any computer.</p>

<h2>Method 1: Finder Quick Actions (fastest)</h2>
<p>Since macOS Mojave, Finder can turn several files into one PDF in two clicks:</p>
<ol>
<li>Put the PDFs in the same Finder window.</li>
<li>Select them: click the first, then hold Command and click the others.</li>
<li>Control-click (or right-click) one of the selected files and choose <strong>Quick Actions → Create PDF</strong>.</li>
</ol>
<p>A new PDF appears in the same folder, usually named after the first file. Finder combines the files in the order they are listed in the window, so the easiest way to control the order is to rename them with numbers first, such as <code>1-cover.pdf</code>, <code>2-letter.pdf</code>, <code>3-references.pdf</code>, and sort by name. Quick Actions also accepts images, so you can mix photos and PDFs in one go.</p>

<h2>Method 2: Preview (best for choosing pages)</h2>
<p>Preview, the Mac’s built-in PDF viewer, lets you see every page as you assemble the document:</p>
<ol>
<li>Open the first PDF in Preview.</li>
<li>Choose <strong>View → Thumbnails</strong> so page thumbnails show in the sidebar.</li>
<li>Drag another PDF from Finder into the sidebar. Drop it between the thumbnails where you want its pages to go. A line shows where they will land.</li>
<li>Repeat for any other files, and drag individual thumbnails up or down to reorder pages.</li>
<li>Choose <strong>File → Export as PDF</strong> and save under a new name.</li>
</ol>
<p>You can also add a whole file with <strong>Edit → Insert → Page from File</strong>. To remove a page, select its thumbnail and press Delete. Exporting to a new name keeps your original files unchanged, which is safer than saving over them.</p>
<p>One common snag: if you drag a file onto a thumbnail rather than between thumbnails, Preview may annotate the page instead of inserting new pages. If that happens, press Command-Z and drop the file in the gap between two pages.</p>

<h2>Method 3: A browser tool (works on any Mac, iPad or PC)</h2>
<p>If you prefer a simple list where you can reorder whole files with buttons, use <a href="/merge-pdf">Merge PDF</a> in Safari or Chrome. Choose the files, arrange them, click Merge and download. The PDFs are combined inside your browser and are not uploaded, so it is fine for personal documents. This method is also handy on a shared or work Mac where you would rather not change files in Finder.</p>

<h2>Which method should you use?</h2>
<ul>
<li><strong>Quick Actions</strong> when you just need everything in one file, fast.</li>
<li><strong>Preview</strong> when you need to drop specific pages, rearrange individual pages or check each page.</li>
<li><strong>A browser tool</strong> when you want the same steps on every device, or Finder and Preview are giving you trouble.</li>
</ul>

<h2>Removing or adding pages after combining</h2>
<p>Combined files often include pages you don’t need, such as blank backs of scanned sheets or terms-and-conditions pages from a statement. In Preview, select those thumbnails and press Delete. In a browser, <a href="/delete-pdf-pages">Delete PDF Pages</a> lets you click the pages to remove. To slot an extra page into the middle of a document, use <a href="/add-pages-to-pdf">Add Pages to PDF</a> and choose the position.</p>

<h2>Troubleshooting</h2>
<ul>
<li><strong>“Create PDF” is missing from Quick Actions.</strong> Open System Settings, search for “Extensions”, and make sure Create PDF is enabled under Finder extensions.</li>
<li><strong>The file is password-protected.</strong> Open it in Preview with the password, then use File → Export as PDF to save an unlocked copy you are allowed to edit.</li>
<li><strong>The combined file is too large to email.</strong> Large scanned pages are usually the cause. Rescanning at a lower resolution, or rebuilding from compressed photos, makes the biggest difference.</li>
<li><strong>Pages are in the wrong order.</strong> In Preview, drag thumbnails into place before exporting; with Quick Actions, rename the files with numbers and try again.</li>
</ul>
"""),
dict(
slug="how-to-merge-two-pdfs-into-one", date="2026-10-24",
title="How to Merge 2 PDFs Into 1 (Free, in Under a Minute)",
desc="The quickest free ways to combine two PDF files into one on Windows, Mac, iPhone and Android, plus how to put pages in the right order.",
tools=["merge-pdf", "add-pages-to-pdf"],
body="""
<p>Combining two PDFs is one of the most common document chores: a résumé and a cover letter, a form and its signature page, two halves of a scan, or a statement and a receipt. It should take less than a minute. Here is the fastest way on each device, and how to make sure the pages end up in the right order.</p>

<h2>The one-minute method (any device)</h2>
<ol>
<li>Open <a href="/merge-pdf">Merge PDF</a> in your browser.</li>
<li>Tap “Choose PDF files” and select both PDFs.</li>
<li>Check the order. The file at the top becomes the first pages. Use the arrow to swap them if needed.</li>
<li>Tap “Merge PDFs”, then “Download merged PDF”.</li>
</ol>
<p>That’s it. The two files are joined inside your browser, so nothing is uploaded, and every page keeps its original quality.</p>

<h2>On Windows</h2>
<p>Windows doesn’t include a feature that joins existing PDFs. The free Adobe Acrobat Reader app can view and sign PDFs, but combining files is part of Adobe’s paid Acrobat plans. A browser tool is the simplest free option: open <a href="/merge-pdf">Merge PDF</a> in Edge or Chrome, select both files from File Explorer, and merge.</p>

<h2>On a Mac</h2>
<p>Select both files in Finder, Control-click and choose <strong>Quick Actions → Create PDF</strong>. Or open the first file in Preview, show thumbnails (View → Thumbnails), drag the second file into the sidebar below the last page, and choose File → Export as PDF. Our guide to <a href="/blog/how-to-combine-pdf-files-on-mac">combining PDFs on a Mac</a> covers both methods in detail.</p>

<h2>On iPhone or iPad</h2>
<p>Save both PDFs to the Files app, tap the “…” button and choose Select, tap the two files, then tap “…” at the bottom and choose <strong>Create PDF</strong>. The new file appears in the same folder.</p>

<h2>On Android</h2>
<p>Most Android phones don’t include a built-in way to merge PDFs. Open <a href="/merge-pdf">Merge PDF</a> in Chrome, choose the two files from Downloads or Google Drive, and merge them there.</p>

<h2>Getting the order right</h2>
<p>Most mistakes come from the order of the pages, not the merge itself. A few habits help:</p>
<ul>
<li><strong>Decide what the reader should see first.</strong> For applications, that is usually the cover letter or the form, followed by supporting documents.</li>
<li><strong>Check the first and last page after merging.</strong> Scroll through the new PDF before you send it.</li>
<li><strong>Need the second file in the middle of the first?</strong> Merging only joins files end to end. To insert pages after, say, page 3, use <a href="/add-pages-to-pdf">Add Pages to PDF</a> and choose “After page 3”.</li>
</ul>

<h2>Merging two pages onto one sheet</h2>
<p>Some people searching for this actually want two pages printed side by side on one sheet of paper. That is a printing setting rather than a merge: in your PDF viewer’s Print dialog, look for “Pages per sheet” or “Multiple” and choose 2. If you need it as a file, print to PDF with that setting.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Will the merged file be bigger?</strong> It will be about the size of both files added together, since pages are copied as they are.</li>
<li><strong>Can I merge a PDF with a photo?</strong> Yes. Convert the photo with <a href="/jpg-to-pdf">JPG to PDF</a> first, or use Add Pages to PDF, which accepts images directly.</li>
<li><strong>What if one file is password-protected?</strong> Open it with the password and save an unlocked copy first. Merging tools cannot read locked files.</li>
</ul>
"""),
dict(
slug="how-to-add-a-page-to-a-pdf", date="2026-10-24",
title="How to Add a Page to a PDF Document (iPhone, Mac, Windows, Android)",
desc="Step-by-step ways to add a page to a PDF on any device: insert pages from another PDF, add a photo as a page, or slip in a blank page, all for free.",
tools=["add-pages-to-pdf", "merge-pdf", "delete-pdf-pages"],
body="""
<p>You have a PDF that is almost right. A signed page needs to go back into a contract, a scan is missing page 4, or an application wants a photo of your ID attached after the form. You don’t need to rebuild the document. You only need to insert the page where it belongs.</p>
<p>Here is how to add a page to a PDF on every common device, with free methods only.</p>

<h2>The quick way on any device</h2>
<ol>
<li>Open <a href="/add-pages-to-pdf">Add Pages to PDF</a> in your browser.</li>
<li>Choose the PDF you want to add to.</li>
<li>Choose the page or pages to insert. These can be other PDFs, or JPG, PNG and WebP photos.</li>
<li>Pick where they go: at the beginning, at the end, or after a page number you choose.</li>
<li>Tap “Add pages” and download the new PDF.</li>
</ol>
<p>The work happens inside your browser, so the document is never uploaded to a server. That matters when the PDF is a contract, a tax form or anything with personal details on it. Your original file stays untouched; you get a new copy with the extra pages.</p>

<h2>On a Mac (Preview)</h2>
<p>Preview, the PDF viewer built into every Mac, can insert pages without any extra software.</p>
<ol>
<li>Open the PDF in Preview and choose <strong>View → Thumbnails</strong> to show the page sidebar.</li>
<li>Click the thumbnail of the page you want the new page to follow.</li>
<li>Choose <strong>Edit → Insert → Page from File</strong> to add pages from another PDF, or <strong>Edit → Insert → Blank Page</strong> for an empty page.</li>
<li>Choose <strong>File → Save</strong> (or File → Export as PDF to keep the original as it was).</li>
</ol>
<p>You can also drag another PDF straight from Finder into the thumbnail sidebar and drop it between two pages. If you need to join several whole files instead, see our guide to <a href="/blog/how-to-combine-pdf-files-on-mac">combining PDF files on a Mac</a>.</p>

<h2>On iPhone or iPad (Files app)</h2>
<ol>
<li>Save the PDF to the Files app and open it.</li>
<li>Show the page thumbnails. On iPhone, turn the phone sideways or swipe in from the left edge; on iPad they usually appear on the left.</li>
<li>Touch and hold the thumbnail of the page the new one should follow.</li>
<li>Choose <strong>Insert Blank Page</strong>, <strong>Insert from File</strong> (to add pages from another PDF), or <strong>Scan Pages</strong> to photograph a paper page with the camera.</li>
<li>Tap Done. The change is saved to the file.</li>
</ol>
<p>The exact menu names can vary slightly between iOS versions. If you don’t see them, the browser method above works in Safari on any iPhone.</p>

<h2>On Windows</h2>
<p>Windows can open PDFs in Microsoft Edge, but Edge can’t insert pages into one. The free Adobe Acrobat Reader app can’t either; organizing and inserting pages is part of Adobe’s paid Acrobat plans. The simplest free route is a browser tool: open <a href="/add-pages-to-pdf">Add Pages to PDF</a> in Edge or Chrome, pick your files from File Explorer, and choose where the pages go.</p>

<h2>On Android</h2>
<p>Most Android phones can view PDFs but have no built-in way to edit their pages. Open <a href="/add-pages-to-pdf">Add Pages to PDF</a> in Chrome, choose your PDF from Downloads or Google Drive, then add pages from another file or straight from your photo gallery.</p>

<h2>Adding a photo or scan as a page</h2>
<p>A common case is attaching a photo: an ID card, a receipt, or a signed page you photographed with your phone. Add Pages to PDF accepts images directly. Each picture becomes one page, sized to match the first page of your document, so a photo added to a US Letter PDF becomes a US Letter page with the image scaled to fit. Phone photos keep the rotation the camera recorded, so they won’t come out sideways.</p>
<p>For the clearest result, photograph the page flat, in good light, from straight above. If you have several photos to turn into a document of their own, <a href="/jpg-to-pdf">JPG to PDF</a> is quicker.</p>

<h2>Adding a page vs merging PDFs</h2>
<p>Both tools combine pages, but they do different jobs:</p>
<ul>
<li><strong>Add pages</strong> when the new page has to go in a specific spot inside an existing document, such as after page 3.</li>
<li><strong><a href="/merge-pdf">Merge PDFs</a></strong> when you want to join whole files end to end, such as a cover letter followed by a résumé.</li>
</ul>
<p>And if the problem is an extra page rather than a missing one, <a href="/delete-pdf-pages">Delete PDF Pages</a> lets you click the pages to remove.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Will adding a page reduce the quality of the rest?</strong> No. Existing pages are copied as they are, so text stays sharp and searchable.</li>
<li><strong>Can I add a page to a password-protected PDF?</strong> Not until it’s unlocked. Open it with the password, save an unprotected copy, and add pages to that.</li>
<li><strong>Can I add a page to a PDF that has form fields?</strong> Yes, but if you plan to fill in the form, fill it in first and save, then add pages to the completed copy.</li>
<li><strong>How do I add page numbers after inserting pages?</strong> That’s a separate step. Many PDF editors have an “add page numbers” option; if your document came from Word or Google Docs, it’s often easier to number it there and export again.</li>
</ul>
"""),
dict(
slug="how-much-stone-do-i-need", date="2026-10-24",
title="How Much Stone Do I Need for a Driveway, Patio or Path?",
desc="Worked examples for how much gravel or crushed stone to order for driveways, patio bases, garden paths and French drains, plus how gravel is priced by the ton.",
tools=["gravel-calculator", "cubic-yard-calculator", "concrete-calculator"],
body="""
<p>Order too little stone and the delivery truck has to come back, often with a second delivery fee. Order too much and you’re left with a pile in the yard. The good news is that working out the right amount takes three measurements and one formula. Below are real examples for the most common projects, so you can see the numbers before you call a supplier.</p>

<h2>The formula</h2>
<div class="formula">Cubic yards = length (ft) × width (ft) × depth (inches ÷ 12) ÷ 27<br>Tons = cubic yards × tons per cubic yard</div>
<p>Depth is the part people get wrong. It has to be in feet before you multiply, so 4 inches is 0.333 ft, 3 inches is 0.25 ft and 2 inches is 0.167 ft. Dividing by 27 turns cubic feet into cubic yards, because a cubic yard is 3 × 3 × 3 feet.</p>
<p>Most gravel and crushed stone weighs around 1.4 tons per cubic yard, though it ranges from roughly 1.3 to 1.7 depending on the stone size and how wet it is. Ask your supplier for the figure for the product you’re buying. Then add about 10% for compaction and uneven ground.</p>
<p>Our <a href="/gravel-calculator">gravel calculator</a> does all of this for you, including the extra and the cost. The examples below show how it works.</p>

<h2>Example 1: a gravel driveway</h2>
<p>A single-car driveway 50 feet long and 10 feet wide, 4 inches deep:</p>
<ul>
<li>50 × 10 × 0.333 = 166.7 cubic feet</li>
<li>166.7 ÷ 27 = 6.17 cubic yards</li>
<li>6.17 × 1.4 = 8.6 tons</li>
<li>With 10% extra: about <strong>9.5 tons</strong></li>
</ul>
<p>Four inches works for topping up an existing driveway. A brand-new driveway on bare soil usually needs more, built in layers: a coarse base stone first, then a finer top layer that packs down. On clay or soft ground, or where heavy vehicles park, a deeper base and landscape fabric underneath help prevent ruts.</p>

<h2>Example 2: a base for a paver patio</h2>
<p>A 12 × 12 ft patio with a 4-inch compacted base:</p>
<ul>
<li>12 × 12 × 0.333 = 48 cubic feet</li>
<li>48 ÷ 27 = 1.78 cubic yards</li>
<li>1.78 × 1.4 = 2.5 tons</li>
<li>With 10% extra: about <strong>2.75 tons</strong></li>
</ul>
<p>Paver bases often go to 4 to 6 inches in colder climates, plus a thin layer of sand on top for setting the pavers. If you plan to pour a slab instead, use the <a href="/concrete-calculator">concrete calculator</a> for the concrete and this method for the stone underneath.</p>

<h2>Example 3: a garden path</h2>
<p>A path 30 feet long and 3 feet wide, 2 inches deep:</p>
<ul>
<li>30 × 3 × 0.167 = 15 cubic feet</li>
<li>15 ÷ 27 = 0.56 cubic yards</li>
<li>0.56 × 1.4 = 0.78 tons</li>
<li>With 10% extra: just under <strong>1 ton</strong></li>
</ul>
<p>Small jobs like this are often cheaper in bags from a garden center, or as a half-yard scoop from a landscape yard if you have a truck or trailer.</p>

<h2>Example 4: a French drain</h2>
<p>A trench 40 feet long, 1 foot wide and 18 inches deep:</p>
<ul>
<li>40 × 1 × 1.5 = 60 cubic feet</li>
<li>60 ÷ 27 = 2.2 cubic yards</li>
<li>2.2 × 1.4 = 3.1 tons</li>
</ul>
<p>A 4-inch perforated pipe in that trench takes up only about 3.5 cubic feet, so it barely changes the order. Drains need clean, washed stone with no fine dust, so water can flow through the gaps.</p>

<h2>How far does a ton go?</h2>
<p>At 1.4 tons per cubic yard, one ton of gravel is about 19 cubic feet. Spread out, that covers:</p>
<table>
<thead><tr><th>Depth</th><th>Area one ton covers</th></tr></thead>
<tbody>
<tr><td>2 inches</td><td>about 115 sq ft</td></tr>
<tr><td>3 inches</td><td>about 77 sq ft</td></tr>
<tr><td>4 inches</td><td>about 58 sq ft</td></tr>
<tr><td>6 inches</td><td>about 39 sq ft</td></tr>
</tbody>
</table>

<h2>Which stone for which job</h2>
<ul>
<li><strong>Crusher run</strong> (also sold as road base or dense grade aggregate) mixes stone with fine dust. It packs down hard, which makes it a good base for driveways and patios. It drains slowly, so don’t use it for drainage.</li>
<li><strong>Clean crushed stone</strong>, such as #57 stone at roughly ¾ to 1 inch, has no fines. Water runs through it, so it suits French drains, behind retaining walls and the top layer of many driveways.</li>
<li><strong>Pea gravel</strong> is small and rounded. It’s comfortable underfoot for paths and play areas, but it rolls and shifts, so it’s a poor choice for driveways and slopes unless it’s held in by edging or grid panels.</li>
<li><strong>River rock</strong> is larger and smooth, mostly used for decoration and around downspouts.</li>
</ul>
<p>Names vary between regions, so describe the job to the supplier and ask what they recommend.</p>

<h2>How gravel is priced</h2>
<p>Landscape yards and quarries sell stone by the ton, by the cubic yard, or both. Prices depend heavily on the type of stone and where you live, so there’s no single national price worth quoting. What to ask when you call:</p>
<ul>
<li>The price per ton or per yard for the exact product.</li>
<li>The weight per cubic yard, so you can convert between the two.</li>
<li>The delivery fee and any minimum order. Delivery often costs as much as the stone on small orders.</li>
<li>How many tons the truck carries, so a large order doesn’t need two trips.</li>
</ul>
<p>Once you have a price, the math is simple. If a supplier charges, say, $45 a ton, the 9.5-ton driveway above comes to about $430 for the stone, plus delivery. Enter your own price in the <a href="/gravel-calculator">gravel calculator</a> to get the total.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Is it better to buy by the ton or by the yard?</strong> Neither is cheaper by itself. Convert one to the other using the weight per yard, then compare suppliers on the same basis.</li>
<li><strong>Should I order extra?</strong> Yes, about 10%. Stone compacts as it’s spread and rolled, and few yards are perfectly level. Running short costs more than a small leftover pile.</li>
<li><strong>How do I measure an irregular area?</strong> Break it into rectangles, work out each one, and add them together. For a round area, multiply the radius by itself and by 3.14 to get the square feet.</li>
<li><strong>What about dirt, mulch or topsoil?</strong> Those are usually sold by the cubic yard. Use the <a href="/cubic-yard-calculator">cubic yard calculator</a> and skip the tons step.</li>
</ul>
"""),
dict(
slug="how-to-calculate-roofing-squares", date="2026-10-24",
title="How to Calculate Roofing Squares and Shingle Bundles (With Examples)",
desc="Learn what a roofing square is, how to measure your roof from the ground, how roof pitch changes the area, and how many bundles of shingles to buy.",
tools=["roofing-calculator", "percentage-calculator"],
body="""
<p>Roofers don’t talk in square feet. They price jobs, order shingles and compare quotes in <strong>squares</strong>. Knowing how to work out the number of squares on your own roof helps you check a contractor’s quote, plan a DIY reroof or order the right amount of shingles for a shed. You can do it from the ground, without climbing a ladder.</p>

<h2>What is a roofing square?</h2>
<p>One roofing square is <strong>100 square feet</strong> of roof surface. A roof with 2,000 square feet of surface is a 20-square roof. Standard asphalt shingles are packed so that <strong>three bundles cover one square</strong>, although some heavier architectural shingles need four or more, so always check the wrapper.</p>

<h2>Step 1: measure the footprint</h2>
<p>Measure the length and width of the house, then add the overhang on each side, because the eaves are roofed too. An overhang of around 1 foot is common. You can measure along the walls with a tape, take the dimensions from the house plans, or measure the roof outline on an online satellite map.</p>
<div class="formula">Footprint = (length + 2 × overhang) × (width + 2 × overhang)</div>
<p>Example: a 40 × 30 ft house with a 1 ft overhang has a footprint of 42 × 32 = 1,344 square feet.</p>

<h2>Step 2: find the roof pitch</h2>
<p>Pitch is how many inches the roof rises for every 12 inches it runs horizontally. A 6/12 roof rises 6 inches per foot. The easiest way to measure it is from inside the attic: hold a level horizontally against the underside of a rafter, mark 12 inches along the level, and measure straight up from that mark to the rafter. That measurement in inches is the rise. Many US homes fall between 4/12 and 9/12.</p>

<h2>Step 3: apply the pitch multiplier</h2>
<p>A sloped roof has more surface than the ground it covers. The steeper it is, the bigger the difference. Multiply the footprint by the pitch multiplier:</p>
<table>
<thead><tr><th>Pitch</th><th>Multiplier</th><th>Pitch</th><th>Multiplier</th></tr></thead>
<tbody>
<tr><td>3/12</td><td>1.031</td><td>8/12</td><td>1.202</td></tr>
<tr><td>4/12</td><td>1.054</td><td>9/12</td><td>1.250</td></tr>
<tr><td>5/12</td><td>1.083</td><td>10/12</td><td>1.302</td></tr>
<tr><td>6/12</td><td>1.118</td><td>12/12</td><td>1.414</td></tr>
<tr><td>7/12</td><td>1.158</td><td></td><td></td></tr>
</tbody>
</table>
<p>The multiplier comes from the Pythagorean theorem: √(1 + (rise ÷ 12)²). For our example, 1,344 × 1.118 = about 1,503 square feet of roof.</p>

<h2>Step 4: convert to squares and add waste</h2>
<p>Divide the roof area by 100: 1,503 ÷ 100 = 15.0 squares. Then add a waste allowance, because shingles are cut at edges, valleys and ridges:</p>
<ul>
<li><strong>About 10%</strong> for a simple gable roof (two sloped sides).</li>
<li><strong>About 15%</strong> for a hip roof, where all four sides slope and more cutting is needed.</li>
<li><strong>Up to 20%</strong> for complex roofs with dormers, valleys and several levels.</li>
</ul>
<p>Our gable example becomes 15.0 × 1.10 = 16.5 squares. Round up to <strong>17 squares</strong>.</p>

<h2>Step 5: work out the bundles</h2>
<p>At three bundles per square, 16.5 squares × 3 = 49.6, so buy <strong>50 bundles</strong>. Starter strips and ridge cap shingles are usually separate products, sold by the linear foot they cover, so measure the eaves, rakes and ridges and add those to the order.</p>
<p>The <a href="/roofing-calculator">roofing calculator</a> runs all five steps at once: enter the footprint, overhang, pitch and waste, and it gives you the roof area, squares and bundles.</p>

<h2>What else to measure</h2>
<ul>
<li><strong>Underlayment</strong> goes under the shingles and is sold in rolls labeled with the number of squares they cover. Divide your squares by that number.</li>
<li><strong>Drip edge</strong> runs along the eaves and rakes and is sold in lengths, commonly 10 feet.</li>
<li><strong>Ridge vents, flashing and nails</strong> depend on the roof design; a supplier can work these out from your squares and roof shape.</li>
</ul>

<h2>Using squares to check a quote</h2>
<p>Contractors often quote a price per square, which makes quotes easy to compare once you know your own number. If two quotes list very different square counts for the same roof, ask how each one measured it; the difference usually comes from the pitch or the waste allowance. NerdWallet’s roof cost guide puts asphalt shingle roofs at roughly $4.25 to $12.25 per square foot installed, which is about $425 to $1,225 per square, with labor making up around 60% of the total. Local prices vary a lot, so treat that as a rough check rather than a target.</p>
<p>To compare quotes as a percentage difference, the <a href="/percentage-calculator">percentage calculator</a> helps.</p>

<h2>Common questions</h2>
<ul>
<li><strong>How many squares is a 2,000 sq ft house?</strong> It depends on the pitch and overhang, not just the floor area. A single-story 2,000 sq ft home with a 6/12 roof and 1 ft overhangs usually has roughly 24 to 25 squares before waste. A two-story house with the same floor area has a much smaller footprint, and so fewer squares.</li>
<li><strong>How much does one bundle of shingles cover?</strong> About 33.3 square feet for most standard shingles, which is why three make a square.</li>
<li><strong>Do I measure each side of the roof separately?</strong> For simple gable and hip roofs, the footprint-and-pitch method gives the same answer with less work. Measure separately when sections have different pitches.</li>
<li><strong>Is it safe to measure on the roof?</strong> Measuring from the ground or the attic avoids the risk. If you do go up, use proper fall protection, and never climb a wet or steep roof.</li>
</ul>
"""),
dict(
slug="how-to-calculate-cubic-yards", date="2026-10-25",
title="How to Calculate Cubic Yards of Dirt, Mulch and Topsoil",
desc="A simple way to work out cubic yards for dirt, mulch, topsoil and fill, with worked examples for raised beds, garden beds, lawns and holes, plus how many bags make a yard.",
tools=["cubic-yard-calculator", "gravel-calculator", "concrete-calculator"],
body="""
<p>Landscape yards sell dirt, mulch, topsoil and compost by the cubic yard, but nobody measures a garden in yards. You measure in feet and inches, so you need a quick way to turn those measurements into the number a supplier asks for. It takes one formula and about a minute.</p>

<h2>What a cubic yard is</h2>
<p>A cubic yard is a cube 3 feet long, 3 feet wide and 3 feet high. That’s 3 × 3 × 3 = <strong>27 cubic feet</strong>. Picture a box a little bigger than a washing machine. Every cubic yard calculation comes down to finding the cubic feet and dividing by 27.</p>

<h2>The formula</h2>
<div class="formula">Cubic yards = length (ft) × width (ft) × depth (ft) ÷ 27</div>
<p>The step that trips people up is depth. Beds and lawns are measured in inches, so divide the inches by 12 first: 3 inches is 0.25 ft, 4 inches is 0.333 ft, 6 inches is 0.5 ft. If you multiply by 3 instead of 0.25, the answer comes out twelve times too big.</p>
<p>The <a href="/cubic-yard-calculator">cubic yard calculator</a> takes length, width and depth in any units and does the conversion for you. The examples below show the math by hand.</p>

<h2>Example 1: soil for a raised bed</h2>
<p>An 8 × 4 ft raised bed, 12 inches deep:</p>
<ul>
<li>8 × 4 × 1 = 32 cubic feet</li>
<li>32 ÷ 27 = <strong>1.19 cubic yards</strong></li>
</ul>
<p>Fresh, loose soil settles after watering, often by 10% to 20%. Order about 1.3 to 1.4 yards, or plan to top up after the first few weeks.</p>

<h2>Example 2: mulch for a garden bed</h2>
<p>A bed covering 200 square feet, mulched 3 inches deep:</p>
<ul>
<li>200 × 0.25 = 50 cubic feet</li>
<li>50 ÷ 27 = <strong>1.85 cubic yards</strong></li>
</ul>
<p>Two to three inches of mulch is a common depth for keeping weeds down and holding moisture. Keep it pulled back a few inches from tree trunks and plant stems.</p>

<h2>Example 3: topsoil for a new lawn</h2>
<p>A 1,000 sq ft lawn area with 4 inches of new topsoil:</p>
<ul>
<li>1,000 × 0.333 = 333 cubic feet</li>
<li>333 ÷ 27 = <strong>12.3 cubic yards</strong></li>
</ul>
<p>That’s a full truckload, which is why bulk delivery makes sense for lawns. Topdressing an existing lawn uses far less, since it’s spread only about a quarter to half an inch thick.</p>

<h2>Example 4: filling a hole</h2>
<p>A hole 3 feet long, 3 feet wide and 3 feet deep is exactly <strong>1 cubic yard</strong>, because it’s the same shape as the definition. If you’re filling a hole where a tree stump was removed, add a little extra and tamp the dirt down in layers so it doesn’t sink later.</p>

<h2>Round and odd-shaped areas</h2>
<ul>
<li><strong>Circle:</strong> area = 3.14 × radius × radius. A round bed 10 feet across has a radius of 5 ft, so 3.14 × 5 × 5 = 78.5 sq ft. At 3 inches of mulch: 78.5 × 0.25 = 19.6 cu ft, or 0.73 cubic yards.</li>
<li><strong>Triangle:</strong> area = base × height ÷ 2.</li>
<li><strong>Irregular shapes:</strong> split them into rectangles, circles and triangles, work out each one, and add them together. Rounding up slightly covers the curves.</li>
</ul>

<h2>Bags or bulk?</h2>
<p>Garden centers sell mulch and soil in bags measured in cubic feet. To see how many bags equal one cubic yard, divide 27 by the bag size:</p>
<table>
<thead><tr><th>Bag size</th><th>Bags per cubic yard</th></tr></thead>
<tbody>
<tr><td>0.75 cu ft</td><td>36</td></tr>
<tr><td>1 cu ft</td><td>27</td></tr>
<tr><td>1.5 cu ft</td><td>18</td></tr>
<tr><td>2 cu ft</td><td>13.5</td></tr>
<tr><td>3 cu ft</td><td>9</td></tr>
</tbody>
</table>
<p>The mulch bed in Example 2 needs 25 bags of 2 cubic feet. For a job much over a cubic yard or two, bulk delivery is usually cheaper and saves a lot of lifting, though it often comes with a delivery fee and a minimum order.</p>

<h2>Dirt vs gravel vs concrete</h2>
<p>Dirt, mulch, topsoil and compost are sold by volume, so cubic yards are all you need. Gravel and stone are often sold by weight, so you’ll need to convert yards to tons; our guide on <a href="/blog/how-much-stone-do-i-need">how much stone you need</a> and the <a href="/gravel-calculator">gravel calculator</a> handle that. For concrete, the <a href="/concrete-calculator">concrete calculator</a> gives both cubic yards and the number of bags.</p>

<h2>Common questions</h2>
<ul>
<li><strong>How many square feet does a cubic yard cover?</strong> 324 sq ft at 1 inch deep, 162 sq ft at 2 inches, 108 sq ft at 3 inches and 81 sq ft at 4 inches.</li>
<li><strong>How much does a cubic yard of dirt weigh?</strong> Usually around a ton or more, depending on the soil and how wet it is. Check that a pickup or trailer can carry it before you collect a load yourself.</li>
<li><strong>Will a cubic yard fit in a pickup truck?</strong> Many full-size pickups can hold a cubic yard by volume, but a yard of wet soil can be heavier than the truck is rated to carry. Ask the supplier, and check your truck’s payload.</li>
<li><strong>Should I round up?</strong> Yes. Suppliers usually sell in half or whole yards, and running short means a second delivery fee.</li>
</ul>
"""),
dict(
slug="how-to-convert-decimal-to-percent", date="2026-10-25",
title="How to Convert a Decimal to a Percent (and a Percent to a Decimal)",
desc="Convert decimals to percents and back in one step, turn fractions into percents, and work out what percentage one number is of another, with clear examples.",
tools=["percentage-calculator", "discount-calculator"],
body="""
<p>Decimals and percents are two ways of writing the same thing. 0.25 and 25% both mean a quarter. Once you see that a percent is just “per hundred”, converting between them takes one step in either direction.</p>

<h2>Decimal to percent: multiply by 100</h2>
<p>To turn a decimal into a percent, multiply by 100 and add the % sign. In practice, that means moving the decimal point <strong>two places to the right</strong>.</p>
<table>
<thead><tr><th>Decimal</th><th>Move the point</th><th>Percent</th></tr></thead>
<tbody>
<tr><td>0.25</td><td>0.25 → 25.</td><td>25%</td></tr>
<tr><td>0.6</td><td>0.60 → 60.</td><td>60%</td></tr>
<tr><td>0.075</td><td>0.075 → 7.5</td><td>7.5%</td></tr>
<tr><td>0.004</td><td>0.004 → 0.4</td><td>0.4%</td></tr>
<tr><td>1.5</td><td>1.50 → 150.</td><td>150%</td></tr>
</tbody>
</table>
<p>When there aren’t enough digits, add zeros: 0.6 becomes 0.60, which becomes 60%. A decimal bigger than 1 gives a percent over 100%, which is normal for things like growth: 1.5 times as many is 150% of the original.</p>

<h2>Percent to decimal: divide by 100</h2>
<p>Going the other way, divide by 100, which means moving the decimal point <strong>two places to the left</strong> and dropping the % sign.</p>
<ul>
<li>45% → 0.45</li>
<li>8% → 0.08</li>
<li>12.5% → 0.125</li>
<li>0.5% → 0.005</li>
<li>200% → 2</li>
</ul>
<p>You need this step whenever a percent goes into a formula. A 6.5% interest rate is 0.065 in a loan formula, and a 7% sales tax means multiplying a price by 0.07.</p>

<h2>Fraction to percent</h2>
<p>Divide the top number by the bottom number to get a decimal, then multiply by 100.</p>
<ul>
<li>3/8 = 3 ÷ 8 = 0.375 = 37.5%</li>
<li>2/5 = 0.4 = 40%</li>
<li>1/3 = 0.333… ≈ 33.3%</li>
</ul>
<p>A few are worth remembering because they come up all the time: 1/2 = 50%, 1/4 = 25%, 3/4 = 75%, 1/5 = 20%, 1/10 = 10%.</p>

<h2>What percentage is X of Y?</h2>
<p>This is the same idea in a different form. Divide the part by the whole, then multiply by 100.</p>
<div class="formula">Percentage = (part ÷ whole) × 100</div>
<ul>
<li>18 correct answers out of 24: 18 ÷ 24 = 0.75, so <strong>75%</strong>.</li>
<li>45 minutes out of an hour: 45 ÷ 60 = 0.75, so <strong>75%</strong>.</li>
<li>$12 saved on a $80 jacket: 12 ÷ 80 = 0.15, so <strong>15% off</strong>.</li>
</ul>
<p>The order matters. The “whole” is the number you’re comparing against, and it always goes on the bottom. The <a href="/percentage-calculator">percentage calculator</a> handles this and the other common percent questions, including percent change between two numbers.</p>

<h2>Common mistakes</h2>
<ul>
<li><strong>Moving the point the wrong way.</strong> A quick check: a percent number is always 100 times bigger than its decimal. If 0.08 turned into 0.0008%, the point went the wrong way.</li>
<li><strong>Treating 0.5% as 50%.</strong> 0.5% is half of one percent, which is 0.005 as a decimal. This matters with interest rates and fees.</li>
<li><strong>Mixing up percent and percentage points.</strong> If a rate goes from 4% to 6%, it rose 2 percentage points, but that’s a 50% increase in the rate itself.</li>
<li><strong>Adding percents that apply one after another.</strong> 20% off and then another 10% off is 28% off in total, not 30%, because the second discount applies to the already-reduced price. The <a href="/discount-calculator">discount calculator</a> works out stacked discounts for you.</li>
</ul>

<h2>Quick reference</h2>
<table>
<thead><tr><th>Fraction</th><th>Decimal</th><th>Percent</th></tr></thead>
<tbody>
<tr><td>1/100</td><td>0.01</td><td>1%</td></tr>
<tr><td>1/20</td><td>0.05</td><td>5%</td></tr>
<tr><td>1/10</td><td>0.1</td><td>10%</td></tr>
<tr><td>1/8</td><td>0.125</td><td>12.5%</td></tr>
<tr><td>1/5</td><td>0.2</td><td>20%</td></tr>
<tr><td>1/4</td><td>0.25</td><td>25%</td></tr>
<tr><td>1/3</td><td>0.333…</td><td>33.3%</td></tr>
<tr><td>1/2</td><td>0.5</td><td>50%</td></tr>
<tr><td>2/3</td><td>0.666…</td><td>66.7%</td></tr>
<tr><td>3/4</td><td>0.75</td><td>75%</td></tr>
<tr><td>1</td><td>1</td><td>100%</td></tr>
</tbody>
</table>
<p>For working out percentages without a calculator, see our <a href="/blog/percentage-tricks-mental-math">six mental math tricks for percentages</a>.</p>
"""),
dict(
slug="how-to-calculate-chronological-age", date="2026-10-25",
title="How to Calculate Chronological Age (Years, Months and Days)",
desc="Step-by-step method for calculating chronological age for school testing, assessments and records, including how to borrow months and days, with worked examples.",
tools=["age-calculator", "date-difference-calculator"],
body="""
<p>Chronological age is simply how old someone is, measured exactly from their date of birth to a given date. It sounds trivial, but in schools, speech therapy, psychology and pediatrics it has to be precise to the month and day, because test scores are compared with children of the same age. A mistake of one month can shift a score.</p>
<p>Here is how to calculate it by hand, how to handle the borrowing step, and how to check your answer.</p>

<h2>How it’s written</h2>
<p>Chronological age (often shortened to CA) is written as years, months and days. Testing forms usually record it as years and months with a semicolon or hyphen: <strong>8;3</strong> or <strong>8-3</strong> means 8 years and 3 months. Don’t write it as a decimal: 8.3 years is not the same as 8 years 3 months.</p>

<h2>The method</h2>
<p>Write the test date on top and the date of birth underneath, as year, month and day. Then subtract each column, starting with the days.</p>
<table>
<thead><tr><th></th><th>Year</th><th>Month</th><th>Day</th></tr></thead>
<tbody>
<tr><td>Test date</td><td>2026</td><td>10</td><td>25</td></tr>
<tr><td>Date of birth</td><td>2018</td><td>6</td><td>12</td></tr>
<tr><td><strong>Chronological age</strong></td><td><strong>8</strong></td><td><strong>4</strong></td><td><strong>13</strong></td></tr>
</tbody>
</table>
<p>25 − 12 = 13 days, 10 − 6 = 4 months, 2026 − 2018 = 8 years. The child is 8 years, 4 months and 13 days old, recorded as 8;4.</p>

<h2>When you need to borrow</h2>
<p>If the day or month on the bottom is bigger than the one on top, borrow from the next column, just like subtraction with numbers:</p>
<ul>
<li><strong>Days too small:</strong> take 1 from the months column and add the days of a month to the days column. Many test manuals tell you to add <strong>30 days</strong>.</li>
<li><strong>Months too small:</strong> take 1 from the years column and add <strong>12 months</strong> to the months column.</li>
</ul>
<p>Example with both: test date October 5, 2026, birth date December 20, 2019.</p>
<table>
<thead><tr><th></th><th>Year</th><th>Month</th><th>Day</th></tr></thead>
<tbody>
<tr><td>Test date</td><td>2026</td><td>10</td><td>5</td></tr>
<tr><td>After borrowing</td><td>2025</td><td>21</td><td>35</td></tr>
<tr><td>Date of birth</td><td>2019</td><td>12</td><td>20</td></tr>
<tr><td><strong>Chronological age</strong></td><td><strong>6</strong></td><td><strong>9</strong></td><td><strong>15</strong></td></tr>
</tbody>
</table>
<p>The 5 days are smaller than 20, so borrow a month: 10 months becomes 9, and 5 days becomes 35. Then 9 months is smaller than 12, so borrow a year: 2026 becomes 2025, and 9 months becomes 21. Now subtract: 35 − 20 = 15 days, 21 − 12 = 9 months, 2025 − 2019 = 6 years. The age is 6 years, 9 months and 15 days, recorded as 6;9.</p>

<h2>Should you round the days?</h2>
<p>It depends on the test. Some manuals say to ignore the days and never round up; others say to round up to the next month when the days are 15 or more. In the example above, that rule would give 6;10 instead of 6;9. Always follow the instructions for the specific assessment you’re scoring, because the norm tables were built using that rule.</p>

<h2>Checking your answer</h2>
<p>Hand calculations are easy to slip on, especially when borrowing twice. Check with the <a href="/age-calculator">age calculator</a>: enter the date of birth, then set “Age on this date” to the test date. It gives years, months and days instantly.</p>
<p>It counts real calendar months rather than a fixed 30 days, so when the birthday falls near the end of a month, its answer can differ from the 30-day method by a day or two. If the two disagree, use the method your test manual specifies.</p>
<p>For the total number of days or weeks between two dates, for example to track time between assessments, use the <a href="/date-difference-calculator">date difference calculator</a>.</p>

<h2>Adjusted age for premature babies</h2>
<p>For babies born early, pediatricians and therapists often also use an adjusted (or corrected) age: the chronological age minus the number of weeks the baby was born early. A baby born 8 weeks early who is 6 months old has an adjusted age of about 4 months. Adjusted age is commonly used for development checks in the first two to three years; your child’s doctor or therapist will say which age to use.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Is chronological age the same as birthday age?</strong> Yes in meaning, but more precise. “Seven” on a birthday card could be anywhere from 7;0 to 7;11, while chronological age pins it down to the month and day.</li>
<li><strong>What about leap years?</strong> Counting by calendar dates handles them automatically. A child born on February 29 still gains one year of age each year.</li>
<li><strong>Why not just count total days and divide?</strong> Months have different lengths, so dividing days by 30 or 365 gives slightly wrong results. The column method, or a calendar-based calculator, avoids that.</li>
</ul>
"""),
dict(
slug="how-to-remove-metadata-from-photos", date="2026-10-25",
title="How to Remove Metadata from Photos (iPhone, Android, Windows, Mac)",
desc="Photos can reveal where you live and what phone you use. Here’s how to check and remove location and EXIF metadata on any device before you share.",
tools=["image-metadata-remover", "image-compressor"],
body="""
<p>Open the details of almost any photo taken on a phone and you’ll find more than you expected: the exact GPS coordinates where it was taken, the date and time to the second, the phone model, and sometimes the owner’s name. This hidden information is called metadata, and it travels with the file whenever you email it, send it as a document, or upload it somewhere that doesn’t strip it.</p>
<p>Here’s how to see what your photos reveal and remove it on every common device.</p>

<h2>The quickest way on any device</h2>
<ol>
<li>Open the <a href="/image-metadata-remover">Image Metadata Remover</a> in your browser.</li>
<li>Choose one or more photos. The report shows what each one contains, with GPS location and serial numbers highlighted.</li>
<li>Download the clean copies.</li>
</ol>
<p>The photos are processed on your own device and never uploaded. Only the hidden data is removed, so the picture keeps its full quality, and portrait photos still display the right way up.</p>

<h2>On iPhone</h2>
<ul>
<li><strong>Remove location when sharing:</strong> in Photos, select the picture, tap Share, tap <strong>Options</strong> at the top, and turn off <strong>Location</strong>. This applies to that share only.</li>
<li><strong>Remove location from the photo itself:</strong> open the photo, swipe up to see its details, tap <strong>Adjust</strong> next to the location, and choose <strong>No Location</strong>.</li>
<li><strong>Stop recording location:</strong> go to Settings → Privacy &amp; Security → Location Services → Camera and choose <strong>Never</strong>.</li>
</ul>
<p>These options handle location, but not the camera model, date or other fields. For a fully clean file, use the browser tool above in Safari. iPhones save photos as HEIC by default; set Settings → Camera → Formats → <strong>Most Compatible</strong> to save JPGs instead, which every tool can clean.</p>

<h2>On Android</h2>
<ul>
<li><strong>Stop recording location:</strong> open your Camera app’s settings and turn off the option usually called <strong>Location tags</strong> or <strong>Save location</strong>. The name varies by phone maker.</li>
<li><strong>In Google Photos:</strong> look in Settings → Sharing for an option to remove geo location from items you share by link.</li>
<li><strong>For a fully clean copy:</strong> open the <a href="/image-metadata-remover">metadata remover</a> in Chrome and pick the photos from your gallery.</li>
</ul>

<h2>On Windows</h2>
<ol>
<li>Right-click the photo in File Explorer and choose <strong>Properties</strong>.</li>
<li>Open the <strong>Details</strong> tab and click <strong>Remove Properties and Personal Information</strong> at the bottom.</li>
<li>Choose <strong>Create a copy with all possible properties removed</strong>, or pick individual fields to remove.</li>
</ol>
<p>This works well for JPG files. It can’t touch every type of metadata, such as some XMP blocks added by editing apps, so check the result if privacy really matters.</p>

<h2>On a Mac</h2>
<ul>
<li><strong>Preview:</strong> open the photo, choose Tools → Show Inspector, click the <strong>(i)</strong> tab, open <strong>GPS</strong>, and click <strong>Remove Location Info</strong>. This removes location only.</li>
<li><strong>Photos app:</strong> when exporting (File → Export), untick the option to include location information.</li>
</ul>

<h2>What photo metadata can reveal</h2>
<table>
<thead><tr><th>Field</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>GPS location</td><td>Can pinpoint your home, workplace or children’s school to within a few meters.</td></tr>
<tr><td>Date and time</td><td>Shows when you were at a place, or when you were away from home.</td></tr>
<tr><td>Camera model and serial number</td><td>Can link different photos back to the same device.</td></tr>
<tr><td>Owner or artist name</td><td>Some cameras and editing apps write your name into every file.</td></tr>
<tr><td>Editing history and software</td><td>Reveals which apps touched the image and sometimes the original file name.</td></tr>
<tr><td>AI prompts</td><td>Images from Stable Diffusion and similar tools often store the full prompt and settings.</td></tr>
</tbody>
</table>

<h2>Don’t social networks remove it anyway?</h2>
<p>Many large platforms strip location and most EXIF data when you upload a photo, but you can’t count on it everywhere. Email attachments, files shared as documents in messaging apps, cloud-storage links, forum uploads and marketplace listings frequently keep the original file, metadata included. Cleaning photos yourself before sharing is the only way to be sure.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Does removing metadata change the photo?</strong> Not with a lossless tool. The <a href="/image-metadata-remover">metadata remover</a> copies the image data unchanged. Screenshots and re-saving in an editor also drop metadata, but they re-compress the image.</li>
<li><strong>Should businesses remove metadata from website images?</strong> It’s good practice. It removes staff names and locations, and slightly reduces file size. For bigger savings, also run images through the <a href="/image-compressor">image compressor</a>.</li>
<li><strong>Can metadata be recovered after removal?</strong> Not from the clean copy. It’s gone from that file, though your original still has it.</li>
</ul>
"""),
dict(
slug="what-are-meta-tags", date="2026-10-25",
title="What Are Meta Tags? The Ones That Matter for SEO (With Examples)",
desc="A plain-English guide to meta tags: what they are, which ones affect Google rankings and clicks, which to ignore, and copy-ready examples.",
tools=["meta-tag-generator", "serp-preview-tool", "seo-checker"],
body="""
<p>Meta tags are snippets of HTML in the <code>&lt;head&gt;</code> section of a web page. Visitors never see them on the page, but search engines, browsers and social networks read them to understand the page and decide how to show it. A handful of them shape how your site appears in Google and how your links look when they’re shared. Most of the rest are optional or obsolete.</p>

<h2>The meta tags that matter</h2>
<h3>1. Title tag</h3>
<pre class="formula">&lt;title&gt;Free Mortgage Calculator – Monthly Payment with Taxes&lt;/title&gt;</pre>
<p>Technically not a meta tag, but the most important tag in the head. It’s the blue headline in search results, the text in the browser tab, and a strong signal of what the page is about. Keep it unique for every page, around 50–60 characters, with the main topic near the start.</p>

<h3>2. Meta description</h3>
<pre class="formula">&lt;meta name="description" content="Work out your monthly mortgage payment with taxes, insurance and PMI. Free, no sign-up."&gt;</pre>
<p>The short summary under the title in search results. Google says it doesn’t use descriptions as a ranking factor, but a specific, useful description persuades more people to click. Aim for about 120–160 characters. Test yours in the <a href="/serp-preview-tool">SERP preview tool</a>.</p>

<h3>3. Viewport</h3>
<pre class="formula">&lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;</pre>
<p>Tells phones to fit the page to the screen. Without it, mobile visitors see a tiny desktop layout. Google indexes the mobile version of your pages, so this one is essential.</p>

<h3>4. Robots</h3>
<pre class="formula">&lt;meta name="robots" content="noindex, follow"&gt;</pre>
<p>Only needed when you want to change the default. <code>noindex</code> keeps a page out of search results (useful for thank-you pages, internal search results and thin pages); <code>nofollow</code> asks search engines not to follow the page’s links. Pages without a robots tag are indexed and followed normally.</p>

<h3>5. Canonical link</h3>
<pre class="formula">&lt;link rel="canonical" href="https://example.com/mortgage-calculator/"&gt;</pre>
<p>Points to the preferred URL when the same content is available at several addresses, such as with tracking parameters or both www and non-www. It helps search engines combine signals onto one page.</p>

<h3>6. Charset</h3>
<pre class="formula">&lt;meta charset="utf-8"&gt;</pre>
<p>Tells the browser how to read the characters on the page, so symbols, accents and emoji display properly. Put it first in the head.</p>

<h3>7. Open Graph tags</h3>
<pre class="formula">&lt;meta property="og:title" content="Free Mortgage Calculator"&gt;
&lt;meta property="og:description" content="Monthly payment with taxes, insurance and PMI."&gt;
&lt;meta property="og:image" content="https://example.com/share.jpg"&gt;</pre>
<p>Control the preview card when a link is shared on Facebook, LinkedIn, WhatsApp, Slack and most messaging apps. They don’t affect Google rankings, but a good image and headline make shared links far more clickable.</p>

<h3>8. X (Twitter) card</h3>
<pre class="formula">&lt;meta name="twitter:card" content="summary_large_image"&gt;</pre>
<p>Tells X to show a large image preview. X falls back to your Open Graph tags for the title, description and image.</p>

<h2>Meta tags you can ignore</h2>
<ul>
<li><strong>Meta keywords:</strong> Google has ignored it for well over a decade, and it hands your keyword list to competitors.</li>
<li><strong>Revisit-after, rating, distribution, author</strong> and similar: not used by Google for ranking.</li>
<li><strong>Language meta tags:</strong> declare the language with <code>&lt;html lang="en"&gt;</code> instead, and use hreflang links for translated versions.</li>
</ul>

<h2>How to add meta tags</h2>
<ul>
<li><strong>Hand-coded sites:</strong> paste the tags inside <code>&lt;head&gt;</code>. The <a href="/meta-tag-generator">meta tag generator</a> writes them for you with live previews.</li>
<li><strong>WordPress:</strong> an SEO plugin such as Yoast SEO, Rank Math or All in One SEO adds title, description, canonical and Open Graph fields to every post.</li>
<li><strong>Shopify, Wix and Squarespace:</strong> use the “SEO” or “Search engine listing” section in each page’s settings.</li>
</ul>

<h2>How to check a page’s meta tags</h2>
<p>Right-click the page and choose “View page source”, then look between <code>&lt;head&gt;</code> and <code>&lt;/head&gt;</code>. Or run the page through the <a href="/seo-checker">SEO checker</a>, which reads the title, description, robots, canonical, Open Graph and X tags and flags anything missing or too long.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Do meta tags improve rankings?</strong> The title tag helps search engines understand the page. The description, Open Graph and X tags mainly improve clicks. Robots and canonical tags prevent problems rather than boost rankings.</li>
<li><strong>Why doesn’t Google show my meta description?</strong> Google picks its own snippet when it thinks page text answers the search better. That’s normal; a good description is still used for many queries.</li>
<li><strong>How many meta tags should a page have?</strong> There’s no target number. The eight above cover almost every site.</li>
</ul>
"""),
dict(
slug="title-tag-and-meta-description-length", date="2026-10-25",
title="Meta Title Length and Meta Description Length: 2026 Guide",
desc="What is the ideal meta title length and meta description length? The limits Google uses in characters and pixels, and how to write titles that don’t get cut off.",
tools=["serp-preview-tool", "meta-tag-generator"],
body="""
<p>How long should a meta title be? Write a title that’s too long and Google cuts it off with “…”, often right before the words that matter. Write one that’s too short and you waste space that could persuade someone to click. Here are the lengths that work, and why the real limit is measured in pixels rather than characters.</p>

<h2>The short answer</h2>
<table>
<thead><tr><th></th><th>Aim for</th><th>Google shows up to about</th></tr></thead>
<tbody>
<tr><td>Title tag</td><td>50–60 characters</td><td>600 pixels on desktop</td></tr>
<tr><td>Meta description (desktop)</td><td>120–160 characters</td><td>920 pixels</td></tr>
<tr><td>Meta description (mobile)</td><td>Key message in the first 120 characters</td><td>About 680 pixels</td></tr>
</tbody>
</table>
<p>These are guides, not hard rules. Google doesn’t publish official limits and adjusts its layout from time to time. Test your own text in the <a href="/serp-preview-tool">SERP preview tool</a>, which measures it in pixels.</p>

<h2>Why pixels matter more than characters</h2>
<p>Search results have a fixed width, so Google truncates text when it runs out of room. Letters have different widths: a capital W takes up several times the space of a lowercase i. A 55-character title in narrow letters fits easily; a 50-character title full of capitals and wide letters may not.</p>
<p>Compare:</p>
<ul>
<li><em>“Illinois little-league fields list”</em>: narrow letters, fits comfortably.</li>
<li><em>“WOW! MEGA HOME MAKEOVER WORKBOOK”</em>: fewer characters, but capitals make it far wider.</li>
</ul>
<p>Avoid writing titles in all capitals. Besides looking shouty, they get cut off much sooner.</p>

<h2>How to write a title tag that fits</h2>
<ol>
<li><strong>Start with the topic.</strong> Put the main keyword in the first few words, where it’s never truncated.</li>
<li><strong>Add the benefit or detail that earns the click:</strong> “free”, a year, a number, or the specific result.</li>
<li><strong>Put your brand at the end, if at all.</strong> “ – SmartToolsy” is the first thing to be cut, which is fine.</li>
<li><strong>Use separators sparingly.</strong> One dash or pipe is enough.</li>
<li><strong>Make every title unique</strong>, so Google can tell your pages apart.</li>
</ol>
<p>Example: <em>“Roofing Calculator – Roof Area, Squares & Shingle Bundles”</em> puts the keyword first and then answers what the tool gives you.</p>

<h2>How to write a meta description that fits</h2>
<ul>
<li>Say what the page gives the reader, in one or two plain sentences.</li>
<li>Include the main keyword naturally; Google bolds words that match the search.</li>
<li>Put the most important point in the first 120 characters so it survives on mobile.</li>
<li>End with a reason to act, such as “Free, no sign-up” or “With worked examples”.</li>
</ul>

<h2>Why Google sometimes ignores your title and description</h2>
<p>Google rewrites titles when they’re too long, stuffed with keywords, the same across many pages, or don’t match what the page is about. It often uses the page’s main heading (H1) instead, so keeping your title and H1 closely aligned reduces rewrites. Descriptions are replaced with page text even more often, whenever another passage matches the search better. You can’t prevent this completely, but clear, accurate tags are used far more often than vague or spammy ones.</p>

<h2>Checking your pages</h2>
<p>Use the <a href="/serp-preview-tool">SERP preview tool</a> to test new titles and to load the current title and description of any live page. When you’re happy, the <a href="/meta-tag-generator">meta tag generator</a> produces the HTML. To find pages with missing or overlong tags, run them through the <a href="/seo-checker">SEO checker</a>.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Is a longer title bad for SEO?</strong> Not in itself. Google still reads the whole title; it just can’t display all of it. The risk is losing important words or getting your title rewritten.</li>
<li><strong>How short is too short?</strong> Titles under about 30 characters often leave out useful detail. Use the space to describe the page fully.</li>
<li><strong>Do the limits differ on mobile?</strong> Mobile titles can wrap onto two lines, so they’re slightly more forgiving, but descriptions are shorter. Writing for desktop and front-loading the key words covers both.</li>
</ul>
"""),
dict(
slug="how-to-block-ai-crawlers-robots-txt", date="2026-10-25",
title="How to Block AI Crawlers with robots.txt (GPTBot, ClaudeBot and More)",
desc="Which AI bots crawl your site, how to block them in robots.txt, what blocking does and doesn’t do, and why you might allow AI search bots.",
tools=["robots-txt-generator", "seo-checker"],
body="""
<p>AI companies send crawlers across the web to collect text for training their models and to fetch pages when people ask AI assistants questions. If you’d rather your content wasn’t used that way, robots.txt is the standard way to say so. Here’s how to do it, and the trade-offs to think about first.</p>

<h2>Two kinds of AI crawlers</h2>
<ul>
<li><strong>Training crawlers</strong> collect pages to build and improve AI models. Blocking them asks the company not to use your content for training. You lose little or no traffic.</li>
<li><strong>Search and assistant crawlers</strong> fetch pages to answer questions in AI search tools, often with a link back to the source. Blocking them can keep your site out of those answers and cost you visitors.</li>
</ul>
<p>Many publishers block training crawlers but allow search crawlers.</p>

<h2>Common AI crawler names</h2>
<table>
<thead><tr><th>User-agent</th><th>Company</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>GPTBot</td><td>OpenAI</td><td>Model training</td></tr>
<tr><td>OAI-SearchBot</td><td>OpenAI</td><td>ChatGPT search results</td></tr>
<tr><td>ChatGPT-User</td><td>OpenAI</td><td>Pages fetched when a user asks ChatGPT</td></tr>
<tr><td>ClaudeBot</td><td>Anthropic</td><td>Model training</td></tr>
<tr><td>Google-Extended</td><td>Google</td><td>Use in Gemini models (not Google Search)</td></tr>
<tr><td>Applebot-Extended</td><td>Apple</td><td>Use in Apple’s AI models</td></tr>
<tr><td>CCBot</td><td>Common Crawl</td><td>Open web archive widely used for AI training</td></tr>
<tr><td>PerplexityBot</td><td>Perplexity</td><td>Perplexity search index</td></tr>
<tr><td>meta-externalagent</td><td>Meta</td><td>AI training and products</td></tr>
<tr><td>Bytespider</td><td>ByteDance</td><td>AI training</td></tr>
<tr><td>Amazonbot</td><td>Amazon</td><td>Alexa and AI services</td></tr>
</tbody>
</table>
<p>Companies add and rename crawlers from time to time, so check each company’s documentation for the current list.</p>

<h2>The robots.txt rules</h2>
<p>To block one crawler from the whole site, give it its own group:</p>
<pre class="formula">User-agent: GPTBot
Disallow: /</pre>
<p>To block several training crawlers while keeping normal search engines welcome, your file might look like this:</p>
<pre class="formula">User-agent: *
Disallow:

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

Sitemap: https://example.com/sitemap.xml</pre>
<p>The <a href="/robots-txt-generator">robots.txt generator</a> builds this for you with one checkbox, plus a second option for AI search crawlers.</p>

<h2>What blocking does and doesn’t do</h2>
<ul>
<li><strong>It’s a request, not a lock.</strong> Major AI companies say their crawlers respect robots.txt, but nothing technically forces a crawler to obey. Determined scrapers ignore it.</li>
<li><strong>It isn’t retroactive.</strong> Content already collected isn’t removed from existing models.</li>
<li><strong>Blocking Google-Extended doesn’t affect Google Search.</strong> According to Google, regular search crawling and ranking are handled by Googlebot, which you shouldn’t block.</li>
<li><strong>Don’t block Googlebot or Bingbot</strong> unless you want to disappear from search engines.</li>
</ul>

<h2>Should you block AI crawlers?</h2>
<p>It depends on your site. Publishers whose income depends on original writing, artists and photographers often block training crawlers. Businesses that want to be recommended by AI assistants usually allow search crawlers, since being cited in an AI answer can send visitors. A tools site or a local business gets little from blocking and may lose visibility.</p>

<h2>After you change robots.txt</h2>
<ol>
<li>Upload the file to the root of your site so it opens at <code>yourdomain.com/robots.txt</code>.</li>
<li>Open that address in a browser to confirm it’s live.</li>
<li>Run your homepage through the <a href="/seo-checker">SEO checker</a> to make sure robots.txt doesn’t accidentally block all crawlers and that your sitemap is listed.</li>
</ol>

<h2>Common questions</h2>
<ul>
<li><strong>Can I block AI from some pages only?</strong> Yes. Replace <code>Disallow: /</code> with specific folders, such as <code>Disallow: /blog/</code>.</li>
<li><strong>Is there a meta tag instead of robots.txt?</strong> Some sites use <code>noai</code> meta tags, but they aren’t an official standard and support varies. robots.txt is the widely recognised method.</li>
<li><strong>How do I know if AI bots visit my site?</strong> Check your server or CDN logs for the user-agent names in the table above.</li>
</ul>
"""),
dict(
slug="good-keyword-density-for-seo", date="2026-10-25",
title="What Is a Good Keyword Density for SEO? (And What Matters More)",
desc="Is there an ideal keyword density? What Google actually looks for, how to calculate density, how to spot keyword stuffing, and how to cover a topic properly.",
tools=["keyword-density-checker", "word-counter", "seo-checker"],
body="""
<p>Keyword density is the share of words on a page taken up by a particular keyword. It was once a popular SEO target, with advice like “use your keyword 2–3% of the time”. Search engines have moved on a long way since then. Here’s what the number means today, how to use it, and what actually helps a page rank.</p>

<h2>How keyword density is calculated</h2>
<div class="formula">Keyword density = (number of times the keyword appears × words in the keyword) ÷ total words × 100</div>
<p>If “gravel driveway” appears 5 times in a 1,000-word article: 5 × 2 ÷ 1,000 × 100 = 1%. The <a href="/keyword-density-checker">keyword density checker</a> works this out for every word and phrase on a page at once.</p>

<h2>Is there an ideal keyword density?</h2>
<p>No. Google has said for years that it doesn’t use a target keyword density, and pages don’t rank better for hitting any particular percentage. Modern search engines understand language well enough to recognise synonyms, related terms and the overall topic of a page. A page that uses a phrase naturally a few times and covers the subject thoroughly will beat one that repeats the phrase to reach a number.</p>
<p>In practice, most well-written pages end up with their main keyword somewhere around 0.5–2%, simply because that’s how often it comes up when you write naturally about a topic. That’s a result of good writing, not a goal to aim for.</p>

<h2>Keyword stuffing hurts</h2>
<p>Repeating a keyword far more than natural writing would is called keyword stuffing. Google’s spam policies name it explicitly, and it makes text unpleasant to read. Signs to watch for:</p>
<ul>
<li>One word or phrase stands far above everything else in the density table.</li>
<li>Sentences sound awkward because the exact phrase is forced in: “Our cheap plumber Dallas service is the best cheap plumber Dallas has.”</li>
<li>Lists of keywords or place names with no real purpose.</li>
</ul>
<p>Fix it by replacing some mentions with pronouns, synonyms and more specific terms.</p>

<h2>What matters more than density</h2>
<ol>
<li><strong>Put the topic in the right places.</strong> The main keyword belongs in the title tag, the H1, the first paragraph and at least one subheading. These placements matter far more than how many times it appears in total.</li>
<li><strong>Cover related subtopics.</strong> A guide to gravel driveways should also mention base layers, depth, compaction, crushed stone sizes and cost. Those related terms show you’ve covered the subject.</li>
<li><strong>Answer the questions people ask.</strong> Look at the “People also ask” box in Google for your keyword and answer those questions clearly.</li>
<li><strong>Match the search intent.</strong> Someone searching “gravel calculator” wants a calculator, not an essay. Someone searching “how much gravel do I need” wants an explanation with examples.</li>
<li><strong>Write enough to be useful.</strong> There’s no minimum word count, but thin pages rarely answer questions fully. Check yours with the <a href="/word-counter">word counter</a>.</li>
</ol>

<h2>How to use a keyword density checker well</h2>
<ul>
<li><strong>Confirm your main topic leads.</strong> If your target phrase doesn’t appear among the top terms, the page may not be clearly about it.</li>
<li><strong>Spot accidental repetition.</strong> Writers often overuse a word without noticing.</li>
<li><strong>Compare with pages that rank.</strong> Load a competitor’s page to see which related terms they use that you don’t.</li>
</ul>
<p>For a complete on-page review, including title length, headings, links and structured data, run the page through the <a href="/seo-checker">SEO checker</a>.</p>

<h2>Common questions</h2>
<ul>
<li><strong>What’s the best keyword density?</strong> There isn’t one. Write naturally, place the keyword in the title, H1 and opening, and cover the topic thoroughly.</li>
<li><strong>Does keyword density matter for Bing?</strong> Bing also warns against keyword stuffing and focuses on relevance and quality, so the same advice applies.</li>
<li><strong>Should I include the keyword in every paragraph?</strong> No. Use it where it fits; elsewhere, natural variations read better and help just as much.</li>
</ul>
"""),
dict(
slug="how-to-remove-background-from-image", date="2026-10-27",
title="How to Remove the Background from an Image (Free, No Photoshop)",
desc="Free ways to remove a photo’s background on any device, from a one-click browser tool to the built-in options on iPhone, Mac and Windows, plus tips for clean edges.",
tools=["background-remover", "image-cropper", "image-resizer"],
body="""
<p>Cutting a person or product out of a photo used to mean careful work with Photoshop’s pen tool. Today, AI does it in seconds, and several free options are already on your phone or computer. Here’s how to remove a background on each device, and how to get clean, natural-looking edges.</p>

<h2>The quickest way on any device</h2>
<ol>
<li>Open the <a href="/background-remover">Background Remover</a>.</li>
<li>Choose a photo, or paste one with Ctrl+V.</li>
<li>Pick Transparent, White or any color, and download.</li>
</ol>
<p>The AI runs in your browser, so the photo isn’t uploaded. That matters for pictures of people, IDs or products that aren’t public yet.</p>

<h2>On iPhone and iPad</h2>
<p>On recent versions of iOS, open a photo in the Photos app and touch and hold the subject. When it lifts away with a glowing outline, tap <strong>Copy</strong> or <strong>Share</strong>. You can paste the cut-out into Messages, Notes or another app. It works best with people, pets and clear objects.</p>

<h2>On a Mac</h2>
<p>Recent versions of macOS can lift subjects too. In Photos or Preview, right-click the image and choose <strong>Copy Subject</strong>. In Finder, right-click an image file and look for <strong>Quick Actions → Remove Background</strong>, which saves a new transparent PNG next to the original.</p>

<h2>On Windows</h2>
<p>The Paint app in Windows 11 has a <strong>Remove background</strong> button in the Image section of the toolbar. Open the photo in Paint, click it, and save the result as a PNG to keep the transparency.</p>

<h2>On Android</h2>
<p>Some phones include a cut-out feature in their gallery or editing app, often by touching and holding the subject, but it varies by brand. The <a href="/background-remover">browser tool</a> works the same on every Android phone in Chrome.</p>

<h2>Tips for clean edges</h2>
<ul>
<li><strong>Start with contrast.</strong> A subject that stands out from the background in color or brightness gives the cleanest cut.</li>
<li><strong>Use the sharpest, largest photo you have.</strong> Blur and low resolution create fuzzy edges.</li>
<li><strong>Watch hair and fur.</strong> Fine strands are the hardest part for any tool. A plain background behind the subject when you take the photo helps a lot.</li>
<li><strong>Pick the right file type.</strong> Save cut-outs as PNG to keep transparency. JPG fills transparent areas with a solid color.</li>
<li><strong>Finish the layout.</strong> Crop to the shape you need with the <a href="/image-cropper">image cropper</a> and set the exact size with the <a href="/image-resizer">image resizer</a>.</li>
</ul>

<h2>Product photos on a white background</h2>
<p>Many marketplaces ask for main product images on a pure white background. Remove the background, choose White, and download as JPG. Leave a little space around the product and keep the same framing across your listings so they look consistent.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Is it legal to remove the background from any image?</strong> Editing doesn’t change who owns a photo. Use your own images, or ones you have permission to edit.</li>
<li><strong>Why are there faint halos around my subject?</strong> Pixels at the edge mix the subject and the old background. Placing the cut-out on a background of similar brightness hides them, or you can erase them in an editor.</li>
<li><strong>Can I make a transparent background in JPG?</strong> No. JPG doesn’t support transparency; use PNG or WebP.</li>
</ul>
"""),
dict(
slug="how-to-resize-an-image", date="2026-10-27",
title="How to Resize an Image Without Losing Quality (Any Device)",
desc="Resize photos to exact pixels or a file size like 100 KB on Windows, Mac, iPhone and Android, without stretching or blurring them.",
tools=["image-resizer", "image-compressor", "image-cropper"],
body="""
<p>Websites, forms and social networks all want images at particular sizes. Resizing is simple once you know two rules: keep the proportions locked, and make images smaller, not bigger. Here’s how to do it on every device.</p>

<h2>The quickest way on any device</h2>
<ol>
<li>Open the <a href="/image-resizer">Image Resizer</a> and choose your image.</li>
<li>Type the new width; the height adjusts automatically.</li>
<li>If there’s a file size limit, type it in KB.</li>
<li>Download the result.</li>
</ol>

<h2>On Windows</h2>
<ul>
<li><strong>Photos app:</strong> open the image, open the “…” menu and choose <strong>Resize image</strong>, then pick a preset or enter custom dimensions.</li>
<li><strong>Paint:</strong> press Ctrl+W (Resize), choose Pixels, keep “Maintain aspect ratio” ticked, and save as a new file.</li>
</ul>

<h2>On a Mac</h2>
<p>Open the image in Preview, choose <strong>Tools → Adjust Size</strong>, make sure “Scale proportionally” is ticked, enter the width, and save. Use File → Export to save a copy in a different format or quality.</p>

<h2>On iPhone and Android</h2>
<p>Phones don’t have a simple resize option in their photo apps. Use the <a href="/image-resizer">image resizer</a> in Safari or Chrome, or on iPhone, build a short Shortcuts automation with the “Resize Image” action if you do it often.</p>

<h2>How to avoid losing quality</h2>
<ul>
<li><strong>Keep proportions locked.</strong> Changing width and height independently stretches the picture.</li>
<li><strong>Shrink, don’t enlarge.</strong> Making an image smaller keeps it sharp. Making it bigger can’t create detail, so it turns soft.</li>
<li><strong>Resize from the original</strong>, not from a copy that’s already been shrunk and compressed several times.</li>
<li><strong>Choose the right format.</strong> JPG or WebP for photos, PNG for screenshots, logos and graphics with text.</li>
<li><strong>Need a different shape?</strong> Crop first with the <a href="/image-cropper">image cropper</a>, then resize.</li>
</ul>

<h2>Resizing to a file size (KB or MB)</h2>
<p>File size depends on both dimensions and compression. To get under a limit like 100 KB, first reduce the width and height to what’s actually needed, then lower the JPG quality. The resizer does the quality step automatically when you enter a maximum size. For files that are already the right dimensions, the <a href="/image-compressor">image compressor</a> shrinks them without resizing.</p>

<h2>Common sizes</h2>
<table>
<thead><tr><th>Use</th><th>Size in pixels</th></tr></thead>
<tbody>
<tr><td>Instagram square post</td><td>1080 × 1080</td></tr>
<tr><td>Instagram portrait post</td><td>1080 × 1350</td></tr>
<tr><td>Link preview (Open Graph)</td><td>1200 × 630</td></tr>
<tr><td>YouTube thumbnail</td><td>1280 × 720</td></tr>
<tr><td>Blog content image</td><td>1200–1600 wide</td></tr>
<tr><td>2 × 2 inch photo at 300 DPI</td><td>600 × 600</td></tr>
</tbody>
</table>
<p>Platforms adjust their recommendations from time to time, so check the current guidance when it really matters.</p>

<h2>Common questions</h2>
<ul>
<li><strong>What’s the difference between resizing and compressing?</strong> Resizing changes the number of pixels; compressing keeps the pixels but stores them more efficiently. Both make files smaller.</li>
<li><strong>What does DPI mean for resizing?</strong> DPI only matters for printing. On screens, only the pixel dimensions count. For print, multiply inches by 300 to get the pixels you need.</li>
</ul>
"""),
dict(
slug="how-to-crop-a-picture", date="2026-10-27",
title="How to Crop a Picture on iPhone, Android, Windows and Mac",
desc="Step-by-step ways to crop a photo on any device, how to crop to a square or circle, and which aspect ratio to use for Instagram, YouTube and stories.",
tools=["image-cropper", "image-resizer"],
body="""
<p>Cropping removes the parts of a photo you don’t want and changes its shape: a square for a profile picture, a tall 9:16 frame for a story, or a wide 16:9 frame for a thumbnail. Every device can do it, and the steps only take a few seconds.</p>

<h2>The quickest way on any device</h2>
<ol>
<li>Open the <a href="/image-cropper">Image Cropper</a> and choose a picture.</li>
<li>Pick a shape such as 1:1, 4:5 or 16:9, or leave it on Free.</li>
<li>Drag the frame and its corners, then click “Crop and download”.</li>
</ol>
<p>Tick “Circle crop” for a round profile picture with transparent corners.</p>

<h2>On iPhone</h2>
<p>Open the photo in Photos, tap <strong>Edit</strong>, then the crop icon. Drag the corners, or tap the aspect-ratio button at the top to choose Square, 16:9, 4:5 and other shapes. Tap <strong>Done</strong>. You can undo it later with Edit → Revert.</p>

<h2>On Android</h2>
<p>In Google Photos, open the photo, tap <strong>Edit</strong>, then <strong>Crop</strong>. Drag the corners or choose an aspect ratio, then tap <strong>Save copy</strong> to keep the original. Other gallery apps have a similar Edit → Crop option.</p>

<h2>On Windows</h2>
<p>Open the image in the Photos app, click <strong>Edit image</strong> (or press Ctrl+E), and use the crop handles or the aspect-ratio menu. Save a copy so the original stays untouched. In Paint, drag a selection and click <strong>Crop</strong>.</p>

<h2>On a Mac</h2>
<p>In Preview, drag a selection over the area you want and choose <strong>Tools → Crop</strong> (Command+K). In Photos, click Edit, then Crop, where you can also choose an aspect ratio.</p>

<h2>Which shape to choose</h2>
<table>
<thead><tr><th>Ratio</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>1:1 (square)</td><td>Profile pictures, product photos, square posts</td></tr>
<tr><td>4:5</td><td>Portrait posts in Instagram feeds</td></tr>
<tr><td>9:16</td><td>Stories, Reels, TikTok and Shorts</td></tr>
<tr><td>16:9</td><td>YouTube thumbnails, slides, desktop wallpapers</td></tr>
<tr><td>3:2</td><td>Standard prints such as 4 × 6 inches</td></tr>
</tbody>
</table>

<h2>Tips for a better crop</h2>
<ul>
<li><strong>Use the rule of thirds.</strong> Place the subject’s eyes or the main object about a third of the way in, rather than dead center.</li>
<li><strong>Leave breathing room</strong> in the direction a person is looking or moving.</li>
<li><strong>Don’t crop at joints</strong> such as wrists, elbows or knees; it looks awkward.</li>
<li><strong>Crop before resizing.</strong> Get the shape right first, then set the exact size with the <a href="/image-resizer">image resizer</a>.</li>
</ul>

<h2>Common questions</h2>
<ul>
<li><strong>Does cropping reduce quality?</strong> It removes pixels outside the frame, so a heavily cropped photo has fewer pixels and may look soft when shown large.</li>
<li><strong>How do I crop a photo into a circle?</strong> Choose a square crop, tick “Circle crop” in the <a href="/image-cropper">image cropper</a>, and download the PNG.</li>
</ul>
"""),
dict(
slug="png-vs-jpg", date="2026-10-27",
title="PNG vs JPG: Which Image Format Should You Use?",
desc="The real differences between PNG and JPG: compression, transparency, file size and quality, with a simple rule for choosing the right one every time.",
tools=["png-to-jpg", "webp-to-jpg", "image-compressor"],
body="""
<p>PNG and JPG are the two most common image formats, and choosing the wrong one gives you either huge files or blurry graphics. The rule is simple once you know how each one works.</p>

<h2>The short answer</h2>
<ul>
<li><strong>Use JPG for photos:</strong> pictures from a camera or phone, with lots of colors and soft gradients.</li>
<li><strong>Use PNG for graphics:</strong> logos, icons, screenshots, charts, text, and anything that needs a transparent background.</li>
</ul>

<h2>How they compress images</h2>
<p><strong>JPG is lossy.</strong> It throws away detail the eye is unlikely to notice, which makes photos dramatically smaller. At high quality settings the loss is hard to see, but every time a JPG is edited and saved again, a little more detail is lost. Sharp edges, like text, can pick up faint smudges called artifacts.</p>
<p><strong>PNG is lossless.</strong> It keeps every pixel exactly, so text and lines stay crisp. That makes PNG files much larger for photos, often several times the size of a good JPG.</p>

<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>JPG</th><th>PNG</th></tr></thead>
<tbody>
<tr><td>Compression</td><td>Lossy</td><td>Lossless</td></tr>
<tr><td>Best for</td><td>Photos</td><td>Graphics, screenshots, text</td></tr>
<tr><td>Transparency</td><td>No</td><td>Yes</td></tr>
<tr><td>File size for photos</td><td>Small</td><td>Large</td></tr>
<tr><td>Quality after repeated saves</td><td>Gets worse</td><td>Stays the same</td></tr>
<tr><td>Support</td><td>Everywhere</td><td>Everywhere</td></tr>
</tbody>
</table>

<h2>When to convert</h2>
<ul>
<li><strong>A photo saved as PNG</strong> is usually far bigger than it needs to be. Convert it with the <a href="/png-to-jpg">PNG to JPG converter</a> to cut the size.</li>
<li><strong>A logo or screenshot saved as JPG</strong> may look fuzzy around text. Converting to PNG won’t fix lost detail, so go back to the original file if you can.</li>
<li><strong>Need transparency?</strong> Stay with PNG, or use WebP.</li>
</ul>

<h2>What about WebP?</h2>
<p>WebP is a newer format that can do both jobs: lossy compression like JPG and lossless compression with transparency like PNG, usually with smaller files. All current browsers support it, which makes it a strong choice for websites. Some older apps and upload forms still don’t accept it; the <a href="/webp-to-jpg">WebP converter</a> turns WebP files into JPG or PNG when you need to. See <a href="/blog/what-is-a-webp-file">what a WebP file is</a> for more.</p>

<h2>For websites</h2>
<p>Image size has a big effect on page speed. Use JPG or WebP for photos, PNG or SVG for logos and icons, resize images to the width they’re displayed at, and compress them with the <a href="/image-compressor">image compressor</a>.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Is JPEG the same as JPG?</strong> Yes. They’re the same format; .jpg is just a shorter file extension.</li>
<li><strong>Which is better for printing?</strong> Either works if the resolution is high enough. Use maximum-quality JPG for photos and PNG for graphics with text.</li>
<li><strong>Which is better for screenshots?</strong> PNG, because it keeps text sharp.</li>
</ul>
"""),
dict(
slug="what-is-a-webp-file", date="2026-10-27",
title="What Is a WebP File? How to Open It and Convert It to JPG",
desc="What WebP images are, why websites use them, how to open them on Windows, Mac and phones, and how to convert WebP to JPG or PNG for free.",
tools=["webp-to-jpg", "png-to-jpg"],
body="""
<p>You save an image from a website and it arrives as a .webp file, which an app or upload form then refuses to open. WebP is a modern image format that’s great for websites but still unfamiliar to some software. Here’s what it is and how to deal with it.</p>

<h2>What WebP is</h2>
<p>WebP is an image format created by Google and released in 2010. It can compress photos like JPG (lossy) or keep every pixel like PNG (lossless), and it supports transparency and animation too. Its main advantage is size: WebP images are typically noticeably smaller than JPG or PNG files of similar quality, so pages load faster. That’s why many websites now serve images as WebP.</p>

<h2>How to open a WebP file</h2>
<ul>
<li><strong>Any web browser:</strong> Chrome, Edge, Firefox and Safari all open WebP. Drag the file into a browser window.</li>
<li><strong>Windows:</strong> the Photos app opens WebP images on current versions of Windows.</li>
<li><strong>Mac:</strong> Preview and Photos open WebP on recent versions of macOS.</li>
<li><strong>iPhone and Android:</strong> current versions show WebP images in Photos and most gallery apps.</li>
</ul>
<p>The trouble usually comes later: older editing programs, some printers, and many upload forms only accept JPG or PNG.</p>

<h2>How to convert WebP to JPG or PNG</h2>
<ol>
<li>Open the <a href="/webp-to-jpg">WebP to JPG converter</a>.</li>
<li>Choose one or more WebP files.</li>
<li>Pick JPG for photos, or PNG to keep transparency.</li>
<li>Download the files individually or as a ZIP.</li>
</ol>
<p>The conversion happens in your browser, so the images aren’t uploaded. On a Mac, you can also open the file in Preview and use File → Export to save it as JPG or PNG.</p>

<h2>Should you use WebP on your own website?</h2>
<p>Usually, yes. All current major browsers support it, and smaller images help pages load faster, which improves the experience for visitors and is part of Google’s page experience signals. Many content management systems and image CDNs now create WebP versions automatically. Keep JPG or PNG copies for places that need them, such as email newsletters or downloads.</p>

<h2>WebP vs JPG vs PNG</h2>
<ul>
<li><strong>Photos on websites:</strong> WebP, or JPG if you need maximum compatibility.</li>
<li><strong>Graphics with transparency on websites:</strong> WebP or PNG.</li>
<li><strong>Sending to people, printing, uploading to forms:</strong> JPG or PNG.</li>
</ul>
<p>Our guide to <a href="/blog/png-vs-jpg">PNG vs JPG</a> explains the older two formats in more detail, and the <a href="/png-to-jpg">PNG to JPG converter</a> handles PNG files.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Why does Chrome save images as WebP?</strong> It saves whatever format the website sent, and many sites send WebP because it’s smaller.</li>
<li><strong>Is WebP lower quality than JPG?</strong> Not necessarily. At similar file sizes, WebP often looks as good or better. Converting WebP to JPG won’t improve quality, though.</li>
<li><strong>Can WebP be animated?</strong> Yes. Animated WebP files are an alternative to GIFs, usually much smaller.</li>
</ul>
"""),
dict(
slug="social-media-character-limits", date="2026-10-27",
title="Character Limits for X, Instagram, LinkedIn, YouTube and More (2026)",
desc="A quick reference of character limits for social posts, captions, bios, titles, text messages and Google snippets, plus how characters are counted.",
tools=["character-counter", "word-counter", "serp-preview-tool"],
body="""
<p>Every platform caps how much you can write, and the limits are rarely shown until you hit them. Here’s a reference for the most common ones. Check your text against all of them at once with the <a href="/character-counter">character counter</a>.</p>

<h2>Social media posts and captions</h2>
<table>
<thead><tr><th>Platform</th><th>Limit</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>X (Twitter) post</td><td>280 characters</td><td>Paid subscribers can post much longer text</td></tr>
<tr><td>Instagram caption</td><td>2,200 characters</td><td>Only the first line or two show before “more”</td></tr>
<tr><td>Facebook post</td><td>63,206 characters</td><td>Short posts usually get more engagement</td></tr>
<tr><td>LinkedIn post</td><td>3,000 characters</td><td>Text is cut after a few lines with “see more”</td></tr>
<tr><td>Pinterest pin description</td><td>500 characters</td><td>Pin titles allow 100</td></tr>
<tr><td>YouTube title</td><td>100 characters</td><td>Around 60–70 show in most layouts</td></tr>
<tr><td>YouTube description</td><td>5,000 characters</td><td>The first lines appear above “more”</td></tr>
</tbody>
</table>
<p>Platforms change their limits from time to time, so if a number matters for a campaign, check the platform’s help pages.</p>

<h2>Text messages (SMS)</h2>
<p>A single SMS holds <strong>160 characters</strong> of standard text. Longer messages are split into parts of 153 characters each and joined on the recipient’s phone. If the message contains any emoji or characters outside the basic SMS alphabet, the whole message switches to a different encoding that holds only <strong>70 characters</strong> per message (67 per part). That’s why a single emoji can double what a long text costs to send through some services.</p>

<h2>Google search snippets</h2>
<ul>
<li><strong>Title tag:</strong> about 50–60 characters, or 600 pixels wide, before Google cuts it off.</li>
<li><strong>Meta description:</strong> about 120–160 characters on desktop, less on mobile.</li>
</ul>
<p>Since Google measures pixels rather than characters, the <a href="/serp-preview-tool">SERP preview tool</a> gives a more exact answer. Our guide to <a href="/blog/title-tag-and-meta-description-length">title and meta description length</a> explains the details.</p>

<h2>How characters are counted</h2>
<ul>
<li><strong>Spaces count</strong> as characters on almost every platform.</li>
<li><strong>Line breaks count</strong> too, usually as one character each.</li>
<li><strong>Emoji</strong> may count as one or two characters depending on the platform; X, for example, counts most emoji as two.</li>
<li><strong>Links</strong> on X are shortened and counted as 23 characters, whatever their length.</li>
</ul>

<h2>Writing within the limit</h2>
<ul>
<li>Put the key message in the first line, which is often all people see before tapping “more”.</li>
<li>Cut filler words like “just”, “really” and “in order to”.</li>
<li>Use numerals instead of words for numbers.</li>
<li>Check the total in the <a href="/character-counter">character counter</a>, and the word count and reading time in the <a href="/word-counter">word counter</a>.</li>
</ul>
"""),
dict(
slug="how-to-calculate-gpa", date="2026-10-27",
title="How to Calculate Your GPA (Weighted and Unweighted, With Examples)",
desc="Step-by-step GPA calculation on the 4.0 scale with worked examples, how weighted GPA works for Honors and AP classes, and how to figure cumulative GPA.",
tools=["gpa-calculator", "percentage-calculator"],
body="""
<p>Your grade point average turns a semester of letter grades into one number. Colleges, scholarships and employers use it, so it helps to know exactly how it’s worked out. Here’s the method, with examples you can follow by hand, or let the <a href="/gpa-calculator">GPA calculator</a> do it for you.</p>

<h2>Step 1: convert each grade to points</h2>
<p>Most US schools use a 4.0 scale:</p>
<table>
<thead><tr><th>Grade</th><th>Points</th><th>Grade</th><th>Points</th></tr></thead>
<tbody>
<tr><td>A / A+</td><td>4.0</td><td>C+</td><td>2.3</td></tr>
<tr><td>A-</td><td>3.7</td><td>C</td><td>2.0</td></tr>
<tr><td>B+</td><td>3.3</td><td>C-</td><td>1.7</td></tr>
<tr><td>B</td><td>3.0</td><td>D</td><td>1.0</td></tr>
<tr><td>B-</td><td>2.7</td><td>F</td><td>0.0</td></tr>
</tbody>
</table>
<p>Some schools count A+ as 4.3, and a few don’t use plus and minus grades at all. Your transcript or student handbook will say.</p>

<h2>Step 2: multiply by credits</h2>
<p>Classes with more credits (or hours) count more. Multiply each class’s grade points by its credits to get “quality points”.</p>

<h2>Step 3: divide by total credits</h2>
<div class="formula">GPA = total quality points ÷ total credits</div>

<h2>Worked example</h2>
<table>
<thead><tr><th>Class</th><th>Grade</th><th>Credits</th><th>Quality points</th></tr></thead>
<tbody>
<tr><td>English</td><td>A (4.0)</td><td>3</td><td>12.0</td></tr>
<tr><td>Algebra II</td><td>B+ (3.3)</td><td>3</td><td>9.9</td></tr>
<tr><td>Biology</td><td>A- (3.7)</td><td>4</td><td>14.8</td></tr>
<tr><td>History</td><td>B (3.0)</td><td>3</td><td>9.0</td></tr>
<tr><td><strong>Total</strong></td><td></td><td><strong>13</strong></td><td><strong>45.7</strong></td></tr>
</tbody>
</table>
<p>45.7 ÷ 13 = <strong>3.52 GPA</strong>.</p>

<h2>Weighted GPA</h2>
<p>A weighted GPA rewards harder classes. A common system adds <strong>0.5 points for Honors</strong> and <strong>1.0 for AP or IB</strong>, so an A in AP Biology counts as 5.0. In the example above, if Biology were AP and Algebra II Honors, the quality points would rise to 45.7 + 4.0 + 1.5 = 51.2, and the weighted GPA to 51.2 ÷ 13 = <strong>3.94</strong>. Schools vary in how much weight they add and which classes qualify.</p>

<h2>Cumulative GPA</h2>
<p>To combine terms, don’t average the GPAs. Add up all quality points and all credits across every term, then divide. A student with a 3.40 over 30 credits who earns 3.52 over 13 more credits has (3.40 × 30 + 45.7) ÷ 43 = <strong>3.43</strong> overall. Enter your previous GPA and credits in the <a href="/gpa-calculator">GPA calculator</a> to see this instantly.</p>

<h2>Converting a percentage to a GPA</h2>
<p>If your school gives percentages, a common conversion is 93–100% = A, 90–92% = A-, 87–89% = B+, 83–86% = B, and so on down in roughly three-point steps. Check your school’s scale, since cut-offs differ. The <a href="/percentage-calculator">percentage calculator</a> helps turn points earned into a percentage first.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Do colleges use weighted or unweighted GPA?</strong> Many recalculate GPAs using their own method, often unweighted core classes, so it’s useful to know both.</li>
<li><strong>Can a GPA be higher than 4.0?</strong> Yes, if it’s weighted. Unweighted GPAs top out at 4.0 (or 4.3 where A+ counts extra).</li>
<li><strong>Do failed classes count?</strong> Yes. An F adds credits with zero points, pulling the average down, unless your school replaces it when you retake the class.</li>
</ul>
"""),
dict(
slug="how-to-calculate-hours-worked", date="2026-10-27",
title="How to Calculate Hours Worked (and Convert Minutes to Decimal)",
desc="How to add up hours worked from start and end times, subtract breaks, handle overnight shifts, convert minutes to decimal hours for payroll, and work out overtime.",
tools=["time-card-calculator", "salary-to-hourly"],
body="""
<p>Adding up a week of start and end times sounds easy until you hit a 7:45 start, a 30-minute lunch and a shift that ends after midnight. Here’s a reliable method, plus the minutes-to-decimal conversion every payroll system needs. The <a href="/time-card-calculator">time card calculator</a> does all of it automatically.</p>

<h2>Step 1: convert times to 24-hour format</h2>
<p>Afternoon and evening times are easier to subtract in 24-hour format: add 12 to any PM hour except 12 PM. So 5:30 PM becomes 17:30, and 9:15 PM becomes 21:15.</p>

<h2>Step 2: subtract start from end</h2>
<p>For an 8:45 to 17:30 shift: 17:30 − 8:45. Borrow an hour when the minutes don’t work: 17:30 is the same as 16:90, and 16:90 − 8:45 = <strong>8 hours 45 minutes</strong>.</p>

<h2>Step 3: subtract unpaid breaks</h2>
<p>Take off unpaid meal breaks: 8:45 − 0:30 = <strong>8 hours 15 minutes</strong>. Under US federal rules, short rest breaks (typically 5 to 20 minutes) count as paid working time, while meal breaks of 30 minutes or more when you’re fully off duty usually don’t.</p>

<h2>Overnight shifts</h2>
<p>If the end time is earlier than the start, the shift crossed midnight. Add 24 hours to the end time: 22:00 to 6:30 becomes 30:30 − 22:00 = <strong>8 hours 30 minutes</strong>.</p>

<h2>Step 4: convert minutes to decimal hours</h2>
<p>Payroll multiplies hours by a pay rate, so minutes must become fractions of an hour. Divide the minutes by 60: 15 minutes is 0.25 hours, so 8 hours 15 minutes is 8.25 hours, not 8.15.</p>
<table>
<thead><tr><th>Minutes</th><th>Decimal</th><th>Minutes</th><th>Decimal</th></tr></thead>
<tbody>
<tr><td>5</td><td>0.08</td><td>35</td><td>0.58</td></tr>
<tr><td>10</td><td>0.17</td><td>40</td><td>0.67</td></tr>
<tr><td>15</td><td>0.25</td><td>45</td><td>0.75</td></tr>
<tr><td>20</td><td>0.33</td><td>50</td><td>0.83</td></tr>
<tr><td>25</td><td>0.42</td><td>55</td><td>0.92</td></tr>
<tr><td>30</td><td>0.50</td><td>60</td><td>1.00</td></tr>
</tbody>
</table>

<h2>Step 5: total the week and work out overtime</h2>
<p>Add the decimal hours for each day. Under the federal Fair Labor Standards Act, non-exempt employees earn at least 1.5 times their regular rate for hours over 40 in a workweek. Some states have stricter rules, including daily overtime. For 44.5 hours at $20 an hour: 40 × $20 = $800, plus 4.5 × $30 = $135, for <strong>$935</strong> gross pay.</p>

<h2>Common mistakes</h2>
<ul>
<li><strong>Writing 7:30 as 7.30.</strong> Thirty minutes is 0.50 hours, so 7:30 is 7.5.</li>
<li><strong>Forgetting the overnight rule</strong> and getting a negative number.</li>
<li><strong>Subtracting paid breaks.</strong> Only unpaid time comes off.</li>
<li><strong>Rounding each day differently.</strong> Use the same rounding rule every day, or none at all.</li>
</ul>
<p>To see what an hourly wage adds up to over a year, use the <a href="/salary-to-hourly">salary to hourly calculator</a>.</p>
"""),
dict(
slug="how-much-to-tip", date="2026-10-27",
title="How Much to Tip in the US: Restaurants, Delivery, Rideshare and More",
desc="A practical guide to US tipping: typical percentages for restaurants, bars, delivery, rideshare, salons and hotels, plus how to calculate a tip quickly.",
tools=["tip-calculator", "percentage-calculator"],
body="""
<p>Tipping in the United States can feel confusing, especially with tip screens now appearing at almost every counter. Customs vary by region and by how much service you receive, but the ranges below are widely used. To work out the numbers, use the <a href="/tip-calculator">tip calculator</a>.</p>

<h2>Typical tips by service</h2>
<table>
<thead><tr><th>Service</th><th>Common tip</th></tr></thead>
<tbody>
<tr><td>Sit-down restaurant</td><td>15–20% of the bill; more for excellent service</td></tr>
<tr><td>Bartender</td><td>$1–2 per drink, or 15–20% of the tab</td></tr>
<tr><td>Food delivery</td><td>15–20%, with a few dollars as a minimum on small orders</td></tr>
<tr><td>Taxi or rideshare</td><td>15–20% of the fare</td></tr>
<tr><td>Hair salon or barber</td><td>15–20%</td></tr>
<tr><td>Hotel housekeeping</td><td>A few dollars per night, left daily</td></tr>
<tr><td>Valet parking</td><td>A few dollars when your car is returned</td></tr>
<tr><td>Counter service or coffee</td><td>Optional; many people tip a dollar or round up</td></tr>
</tbody>
</table>
<p>In many US states, restaurant servers are paid a lower base wage on the expectation that tips make up much of their income, which is why table-service tips are treated as standard rather than optional.</p>

<h2>How to calculate a tip in your head</h2>
<ul>
<li><strong>10%:</strong> move the decimal point one place left. $48.60 → $4.86.</li>
<li><strong>20%:</strong> double the 10% figure. $4.86 × 2 = $9.72, or about $10.</li>
<li><strong>15%:</strong> take 10% and add half of it. $4.86 + $2.43 = $7.29.</li>
<li><strong>18%:</strong> take 20% and subtract a tenth of 20%. $9.72 − $0.97 ≈ $8.75.</li>
</ul>
<p>Our guide to <a href="/blog/percentage-tricks-mental-math">percentages in your head</a> has more shortcuts.</p>

<h2>Before or after tax?</h2>
<p>Etiquette guides traditionally recommend tipping on the pre-tax amount, but many people tip on the total for simplicity, and the difference is small. The <a href="/tip-calculator">tip calculator</a> can do it either way.</p>

<h2>Splitting the bill</h2>
<p>Add the tip to the total first, then divide by the number of people. Rounding each share up to the nearest dollar makes paying easier and usually adds a little extra for the server.</p>

<h2>When a tip is already included</h2>
<p>Check the bill for a “service charge” or “gratuity”, which some restaurants add automatically, often for larger groups. If it’s there, an extra tip is optional. A service charge isn’t always passed to staff in the same way as a tip, so ask if you’re unsure.</p>

<h2>Common questions</h2>
<ul>
<li><strong>Do you tip on takeout?</strong> It’s optional. Many people leave around 10% or round up, especially for large or complicated orders.</li>
<li><strong>What if the service was bad?</strong> Speak to a manager about the problem. Many people still leave a reduced tip rather than none, since tips are part of servers’ pay.</li>
</ul>
"""),
dict(
slug="salary-to-hourly-wage-table", date="2026-10-27",
title="$60,000 a Year Is How Much an Hour? Salary to Hourly Table",
desc="Hourly, weekly and monthly pay for common salaries from $30,000 to $150,000, how to convert any salary yourself, and why take-home pay is lower.",
tools=["salary-to-hourly", "time-card-calculator", "percentage-calculator"],
body="""
<p>A salary of $60,000 a year works out to about <strong>$28.85 an hour</strong>, based on a standard 40-hour week for 52 weeks (2,080 hours). The table below shows the same conversion for other common salaries, and the <a href="/salary-to-hourly">salary to hourly calculator</a> handles any amount and schedule.</p>

<h2>Salary to hourly table</h2>
<p>Based on 40 hours a week, 52 weeks a year, before taxes.</p>
<table>
<thead><tr><th>Yearly</th><th>Hourly</th><th>Weekly</th><th>Every 2 weeks</th><th>Monthly</th></tr></thead>
<tbody>
<tr><td>$30,000</td><td>$14.42</td><td>$577</td><td>$1,154</td><td>$2,500</td></tr>
<tr><td>$35,000</td><td>$16.83</td><td>$673</td><td>$1,346</td><td>$2,917</td></tr>
<tr><td>$40,000</td><td>$19.23</td><td>$769</td><td>$1,538</td><td>$3,333</td></tr>
<tr><td>$45,000</td><td>$21.63</td><td>$865</td><td>$1,731</td><td>$3,750</td></tr>
<tr><td>$50,000</td><td>$24.04</td><td>$962</td><td>$1,923</td><td>$4,167</td></tr>
<tr><td>$55,000</td><td>$26.44</td><td>$1,058</td><td>$2,115</td><td>$4,583</td></tr>
<tr><td>$60,000</td><td>$28.85</td><td>$1,154</td><td>$2,308</td><td>$5,000</td></tr>
<tr><td>$65,000</td><td>$31.25</td><td>$1,250</td><td>$2,500</td><td>$5,417</td></tr>
<tr><td>$70,000</td><td>$33.65</td><td>$1,346</td><td>$2,692</td><td>$5,833</td></tr>
<tr><td>$75,000</td><td>$36.06</td><td>$1,442</td><td>$2,885</td><td>$6,250</td></tr>
<tr><td>$80,000</td><td>$38.46</td><td>$1,538</td><td>$3,077</td><td>$6,667</td></tr>
<tr><td>$90,000</td><td>$43.27</td><td>$1,731</td><td>$3,462</td><td>$7,500</td></tr>
<tr><td>$100,000</td><td>$48.08</td><td>$1,923</td><td>$3,846</td><td>$8,333</td></tr>
<tr><td>$120,000</td><td>$57.69</td><td>$2,308</td><td>$4,615</td><td>$10,000</td></tr>
<tr><td>$150,000</td><td>$72.12</td><td>$2,885</td><td>$5,769</td><td>$12,500</td></tr>
</tbody>
</table>

<h2>How to convert any salary</h2>
<div class="formula">Hourly = yearly salary ÷ (hours per week × weeks per year)</div>
<p>For the standard 2,080 hours, a quick estimate is to halve the salary and drop the last three zeros: $60,000 → $30 an hour (the exact figure is $28.85). Going the other way, double the hourly rate and add three zeros: $25 an hour → about $50,000 a year (exactly $52,000).</p>

<h2>Different schedules</h2>
<p>If you work 37.5 hours a week, $60,000 is $30.77 an hour. If an hourly job comes with two unpaid weeks off, use 50 weeks: $28.85 × 40 × 50 = $57,700 a year. Enter your own hours and weeks in the <a href="/salary-to-hourly">calculator</a>.</p>

<h2>Why your paycheck is smaller</h2>
<p>All of these figures are gross pay. Take-home pay is reduced by federal income tax, Social Security (6.2%) and Medicare (1.45%), any state and local income tax, and deductions such as health insurance and retirement contributions. Depending on your state and choices, take-home pay is often somewhere around 70–80% of gross for a single filer at these incomes, but it varies widely, so use a paycheck calculator for your state for a precise figure.</p>

<h2>Comparing a salaried and an hourly job</h2>
<ul>
<li><strong>Overtime:</strong> hourly, non-exempt workers earn 1.5× for hours over 40 a week; many salaried roles don’t.</li>
<li><strong>Benefits:</strong> health insurance, retirement matching and paid time off can be worth thousands of dollars a year.</li>
<li><strong>Actual hours:</strong> a $70,000 salary that regularly requires 50-hour weeks works out to about $26.92 an hour.</li>
</ul>
<p>To track the hours you actually work, use the <a href="/time-card-calculator">time card calculator</a>.</p>
"""),
    {
        "slug": "how-long-to-cook-a-turkey",
        "date": "2026-10-27",
        "title": "How Long to Cook a Turkey: Times by Weight, Thawing and a Thanksgiving Timeline",
        "desc": "Turkey cooking times by weight at 325°F (stuffed and unstuffed), how long to thaw it, how big a turkey to buy and a simple Thanksgiving day timeline.",
        "tools": ["turkey-calculator"],
        "body": """
<p>The turkey is the one dish that can push Thanksgiving dinner back by an hour. The good news is that the timing is predictable once you know the weight. This guide uses the USDA's roasting chart; to get times for your exact turkey and dinner time, use the <a href="/turkey-calculator">turkey calculator</a>.</p>

<h2>Turkey cooking time by weight (325°F)</h2>
<table>
<thead><tr><th>Turkey weight</th><th>Unstuffed</th><th>Stuffed</th></tr></thead>
<tbody>
<tr><td>4–8 lb (breast)</td><td>1½–3¼ hours</td><td>2½–3½ hours (6–8 lb)</td></tr>
<tr><td>8–12 lb</td><td>2¾–3 hours</td><td>3–3½ hours</td></tr>
<tr><td>12–14 lb</td><td>3–3¾ hours</td><td>3½–4 hours</td></tr>
<tr><td>14–18 lb</td><td>3¾–4¼ hours</td><td>4–4¼ hours</td></tr>
<tr><td>18–20 lb</td><td>4¼–4½ hours</td><td>4¼–4¾ hours</td></tr>
<tr><td>20–24 lb</td><td>4½–5 hours</td><td>4¾–5¼ hours</td></tr>
</tbody>
</table>
<p>Times are for a fully thawed turkey in a 325°F oven. A turkey cooked from frozen takes about 50% longer. The turkey is done when a food thermometer reads <strong>165°F</strong> in the thickest part of the breast, the innermost part of the thigh and the wing. Do not rely on the pop-up timer alone.</p>

<h2>How big a turkey do you need?</h2>
<p>Plan on about 1 pound of whole turkey per person, or 1½ pounds if you want leftovers. Count children as half a portion.</p>
<ul>
<li>6 people: an 8 to 10 lb turkey</li>
<li>8 people: 12 to 14 lb with leftovers</li>
<li>12 people: 18 to 20 lb with leftovers</li>
<li>20 or more: two medium turkeys cook more evenly than one huge one</li>
</ul>

<h2>How long to thaw a turkey</h2>
<p>Thawing is where most plans go wrong, because a large frozen turkey needs days, not hours.</p>
<table>
<thead><tr><th>Weight</th><th>In the refrigerator</th><th>In cold water</th></tr></thead>
<tbody>
<tr><td>4–12 lb</td><td>1–3 days</td><td>2–6 hours</td></tr>
<tr><td>12–16 lb</td><td>3–4 days</td><td>6–8 hours</td></tr>
<tr><td>16–20 lb</td><td>4–5 days</td><td>8–10 hours</td></tr>
<tr><td>20–24 lb</td><td>5–6 days</td><td>10–12 hours</td></tr>
</tbody>
</table>
<p>For a Thursday dinner, a 16 lb turkey should go into the fridge by Sunday. For a cold-water thaw, keep the turkey in its wrapper, cover it completely, change the water every 30 minutes and cook it as soon as it is thawed. Never thaw a turkey on the counter.</p>

<h2>A simple Thanksgiving day timeline</h2>
<p>Here is an example for a 14 lb unstuffed turkey with dinner at 4:00 PM:</p>
<ul>
<li><strong>11:25 AM:</strong> preheat the oven to 325°F.</li>
<li><strong>11:55 AM:</strong> turkey goes in.</li>
<li><strong>2:25 PM:</strong> start checking the temperature.</li>
<li><strong>3:40 PM at the latest:</strong> out of the oven at 165°F, covered loosely with foil.</li>
<li><strong>3:40–4:00 PM:</strong> let it rest about 20 minutes while you make the gravy, then carve.</li>
</ul>
<p>The resting time is not wasted: the juices settle back into the meat, and the oven is free for the sides.</p>

<h2>Tips for a juicy turkey</h2>
<ul>
<li>Pat the skin dry and season it the night before for crisper skin.</li>
<li>Roast breast-side up on a rack in a shallow pan.</li>
<li>If the breast browns too fast, cover it with a loose tent of foil.</li>
<li>Cooking the stuffing in a separate dish is quicker and easier to get to a safe 165°F.</li>
</ul>
<p>Counting down? See exactly <a href="/days-until/thanksgiving">how many days until Thanksgiving</a>.</p>
""",
    },
    {
        "slug": "how-to-make-a-christmas-budget",
        "date": "2026-10-27",
        "title": "How to Make a Christmas Budget (and Stick to It)",
        "desc": "A step-by-step way to plan Christmas spending: set a total, budget each gift, count food, travel and decorations, and save a set amount from each paycheck.",
        "tools": ["christmas-budget-calculator"],
        "body": """
<p>Holiday spending sneaks up on people because it arrives in small pieces: one more gift, a second trip to the grocery store, a last-minute shipping fee. A budget made in October or November turns that into a plan you can pay for without a January credit card shock. You can do every step below in the <a href="/christmas-budget-calculator">Christmas budget calculator</a>.</p>

<h2>1. Decide your total first</h2>
<p>Start from what you can afford, not from what you spent last year. Look at what you have saved and how many paychecks are left before December 25. Whatever you set aside from those paychecks, plus your savings, is your real budget.</p>

<h2>2. Give every person a number</h2>
<p>List everyone you buy for and put a dollar amount next to each name. A specific limit, such as $40 for a sibling or $20 for a teacher, is much easier to shop to than a vague total. Group smaller gifts together: one line for coworkers or neighbors is enough.</p>

<h2>3. Count the things that aren't gifts</h2>
<p>Gifts are often only half of holiday spending. Add a line for each of these:</p>
<ul>
<li><strong>Food and drinks:</strong> the big dinner, baking and parties.</li>
<li><strong>Travel:</strong> flights, gas and hotel nights to see family.</li>
<li><strong>Decorations:</strong> the tree, lights and replacements for anything broken.</li>
<li><strong>Cards, wrapping and shipping:</strong> small items that add up quickly, especially express postage in December.</li>
</ul>

<h2>4. Save a set amount each payday</h2>
<p>Take what you still need (planned spending minus what you have saved) and divide it by your paychecks before Christmas. For example, if you plan $900, have $200 saved and get paid every two weeks with four paydays left, that is $175 from each paycheck.</p>

<h2>5. Track as you shop</h2>
<p>Update the amounts as you buy. If one gift costs more than planned, take the difference from another line straight away so the total does not drift.</p>

<h2>Easy ways to spend less</h2>
<ul>
<li>Suggest a Secret Santa for big families or office groups, so everyone buys one gift.</li>
<li>Agree on a spending limit with friends, or swap experiences and homemade gifts.</li>
<li>Use Black Friday and Cyber Monday for gifts already on your list, not extra purchases.</li>
<li>Shop early to avoid paying for fast shipping.</li>
</ul>
<p>Keep an eye on the calendar with our <a href="/days-until/christmas">days until Christmas</a> countdown.</p>
""",
    },
    {
        "slug": "when-does-daylight-saving-time-end",
        "date": "2026-10-29",
        "title": "When Does Daylight Saving Time End in 2026? Clocks Fall Back November 1",
        "desc": "Daylight saving time ends Sunday, November 1, 2026, at 2:00 a.m. Here is when to set your clocks back, which states don't change, how it affects sleep and pay, and what's next for the Sunshine Protection Act.",
        "tools": ["time-card-calculator", "date-difference-calculator"],
        "body": """
<p><strong>Daylight saving time ends on Sunday, November 1, 2026, at 2:00 a.m. local time.</strong> At that moment clocks go back one hour to 1:00 a.m., so you get an extra hour of sleep on Saturday night. Phones, computers and most smart devices change by themselves; ovens, car clocks and wall clocks usually need to be changed by hand.</p>
<p>See exactly how long is left with our live <a href="/days-until/daylight-saving-time-ends">countdown to the end of daylight saving time</a>.</p>

<h2>The 2026 and 2027 clock change dates</h2>
<table>
<thead><tr><th>Change</th><th>Date</th><th>What happens</th></tr></thead>
<tbody>
<tr><td>Daylight saving time ends</td><td>Sunday, November 1, 2026</td><td>2:00 a.m. becomes 1:00 a.m. (fall back)</td></tr>
<tr><td>Daylight saving time starts</td><td>Sunday, March 14, 2027</td><td>2:00 a.m. becomes 3:00 a.m. (spring forward)</td></tr>
<tr><td>Daylight saving time ends</td><td>Sunday, November 7, 2027</td><td>2:00 a.m. becomes 1:00 a.m.</td></tr>
</tbody>
</table>
<p>The rule is set by federal law: daylight saving time starts on the <strong>second Sunday of March</strong> and ends on the <strong>first Sunday of November</strong>. The easy way to remember the direction is "spring forward, fall back."</p>

<h2>Do I set my clock forward or back?</h2>
<p><strong>Back.</strong> In November you set clocks back one hour. If you go to bed at 11:00 p.m. on Saturday and your alarm is set for 7:00 a.m., you will get nine hours of sleep instead of eight. Sunrise and sunset both move an hour earlier on the clock, so mornings are brighter and evenings get dark sooner.</p>
<p>Devices that set themselves: smartphones, computers, smartwatches, cable boxes and most newer cars connected to a phone. Devices to check by hand: microwaves, ovens, older car clocks, wall clocks, thermostats with schedules, and alarm clocks without Wi-Fi.</p>

<h2>Which states don't change their clocks?</h2>
<ul>
<li><strong>Hawaii</strong> stays on standard time all year.</li>
<li><strong>Arizona</strong> stays on standard time, except the <strong>Navajo Nation</strong>, which does observe daylight saving time.</li>
<li><strong>U.S. territories</strong> do not change: Puerto Rico, the U.S. Virgin Islands, Guam, the Northern Mariana Islands and American Samoa.</li>
</ul>
<p>Everyone else in the United States changes clocks on November 1. If you work with people in Arizona or Hawaii, the time difference to them shrinks by an hour until March.</p>

<h2>Is daylight saving time ending for good?</h2>
<p>Not yet. The <strong>Sunshine Protection Act</strong>, which would make daylight saving time permanent and end the twice-a-year switch, passed the U.S. House of Representatives on July 14, 2026, by 308 to 117. The Senate received it the next day and sent it to the Commerce, Science and Transportation Committee. It has not passed the Senate or been signed into law, so <strong>the clocks still fall back on November 1, 2026</strong>.</p>
<p>Many states have passed laws saying they would switch to permanent daylight time, but those only take effect if Congress allows it.</p>

<h2>How the time change affects work and pay</h2>
<p>If you work overnight on Saturday, November 1, your shift is one hour longer than usual: a shift from 10:00 p.m. to 6:00 a.m. lasts <strong>nine hours</strong>, not eight, because 1:00 a.m. to 2:00 a.m. happens twice. Hourly workers are generally paid for all hours actually worked, so check that your timesheet counts the extra hour. Our <a href="/time-card-calculator">time card calculator</a> makes it easy to add up hours and minutes for the week; just add the extra hour to the overnight shift.</p>
<p>In March it works the other way: an overnight shift is one hour shorter.</p>

<h2>Tips to adjust your sleep</h2>
<ul>
<li>The fall change is the easy one, but early risers often wake up an hour early for a few days. Go to bed 15 to 20 minutes later each night from Thursday.</li>
<li>Get outside in the morning light on Sunday and Monday; it helps reset your body clock.</li>
<li>Dark evenings arrive suddenly. Plan walks or exercise earlier in the day, and check that car headlights and porch lights work.</li>
<li>For kids and pets, shift meals and bedtime by 15 minutes a day so the change is gradual.</li>
</ul>

<h2>A good reminder for home safety</h2>
<p>Fire departments suggest using the clock change as a reminder to test smoke and carbon monoxide alarms and replace batteries if needed. It is also a good time to check the batteries in thermostats and wireless doorbells.</p>

<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What time does daylight saving time end in 2026?</summary><p>At 2:00 a.m. local time on Sunday, November 1, 2026. Clocks go back to 1:00 a.m.</p></details>
<details><summary>Do we gain or lose an hour in November?</summary><p>You gain an hour. Saturday night is 25 hours long because the hour from 1:00 to 2:00 a.m. happens twice.</p></details>
<details><summary>When does daylight saving time start again?</summary><p>On Sunday, March 14, 2027, at 2:00 a.m., when clocks move forward to 3:00 a.m.</p></details>
<details><summary>Will my phone change the time automatically?</summary><p>Yes, as long as automatic date and time is turned on in your phone's settings.</p></details>
<details><summary>Is the Sunshine Protection Act law?</summary><p>No. It passed the House in July 2026 but has not passed the Senate, so the clock changes continue for now.</p></details>
</div>
<p>Counting down to something else? See our <a href="/days-until">holiday countdowns</a>, including <a href="/days-until/thanksgiving">days until Thanksgiving</a>.</p>
""",
    },
]
