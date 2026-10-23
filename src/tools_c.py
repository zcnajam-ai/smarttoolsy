"""Tool registry part C: PDF tools and the US mortgage calculator."""

PDF_LIB = "/assets/vendor/pdf-lib.min.js"

DROP = """<label class="drop" for="{id}"><input id="{id}" type="file" accept="{accept}" {multi}>
<span class="drop-title">{title}</span><span class="drop-sub">{sub}</span></label>"""


def drop(id, accept, title, sub, multi=False):
    return DROP.format(id=id, accept=accept, title=title, sub=sub, multi="multiple" if multi else "")


PRIVACY_FAQ = """<details><summary>Are my files uploaded to a server?</summary><p>No. The files are opened and processed by JavaScript in your own browser. Nothing is sent to SmartToolsy or anyone else, which makes the tool safe for contracts, bank statements and other private documents.</p></details>"""

TOOLS_C = [
# ---------------------------------------------------------------- merge
dict(
slug="merge-pdf", name="Merge PDF", cat="pdf", ico="M+", scripts=[PDF_LIB],
title="Merge PDF Files Online Free – Combine PDFs in Your Browser",
desc="Combine multiple PDF files into one document. Drag to set the order, then download. Free, no sign-up, and your files never leave your device.",
short="Combine several PDFs into one file, in the order you choose.",
ui=drop("mp-file", "application/pdf,.pdf", "Choose PDF files", "Select two or more PDFs. You can add more afterwards.", True) + """
<ol class="file-list" id="mp-list" aria-live="polite"></ol>
<div class="btns"><button class="btn" id="mp-go" type="button" disabled>Merge PDFs</button><button class="btn ghost" id="mp-clear" type="button">Clear list</button></div>
<p id="mp-msg" class="count-note" aria-live="polite"></p>
<div class="btns" id="mp-dl-wrap" hidden><a class="btn" id="mp-dl" download="merged.pdf">Download merged PDF</a></div>
""",
content="""
<p>Merge PDF joins several PDF files into a single document. Use it to combine scanned pages, put a cover letter in front of a CV, gather invoices into one file for your accountant, or assemble chapters into a full report. You choose the order, click Merge, and download the result in seconds.</p>
<h2>How to merge PDF files</h2>
<ol>
<li>Click “Choose PDF files” and select two or more PDFs. On a computer you can hold Ctrl (or Cmd on a Mac) to pick several at once.</li>
<li>Use the arrow buttons to put the files in the order you want. The top file becomes the first pages.</li>
<li>Click “Merge PDFs”, then “Download merged PDF”.</li>
</ol>
<h2>What is kept when you merge</h2>
<p>Every page is copied exactly as it is, including text, images, fonts and page size, so you can mix A4 and US Letter pages in one file. Text stays selectable and searchable. Bookmarks and interactive form fields from the original files may not carry over, because they belong to each original document’s structure rather than its pages.</p>
<h2>Tips</h2>
<ul>
<li>If you only need some pages from a file, run it through our <a href="/split-pdf">Split PDF</a> tool first, then merge the parts.</li>
<li>Want to add photos or scans? Turn them into a PDF with <a href="/jpg-to-pdf">JPG to PDF</a> and merge that file in.</li>
<li>Very large merged files can be slow to email. Most email services limit attachments to around 20–25 MB.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
""" + PRIVACY_FAQ + """
<details><summary>Can I merge password-protected PDFs?</summary><p>Not while they are locked. Open the file in your PDF reader with the password, save or print a copy without protection, then merge that copy.</p></details>
<details><summary>Is there a limit on files or size?</summary><p>There is no fixed limit. Because merging happens in your browser, the practical limit is your device’s memory. Dozens of files and a few hundred pages work well on most computers.</p></details>
<details><summary>Does merging reduce quality?</summary><p>No. Pages are copied without being re-compressed, so they look exactly like the originals.</p></details>
</div>
"""),
# ---------------------------------------------------------------- split
dict(
slug="split-pdf", name="Split PDF", cat="pdf", ico="S/", scripts=[PDF_LIB],
title="Split PDF Online Free – Extract Pages from a PDF",
desc="Extract pages from a PDF or split it into several files by page ranges. Free, private and fast: the PDF is processed in your browser.",
short="Extract pages or split one PDF into several files.",
ui=drop("sp-file", "application/pdf,.pdf", "Choose a PDF file", "The file is opened in your browser, not uploaded.") + """
<p id="sp-info" class="count-note" aria-live="polite"></p>
<div id="sp-opts" hidden>
<div class="field"><label for="sp-ranges">Pages or ranges</label><input id="sp-ranges" type="text" placeholder="e.g. 1-3, 5, 8-10"></div>
<div class="field"><span class="lbl">Output</span>
<label class="check"><input type="radio" name="sp-mode" value="one" checked> All selected pages in one PDF</label>
<label class="check"><input type="radio" name="sp-mode" value="each"> Each range as a separate PDF</label>
<label class="check"><input type="radio" name="sp-mode" value="pages"> Every page as its own PDF</label></div>
<div class="btns"><button class="btn" id="sp-go" type="button">Split PDF</button></div>
</div>
<p id="sp-msg" class="count-note" aria-live="polite"></p>
<ul class="dl-list" id="sp-out"></ul>
""",
content="""
<p>Split PDF lets you pull out just the pages you need from a larger document, or break one PDF into several smaller files. Send only the signed page of a contract, separate a scanned bundle into individual receipts, or cut a long report into chapters.</p>
<h2>How to split a PDF</h2>
<ol>
<li>Choose a PDF. The tool shows how many pages it has.</li>
<li>Type the pages you want, using commas and dashes, such as <code>1-3, 5, 8-10</code>. Leave the box empty to use every page.</li>
<li>Pick an output: one combined file, one file per range, or one file per page.</li>
<li>Click “Split PDF” and download the files from the list.</li>
</ol>
<h2>Writing page ranges</h2>
<ul>
<li><code>4</code> takes only page 4.</li>
<li><code>2-6</code> takes pages 2 to 6, inclusive.</li>
<li><code>10-</code> takes page 10 to the end.</li>
<li><code>1, 3, 5</code> takes three separate pages. In “separate PDF” mode each becomes its own file.</li>
</ul>
<p>Pages keep their original quality, text and size. Nothing is re-compressed.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
""" + PRIVACY_FAQ + """
<details><summary>Can I reorder pages while splitting?</summary><p>Yes. Pages are taken in the order you type them, so <code>3, 1, 2</code> produces a file that starts with page 3.</p></details>
<details><summary>Why can’t I open my file?</summary><p>Password-protected PDFs must be unlocked first. Damaged files may also fail; try opening and re-saving the PDF in your reader.</p></details>
</div>
"""),
# ---------------------------------------------------------------- jpg to pdf
dict(
slug="jpg-to-pdf", name="JPG to PDF", cat="pdf", ico="J>", scripts=[PDF_LIB],
title="JPG to PDF Converter – Images to PDF Online Free",
desc="Convert JPG, PNG and WebP images into a single PDF. Set page size, orientation and margins. Free, no watermark, and nothing is uploaded.",
short="Turn photos and scans (JPG, PNG, WebP) into one PDF.",
ui=drop("jp-file", "image/jpeg,image/png,image/webp", "Choose images", "JPG, PNG or WebP. Select several to make a multi-page PDF.", True) + """
<ol class="file-list" id="jp-list" aria-live="polite"></ol>
<div class="row">
 <div class="field"><label for="jp-size">Page size</label><select id="jp-size"><option value="fit">Same as image</option><option value="a4">A4</option><option value="letter" selected>US Letter</option></select></div>
 <div class="field"><label for="jp-orient">Orientation</label><select id="jp-orient"><option value="auto">Automatic</option><option value="portrait">Portrait</option><option value="landscape">Landscape</option></select></div>
 <div class="field"><label for="jp-margin">Margin</label><select id="jp-margin"><option value="0">None</option><option value="18" selected>Small</option><option value="36">Large</option></select></div>
</div>
<div class="btns"><button class="btn" id="jp-go" type="button" disabled>Create PDF</button><button class="btn ghost" id="jp-clear" type="button">Clear list</button></div>
<p id="jp-msg" class="count-note" aria-live="polite"></p>
<div class="btns" id="jp-dl-wrap" hidden><a class="btn" id="jp-dl" download="images.pdf">Download PDF</a></div>
""",
content="""
<p>JPG to PDF turns one or more images into a PDF document. It is the quickest way to send phone photos of receipts, ID documents or handwritten notes as a single tidy file, or to submit scanned pages to a form that only accepts PDFs. PNG and WebP images work too.</p>
<h2>How to convert images to PDF</h2>
<ol>
<li>Choose your images. Each image becomes one page.</li>
<li>Reorder them with the arrow buttons if needed.</li>
<li>Choose a page size. “Same as image” keeps each page exactly the size of its photo; A4 and US Letter fit the image onto a standard sheet for printing.</li>
<li>Click “Create PDF” and download it.</li>
</ol>
<h2>Which page size should I pick?</h2>
<ul>
<li><strong>US Letter</strong> (8.5 × 11 in) is standard in the United States and Canada.</li>
<li><strong>A4</strong> (210 × 297 mm) is used almost everywhere else, including the UK, Europe, Pakistan and India.</li>
<li><strong>Same as image</strong> is best for viewing on screen, because there are no white borders.</li>
</ul>
<p>With “Automatic” orientation, wide photos are placed on landscape pages and tall photos on portrait pages, so nothing is shrunk more than necessary.</p>
<h2>Keeping file size small</h2>
<p>JPG photos are placed into the PDF without being re-compressed, so quality is preserved and the PDF is roughly the size of the images combined. If the result is too large to email, shrink the photos first with our <a href="/image-compressor">Image Compressor</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
""" + PRIVACY_FAQ + """
<details><summary>Is there a watermark?</summary><p>No. The PDF contains only your images.</p></details>
<details><summary>Can I combine the result with other PDFs?</summary><p>Yes. Use <a href="/merge-pdf">Merge PDF</a> to add it to existing documents.</p></details>
</div>
"""),
# ---------------------------------------------------------------- pdf to jpg
dict(
slug="pdf-to-jpg", name="PDF to JPG", cat="pdf", ico="P>", scripts=[],
title="PDF to JPG Converter – Save PDF Pages as Images Online",
desc="Convert each page of a PDF into a high-quality JPG or PNG image. Choose resolution and pages. Free, private, and works in your browser.",
short="Save PDF pages as high-quality JPG or PNG images.",
ui=drop("pj-file", "application/pdf,.pdf", "Choose a PDF file", "Each page will be turned into an image.") + """
<div class="row">
 <div class="field"><label for="pj-fmt">Format</label><select id="pj-fmt"><option value="image/jpeg">JPG</option><option value="image/png">PNG</option></select></div>
 <div class="field"><label for="pj-dpi">Quality</label><select id="pj-dpi"><option value="96">Screen (96 DPI)</option><option value="150" selected>Standard (150 DPI)</option><option value="300">Print (300 DPI)</option></select></div>
 <div class="field"><label for="pj-pages">Pages (optional)</label><input id="pj-pages" type="text" placeholder="All pages, or e.g. 1-3, 6"></div>
</div>
<div class="btns"><button class="btn" id="pj-go" type="button" disabled>Convert to images</button></div>
<p id="pj-msg" class="count-note" aria-live="polite"></p>
<div class="thumbs" id="pj-out"></div>
""",
content="""
<p>PDF to JPG converts the pages of a PDF into image files. Use it to post a page of a brochure on social media, put a slide into a presentation, attach a page to a chat app that does not preview PDFs, or keep a picture of a ticket on your phone. Choose JPG for small files or PNG for crisp text and diagrams.</p>
<h2>How to convert a PDF to images</h2>
<ol>
<li>Choose a PDF file.</li>
<li>Pick JPG or PNG and a quality level.</li>
<li>Optionally type the pages you want, such as <code>1-3, 6</code>. Leave it empty for every page.</li>
<li>Click “Convert to images” and download each page from the previews.</li>
</ol>
<h2>Choosing the right quality</h2>
<p>PDF pages are measured in points (1/72 of an inch), so the image size depends on the DPI you choose. A US Letter page at 150 DPI becomes about 1275 × 1650 pixels, which is sharp on any screen. Choose 300 DPI only if you plan to print the image, because the files are four times larger.</p>
<h2>JPG or PNG?</h2>
<ul>
<li><strong>JPG</strong> gives much smaller files and is ideal for pages with photos.</li>
<li><strong>PNG</strong> keeps text and lines perfectly sharp and is better for documents, charts and slides, at the cost of larger files.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
""" + PRIVACY_FAQ + """
<details><summary>How is the PDF rendered?</summary><p>Pages are drawn with PDF.js, the open-source PDF engine built by Mozilla and used in the Firefox browser, so results match what you see in a normal PDF viewer.</p></details>
<details><summary>Can I convert a PDF with many pages?</summary><p>Yes. Pages are processed one at a time. Very long documents at 300 DPI may take a little while on older phones.</p></details>
</div>
"""),
# ---------------------------------------------------------------- mortgage
dict(
slug="mortgage-calculator", name="Mortgage Calculator", cat="calc", ico="$h",
title="Mortgage Calculator with Taxes, Insurance & PMI (PITI)",
desc="Estimate your monthly mortgage payment including property tax, homeowners insurance, PMI and HOA. See total interest, payoff date and a yearly amortization schedule.",
short="Monthly payment with taxes, insurance, PMI and HOA.",
ui="""
<div class="row">
 <div class="field"><label for="mg-price">Home price ($)</label><input id="mg-price" type="number" min="0" step="1000" value="400000"></div>
 <div class="field"><label for="mg-down">Down payment</label><div class="split"><input id="mg-down" type="number" min="0" step="1" value="20" aria-label="Down payment amount"><select id="mg-down-u" aria-label="Down payment unit"><option value="pct">%</option><option value="usd">$</option></select></div></div>
 <div class="field"><label for="mg-rate">Interest rate (%)</label><input id="mg-rate" type="number" min="0" step="0.01" value="6.5"></div>
 <div class="field"><label for="mg-term">Loan term</label><select id="mg-term"><option value="30" selected>30 years</option><option value="20">20 years</option><option value="15">15 years</option><option value="10">10 years</option></select></div>
</div>
<details class="more" open><summary class="lbl">Taxes, insurance and fees</summary>
<div class="row">
 <div class="field"><label for="mg-tax">Property tax (% of price per year)</label><input id="mg-tax" type="number" min="0" step="0.01" value="1.1"></div>
 <div class="field"><label for="mg-ins">Home insurance ($ per year)</label><input id="mg-ins" type="number" min="0" step="50" value="1800"></div>
 <div class="field"><label for="mg-pmi">PMI (% of loan per year)</label><input id="mg-pmi" type="number" min="0" step="0.05" value="0.6"></div>
 <div class="field"><label for="mg-hoa">HOA ($ per month)</label><input id="mg-hoa" type="number" min="0" step="10" value="0"></div>
</div>
<div class="row">
 <div class="field"><label for="mg-start">First payment</label><input id="mg-start" type="month"></div>
 <div class="field"><label for="mg-extra">Extra principal ($ per month)</label><input id="mg-extra" type="number" min="0" step="25" value="0"></div>
</div>
</details>
<div class="result" id="mg-out" aria-live="polite"></div>
<details id="mg-sched-wrap" hidden style="margin-top:14px"><summary class="lbl" style="cursor:pointer">Yearly amortization schedule</summary><div id="mg-sched" style="overflow-x:auto"></div></details>
""",
content="""
<p>This mortgage calculator estimates your full monthly house payment, not just the loan. It adds property tax, homeowners insurance, private mortgage insurance (PMI) and HOA dues to principal and interest, so you see the number that will actually leave your bank account each month. It also shows the total interest over the life of the loan, your payoff date, when PMI should drop off, and how extra payments can save you years of interest.</p>

<h2>How to use the mortgage calculator</h2>
<ol>
<li>Enter the home price and your down payment, either as a percentage or a dollar amount.</li>
<li>Enter the interest rate you have been quoted and choose the loan term.</li>
<li>Adjust property tax, insurance and HOA to match the homes you are looking at. Listing pages and county tax websites show local figures.</li>
<li>Optionally add an extra monthly principal payment to see how much sooner you could be mortgage-free.</li>
</ol>
<p>The results update as you type. Open the yearly schedule to see how your balance falls over time.</p>

<h2>What makes up a mortgage payment (PITI)</h2>
<p>Lenders often describe a house payment as <strong>PITI</strong>:</p>
<ul>
<li><strong>Principal</strong> – the part that pays down what you borrowed.</li>
<li><strong>Interest</strong> – what the lender charges for the loan.</li>
<li><strong>Taxes</strong> – property tax, usually collected monthly into an escrow account and paid to your county once or twice a year.</li>
<li><strong>Insurance</strong> – homeowners insurance, also usually paid through escrow.</li>
</ul>
<p>On top of PITI, many buyers also pay PMI and HOA dues. This calculator includes all of them.</p>

<h2>The mortgage payment formula</h2>
<p>Principal and interest for a fixed-rate mortgage are calculated with the standard amortization formula:</p>
<div class="formula">M = P × r × (1 + r)<sup>n</sup> ÷ ((1 + r)<sup>n</sup> − 1)</div>
<p><strong>P</strong> is the loan amount, <strong>r</strong> is the monthly interest rate (annual rate ÷ 12 ÷ 100) and <strong>n</strong> is the number of monthly payments (360 for a 30-year loan). For example, a $320,000 loan at 6.5% for 30 years gives a principal-and-interest payment of about $2,023 a month. Early in the loan most of that goes to interest; by the final years almost all of it goes to principal.</p>

<h2>What is PMI and when does it go away?</h2>
<p>On a conventional loan, lenders usually require private mortgage insurance when your down payment is less than 20% of the home’s price. PMI protects the lender, not you, and commonly costs somewhere around 0.3% to 1.5% of the loan amount per year, depending on your credit score and down payment.</p>
<p>Under the US Homeowners Protection Act, you can ask your lender to cancel PMI once your balance reaches 80% of the home’s original value, and it must end automatically when the balance is scheduled to reach 78%. The calculator shows the month that 78% point is reached on your schedule. FHA loans work differently and use their own mortgage insurance premium, which this calculator does not model.</p>

<h2>15-year vs 30-year mortgage</h2>
<p>A 30-year term gives the lowest monthly payment, which makes a home more affordable month to month. A 15-year term has a higher payment but usually a lower interest rate, and you pay far less interest overall because the balance is repaid twice as fast. Try both terms above with the rates you are quoted: the difference in total interest is often more than the price of a car.</p>

<h2>How much house can I afford?</h2>
<p>A common guideline is the <strong>28/36 rule</strong>: keep your total housing payment at or below 28% of your gross monthly income, and all monthly debt payments (housing, car, student loans, credit cards) at or below 36%. If your household earns $9,000 a month before tax, that suggests a housing payment of up to about $2,520. Lenders may approve more than this, but staying within the guideline leaves room for savings, repairs and emergencies.</p>

<h2>Ways to lower your mortgage cost</h2>
<ul>
<li><strong>Improve your credit score</strong> before applying; better scores usually mean lower rates and cheaper PMI.</li>
<li><strong>Compare at least three lenders.</strong> Rates and fees vary, and a quarter of a percentage point adds up over decades.</li>
<li><strong>Put down 20% if you can</strong> to avoid PMI altogether.</li>
<li><strong>Pay a little extra principal.</strong> Use the extra payment box to see the effect; even $100 a month can shave years off a 30-year loan.</li>
<li><strong>Shop for insurance</strong> each year and appeal your property tax assessment if it looks too high.</li>
</ul>

<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Does this include closing costs?</summary><p>No. Closing costs are paid once at purchase, typically a few percent of the loan amount, and do not change the monthly payment unless you roll them into the loan.</p></details>
<details><summary>What interest rate should I enter?</summary><p>Use a rate quoted by a lender for your credit profile, or today’s average rate from a reputable source as a starting estimate. Rates change daily, so update the number when you get real quotes.</p></details>
<details><summary>Is this for fixed-rate or adjustable-rate mortgages?</summary><p>It calculates a fixed-rate loan. For an adjustable-rate mortgage (ARM), the result is accurate only for the initial fixed period.</p></details>
<details><summary>Why is my lender’s payment slightly different?</summary><p>Lenders round differently, may require an escrow cushion, and use exact tax and insurance bills. Treat this result as a close estimate.</p></details>
</div>
<p><em>This calculator provides estimates for planning only and is not financial advice. Confirm figures with your lender.</em></p>
"""),
]
