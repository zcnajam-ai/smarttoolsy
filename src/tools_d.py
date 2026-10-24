"""Tool registry part D: Delete PDF Pages, Add Pages to PDF, TXT to PDF, Amortization Schedule."""
from tools_c import drop, PRIVACY_FAQ, PDF_LIB

TOOLS_D = [
# ---------------------------------------------------------------- delete pages
dict(
slug="delete-pdf-pages", name="Delete PDF Pages", cat="pdf", ico="D−", scripts=[PDF_LIB],
title="Delete Pages from PDF Free – Remove PDF Pages Online",
desc="Remove unwanted pages from a PDF for free. Click page thumbnails or type page numbers, then download the new file. Nothing is uploaded.",
short="Remove unwanted pages from a PDF by clicking them.",
ui=drop("dp-file", "application/pdf,.pdf", "Choose a PDF file", "Page previews appear below. Click a page to mark it for deletion.") + """
<p id="dp-info" class="count-note" aria-live="polite"></p>
<div id="dp-opts" hidden>
<div class="field"><label for="dp-pages">Pages to delete</label><input id="dp-pages" type="text" placeholder="Click pages below, or type e.g. 2, 5-7"></div>
<div class="thumbs pick" id="dp-thumbs"></div>
<div class="btns"><button class="btn" id="dp-go" type="button">Delete pages and download</button></div>
</div>
<p id="dp-msg" class="count-note" aria-live="polite"></p>
<div class="btns" id="dp-dl-wrap" hidden><a class="btn" id="dp-dl" download="edited.pdf">Download PDF</a></div>
""",
content="""
<p>Delete PDF Pages removes the pages you don’t want from a PDF and gives you a clean new file. Take out blank scanned pages, ads in a bank statement, an old cover sheet or confidential pages before you share a document. You can see every page as a thumbnail, so you remove exactly the right ones.</p>
<h2>How to delete pages from a PDF</h2>
<ol>
<li>Choose your PDF. Small previews of every page appear.</li>
<li>Click each page you want to remove. Marked pages turn red, and their numbers fill the box above. You can also type page numbers directly, such as <code>2, 5-7</code>.</li>
<li>Click “Delete pages and download”.</li>
</ol>
<p>The pages you keep stay exactly as they were: text remains selectable, images keep their quality and nothing is re-compressed.</p>
<h2>Why delete pages instead of printing a new PDF?</h2>
<p>Printing a PDF to a new PDF with a page range is a common workaround, but it only handles one continuous range and can flatten form fields or increase file size. Deleting pages directly keeps the original page content untouched and lets you remove pages from anywhere in the document at once.</p>
<h2>Tips</h2>
<ul>
<li>Want to keep only a few pages from a long file? It may be quicker to extract them with <a href="/split-pdf">Split PDF</a>.</li>
<li>Need to put pages in from another document? Use <a href="/add-pages-to-pdf">Add Pages to PDF</a>.</li>
<li>Your original file is never changed; you download a new copy.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
""" + PRIVACY_FAQ + """
<details><summary>Can I undo a deletion?</summary><p>Yes, before you download. Click a red page again to keep it. After downloading, your original PDF is still on your device unchanged.</p></details>
<details><summary>Can I delete every page?</summary><p>No. A PDF must have at least one page, so the tool asks you to keep one or more.</p></details>
<details><summary>Does it work with scanned PDFs?</summary><p>Yes. Scanned pages are images inside the PDF, and they are kept or removed just like any other page.</p></details>
</div>
"""),
# ---------------------------------------------------------------- add pages
dict(
slug="add-pages-to-pdf", name="Add Pages to PDF", cat="pdf", ico="A+", scripts=[PDF_LIB],
title="Add Pages to PDF – Insert Pages or Images into a PDF Free",
desc="Insert pages from another PDF, or JPG and PNG images, into an existing PDF at the beginning, the end or after any page. Free and private.",
short="Insert pages from another PDF or images anywhere in a PDF.",
ui=drop("ap-main", "application/pdf,.pdf", "1. Choose the main PDF", "This is the document you want to add pages to.") + """
<p id="ap-info" class="count-note" aria-live="polite"></p>
<div style="margin-top:12px">""" + drop("ap-add", "application/pdf,.pdf,image/jpeg,image/png,image/webp", "2. Choose pages to add", "PDF files or JPG, PNG and WebP images.", True) + """</div>
<ol class="file-list" id="ap-list" aria-live="polite"></ol>
<div class="row">
 <div class="field"><label for="ap-pos">Insert</label><select id="ap-pos"><option value="end">At the end</option><option value="start">At the beginning</option><option value="after">After page…</option></select></div>
 <div class="field" id="ap-after-f" hidden><label for="ap-after">After page number</label><input id="ap-after" type="number" min="1" value="1"></div>
</div>
<div class="btns"><button class="btn" id="ap-go" type="button" disabled>Add pages</button></div>
<p id="ap-msg" class="count-note" aria-live="polite"></p>
<div class="btns" id="ap-dl-wrap" hidden><a class="btn" id="ap-dl" download="with-added-pages.pdf">Download PDF</a></div>
""",
content="""
<p>Add Pages to PDF inserts new pages into a document you already have. Put a signed page back into a contract, add a cover page, attach photos of receipts to an expense report, or slip a missing page into the middle of a scan. Pages can come from other PDFs or from JPG, PNG and WebP images.</p>
<h2>How to add pages to a PDF</h2>
<ol>
<li>Choose the main PDF you want to add to.</li>
<li>Choose the files to insert. Each PDF adds all of its pages; each image becomes one page.</li>
<li>Pick where they go: at the beginning, at the end, or after a specific page.</li>
<li>Click “Add pages” and download the new PDF.</li>
</ol>
<h2>How image pages are sized</h2>
<p>Images are placed on pages the same size as the first page of your main PDF, so a photo added to a US Letter document becomes a US Letter page. The picture is scaled to fit inside the page with a small margin and keeps its proportions. Phone photos keep the rotation your camera recorded.</p>
<h2>Adding vs merging</h2>
<p>If you simply want to join whole files end to end, <a href="/merge-pdf">Merge PDF</a> is quicker. Use this tool when the new pages must go in a particular place inside an existing document. To take pages out instead, use <a href="/delete-pdf-pages">Delete PDF Pages</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
""" + PRIVACY_FAQ + """
<details><summary>Can I add a blank page?</summary><p>Yes. Add a plain white image (for example, a screenshot of an empty document) and it becomes a blank page at the size of your PDF.</p></details>
<details><summary>Will the original pages change?</summary><p>No. Existing pages are copied exactly; only the new pages are added.</p></details>
</div>
"""),
# ---------------------------------------------------------------- txt to pdf
dict(
slug="txt-to-pdf", name="TXT to PDF", cat="pdf", ico="T>", scripts=[PDF_LIB],
title="TXT to PDF Converter – Convert Text Files to PDF Online",
desc="Convert a .txt file or pasted text into a clean PDF. Choose font, size, page size and margins. Free, no sign-up, and nothing is uploaded.",
short="Turn a .txt file or pasted text into a tidy PDF.",
ui=drop("tp-file", ".txt,text/plain", "Choose a .txt file", "Or paste text in the box below.") + """
<div class="field" style="margin-top:12px"><label for="tp-text">Text</label><textarea id="tp-text" placeholder="Paste or type your text…"></textarea></div>
<div class="row">
 <div class="field"><label for="tp-font">Font</label><select id="tp-font"><option value="Helvetica">Sans serif (Helvetica)</option><option value="TimesRoman">Serif (Times)</option><option value="Courier">Monospace (Courier)</option></select></div>
 <div class="field"><label for="tp-size">Font size</label><select id="tp-size"><option>10</option><option selected>11</option><option>12</option><option>14</option></select></div>
 <div class="field"><label for="tp-page">Page size</label><select id="tp-page"><option value="letter" selected>US Letter</option><option value="a4">A4</option></select></div>
 <div class="field"><label for="tp-margin">Margins</label><select id="tp-margin"><option value="54">0.75 in</option><option value="72" selected>1 in</option><option value="36">0.5 in</option></select></div>
</div>
<div class="btns"><button class="btn" id="tp-go" type="button">Create PDF</button></div>
<p id="tp-msg" class="count-note" aria-live="polite"></p>
<div class="btns" id="tp-dl-wrap" hidden><a class="btn" id="tp-dl" download="text.pdf">Download PDF</a></div>
""",
content="""
<p>TXT to PDF turns plain text into a properly formatted PDF document. It is handy for notes, logs, code snippets, transcripts and anything saved from a simple text editor that you need to send, print or upload somewhere that only accepts PDFs. Long lines wrap neatly and pages break automatically.</p>
<h2>How to convert text to PDF</h2>
<ol>
<li>Choose a .txt file, or paste your text into the box.</li>
<li>Pick a font, size, page size and margins.</li>
<li>Click “Create PDF” and download the file.</li>
</ol>
<h2>Choosing a font</h2>
<ul>
<li><strong>Sans serif</strong> is clean and easy to read on screen.</li>
<li><strong>Serif</strong> looks traditional and suits letters and printed documents.</li>
<li><strong>Monospace</strong> gives every character the same width, so columns, tables made of spaces, and code stay aligned exactly as in your text editor.</li>
</ul>
<h2>Character support</h2>
<p>The tool uses the standard fonts built into every PDF reader, which keeps files tiny and opens everywhere. These fonts cover English and Western European characters, including accented letters and curly quotes. Characters outside that set, such as emoji or non-Latin scripts, are replaced with a question mark and the tool tells you how many were changed. For other scripts, print the text from your browser to PDF instead.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
""" + PRIVACY_FAQ + """
<details><summary>Are tabs and blank lines kept?</summary><p>Yes. Blank lines are kept, and each tab becomes four spaces so indentation is preserved.</p></details>
<details><summary>Can I convert Word documents?</summary><p>This tool handles plain text. For a Word document, use Word’s own “Save as PDF” or “Export” option, which keeps the formatting.</p></details>
</div>
"""),
# ---------------------------------------------------------------- amortization
dict(
slug="amortization-calculator", name="Amortization Schedule Calculator", cat="calc", ico="Am",
title="Amortization Schedule Calculator – Monthly Loan Payment Table",
desc="See a full month-by-month amortization schedule for any loan, with payment dates, principal, interest and balance. Add extra payments and download as CSV.",
short="Month-by-month loan schedule with extra payments and CSV export.",
ui="""
<div class="row">
 <div class="field"><label for="am-p">Loan amount ($)</label><input id="am-p" type="number" min="0" step="100" value="250000"></div>
 <div class="field"><label for="am-r">Interest rate (%)</label><input id="am-r" type="number" min="0" step="0.01" value="6.5"></div>
 <div class="field"><label for="am-y">Term (years)</label><input id="am-y" type="number" min="0.5" step="0.5" value="30"></div>
 <div class="field"><label for="am-start">First payment</label><input id="am-start" type="month"></div>
 <div class="field"><label for="am-extra">Extra principal ($/month)</label><input id="am-extra" type="number" min="0" step="25" value="0"></div>
</div>
<div class="result" id="am-out" aria-live="polite"></div>
<div class="btns"><button class="btn ghost" id="am-csv" type="button">Download schedule (CSV)</button></div>
<div id="am-table"></div>
""",
content="""
<p>An amortization schedule shows exactly how a loan is paid off, one payment at a time. For every month it lists the payment date, how much goes to interest, how much reduces the balance, and what you still owe. Use this calculator for mortgages, car loans, personal loans and student loans with a fixed rate, and see the total cost of the loan before you sign.</p>

<h2>How to use the amortization calculator</h2>
<ol>
<li>Enter the loan amount, the annual interest rate and the term in years.</li>
<li>Choose the month of your first payment so the schedule shows real dates.</li>
<li>Optionally add an extra monthly principal payment to see how much sooner you’d finish.</li>
<li>Open any year to see its monthly rows, or download the full schedule as a CSV file for Excel or Google Sheets.</li>
</ol>

<h2>What “amortization” means</h2>
<p>An amortizing loan is repaid in equal monthly payments that cover both interest and principal. Each month, interest is charged on the balance you still owe. Whatever is left of the payment after interest reduces that balance. Because the balance is largest at the start, early payments are mostly interest; as the balance falls, more of each payment goes to principal. On a 30-year mortgage at 6.5%, it takes many years before principal makes up the larger share of the payment.</p>

<h2>The formula</h2>
<div class="formula">Payment = P × r × (1 + r)<sup>n</sup> ÷ ((1 + r)<sup>n</sup> − 1)<br>Interest this month = balance × r<br>Principal this month = payment − interest</div>
<p><strong>P</strong> is the loan amount, <strong>r</strong> the monthly rate (annual rate ÷ 12 ÷ 100) and <strong>n</strong> the number of payments. A $250,000 loan at 6.5% over 30 years has a monthly payment of about $1,580.17.</p>

<h2>Total loan cost</h2>
<p>The total cost of a loan is every payment added together: the amount you borrowed plus all the interest. The calculator shows this under “Total of payments”. For the example above, you would repay roughly $568,860, of which about $318,860 is interest. Comparing total cost, not just the monthly payment, is the clearest way to compare loan offers with different rates and terms.</p>

<h2>How extra payments change the schedule</h2>
<p>Extra money paid toward principal reduces the balance immediately, so every later month charges less interest. Even modest amounts matter: adding $200 a month to the example loan pays it off years early and saves tens of thousands of dollars in interest. Check with your lender that extra payments are applied to principal and that there is no prepayment penalty.</p>

<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Does the schedule include taxes and insurance?</summary><p>No. It covers principal and interest only. For a house payment including property tax, insurance and PMI, use the <a href="/mortgage-calculator">mortgage calculator</a>.</p></details>
<details><summary>Why is my lender’s schedule slightly different?</summary><p>Lenders round each payment to the cent and some calculate interest by days in the month. Differences are usually a few cents per month.</p></details>
<details><summary>Can I use it for car loans?</summary><p>Yes. Enter the amount financed, the APR and the term, for example 5 years for a 60-month loan.</p></details>
</div>
<p><em>Results are estimates for planning and are not financial advice.</em></p>
"""),
]
