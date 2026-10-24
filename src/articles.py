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
]
