"""Tool registry part A: text tools and calculators."""

TOOLS_A = [
# ---------------------------------------------------------------- word counter
dict(
slug="word-counter", name="Word Counter", cat="text", ico="Wc",
title="Word Counter – Count Words, Characters & Reading Time Online",
desc="Free online word counter. Count words, characters, sentences and paragraphs, and see reading and speaking time as you type.",
short="Count words, characters, sentences and reading time as you type.",
ui="""
<div class="field"><label for="wc-in">Your text</label>
<textarea id="wc-in" placeholder="Type or paste your text here…"></textarea></div>
<div class="stats" aria-live="polite">
 <div class="stat"><b id="wc-words">0</b><span>Words</span></div>
 <div class="stat"><b id="wc-chars">0</b><span>Characters</span></div>
 <div class="stat"><b id="wc-nospace">0</b><span>Without spaces</span></div>
 <div class="stat"><b id="wc-sent">0</b><span>Sentences</span></div>
 <div class="stat"><b id="wc-para">0</b><span>Paragraphs</span></div>
 <div class="stat"><b id="wc-read">0 min</b><span>Reading time</span></div>
 <div class="stat"><b id="wc-speak">0 min</b><span>Speaking time</span></div>
</div>
<div class="btns"><button class="btn ghost" id="wc-copy" type="button">Copy text</button>
<button class="btn ghost" id="wc-clear" type="button">Clear</button></div>
<h3>Most used words</h3><div id="wc-top" class="code">Start typing to see keyword frequency.</div>
""",
content="""
<p>This word counter gives you a live count of words, characters, sentences and paragraphs while you type or paste. It also estimates how long the text takes to read silently and to say out loud, which is handy for speeches, video scripts and presentations. Everything runs in your browser, so your writing is never uploaded anywhere.</p>
<h2>How to use the word counter</h2>
<ol>
<li>Type in the box above, or paste text from Word, Google Docs, an email or a web page.</li>
<li>Watch the counts update instantly. There is no button to press.</li>
<li>Check the “Most used words” list to spot words you repeat too often.</li>
<li>Use “Copy text” to take your edited text back to where you were working.</li>
</ol>
<h2>When a word count matters</h2>
<p>Students work to essay limits, such as a 500-word college application essay or a 2,000-word assignment. Freelance writers are often paid per word. Social platforms and search engines also have practical limits: a page title usually displays fully at around 50–60 characters, and a meta description at around 150–160 characters. Knowing your exact count saves you from trimming at the last minute.</p>
<h2>How the counts are calculated</h2>
<ul>
<li><strong>Words</strong> are groups of letters or numbers separated by spaces or line breaks. Hyphenated words like “well-known” count as one word, which matches how most word processors count.</li>
<li><strong>Sentences</strong> end with a full stop, question mark or exclamation mark.</li>
<li><strong>Paragraphs</strong> are blocks of text separated by a blank line or line break.</li>
<li><strong>Reading time</strong> assumes about 238 words per minute, a commonly cited average for adult silent reading of non-fiction.</li>
<li><strong>Speaking time</strong> assumes about 140 words per minute, a comfortable pace for a talk or voice-over.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is my text saved or sent to a server?</summary><p>No. The counting happens entirely in your browser with JavaScript. Close the tab and the text is gone.</p></details>
<details><summary>Why is my count slightly different from Microsoft Word?</summary><p>Tools treat edge cases differently, such as dashes with spaces around them, URLs and numbers with symbols. The difference is usually one or two words in a long document.</p></details>
<details><summary>Does it count words in other languages?</summary><p>Yes, for any language that separates words with spaces, including Spanish, French, German and Urdu written in Roman script. Languages like Chinese and Japanese do not use spaces, so the character count is the better measure for them.</p></details>
<details><summary>How many pages is 1,000 words?</summary><p>Roughly two pages single-spaced or four pages double-spaced, using a 12-point font and standard margins.</p></details>
</div>
"""),
# ---------------------------------------------------------------- case converter
dict(
slug="case-converter", name="Case Converter", cat="text", ico="Aa",
title="Case Converter – UPPERCASE, lowercase, Title Case & more",
desc="Convert text to uppercase, lowercase, title case, sentence case, camelCase, snake_case and kebab-case instantly. Free and private.",
short="Switch text between UPPER, lower, Title, Sentence, camelCase and more.",
ui="""
<div class="field"><label for="cc-in">Your text</label>
<textarea id="cc-in" placeholder="Paste text to convert…"></textarea></div>
<div class="btns" id="cc-btns">
 <button class="btn" type="button" data-case="upper">UPPERCASE</button>
 <button class="btn" type="button" data-case="lower">lowercase</button>
 <button class="btn" type="button" data-case="title">Title Case</button>
 <button class="btn" type="button" data-case="sentence">Sentence case</button>
 <button class="btn ghost" type="button" data-case="camel">camelCase</button>
 <button class="btn ghost" type="button" data-case="pascal">PascalCase</button>
 <button class="btn ghost" type="button" data-case="snake">snake_case</button>
 <button class="btn ghost" type="button" data-case="kebab">kebab-case</button>
 <button class="btn ghost" type="button" data-case="alt">aLtErNaTiNg</button>
</div>
<div class="btns"><button class="btn ghost" id="cc-copy" type="button">Copy result</button></div>
""",
content="""
<p>The case converter changes the capitalization of any text in one click. Fix a paragraph someone typed with Caps Lock on, turn a list of names into proper Title Case, or format variable names for code. The result replaces the text in the box so you can convert again or copy it straight away.</p>
<h2>How to use it</h2>
<ol>
<li>Paste or type your text into the box.</li>
<li>Click the case you want. The text changes immediately.</li>
<li>Click “Copy result” and paste it wherever you need it.</li>
</ol>
<h2>What each option does</h2>
<ul>
<li><strong>UPPERCASE</strong> makes every letter a capital. Good for headings and labels.</li>
<li><strong>lowercase</strong> makes every letter small. Useful for cleaning up email lists or tags.</li>
<li><strong>Title Case</strong> capitalizes the main words and keeps short words like “a”, “of” and “the” in lowercase unless they start the title, following common headline style.</li>
<li><strong>Sentence case</strong> capitalizes the first letter of each sentence and lowercases the rest. This is the style most modern websites use for headings and buttons.</li>
<li><strong>camelCase</strong> and <strong>PascalCase</strong> remove spaces and capitalize each word, used for JavaScript and Java names.</li>
<li><strong>snake_case</strong> joins words with underscores, common in Python and databases.</li>
<li><strong>kebab-case</strong> joins words with hyphens, used in URLs and CSS class names.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Will Sentence case fix names and places?</summary><p>No tool can know every proper noun, so names like “London” or “Sara” will become lowercase in the middle of a sentence. Read through the result and capitalize names by hand.</p></details>
<details><summary>Can I convert a whole document?</summary><p>Yes. There is no length limit beyond what your browser can handle comfortably, which is many thousands of words.</p></details>
<details><summary>Does it keep line breaks?</summary><p>For UPPER, lower, Title and Sentence case, yes. The code-style options (camelCase, snake_case and so on) convert each line separately so a list of names becomes a list of identifiers.</p></details>
</div>
"""),
# ---------------------------------------------------------------- lorem ipsum
dict(
slug="lorem-ipsum-generator", name="Lorem Ipsum Generator", cat="text", ico="Li",
title="Lorem Ipsum Generator – Placeholder Text for Designs",
desc="Generate lorem ipsum placeholder text by paragraphs, sentences or words. Copy plain text or HTML for mockups and templates.",
short="Make placeholder text by paragraphs, sentences or words.",
ui="""
<div class="row">
 <div class="field"><label for="li-n">How many</label><input id="li-n" type="number" min="1" max="100" value="3"></div>
 <div class="field"><label for="li-unit">Of what</label><select id="li-unit"><option value="p">Paragraphs</option><option value="s">Sentences</option><option value="w">Words</option></select></div>
</div>
<label class="check"><input type="checkbox" id="li-start" checked> Start with “Lorem ipsum dolor sit amet…”</label>
<label class="check"><input type="checkbox" id="li-html"> Wrap paragraphs in &lt;p&gt; tags</label>
<div class="btns"><button class="btn" id="li-go" type="button">Generate</button><button class="btn ghost" id="li-copy" type="button">Copy</button></div>
<div class="field"><label for="li-out">Result</label><textarea id="li-out" readonly></textarea></div>
""",
content="""
<p>Lorem ipsum is dummy text that designers and developers use to fill a layout before the real words are ready. Because it looks like natural language but cannot be read, people judge the design itself instead of getting distracted by the copy. This generator creates as much of it as you need, as plain text or as HTML paragraphs.</p>
<h2>How to use it</h2>
<ol>
<li>Choose a number and whether you want paragraphs, sentences or words.</li>
<li>Decide whether to start with the classic opening line and whether you want &lt;p&gt; tags.</li>
<li>Click Generate, then Copy, and paste it into your design tool, CMS or code.</li>
</ol>
<h2>Where lorem ipsum comes from</h2>
<p>The text is a scrambled passage from <em>De finibus bonorum et malorum</em>, a work on ethics written by the Roman philosopher Cicero in 45 BC. Printers began using a shuffled version of it as filler type centuries ago, and it spread to desktop publishing software in the 1980s. The words are real Latin roots, which is why the text has a natural rhythm of short and long words.</p>
<h2>Tips for using placeholder text</h2>
<ul>
<li>Match the length you expect from the real content. A headline slot filled with three paragraphs will hide layout problems.</li>
<li>Replace placeholder text before a site goes live. Search engines and ad reviewers treat pages full of lorem ipsum as unfinished.</li>
<li>For user testing, real or realistic copy usually gives better feedback than Latin filler.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is lorem ipsum free to use?</summary><p>Yes. It is based on a text over 2,000 years old and is in the public domain.</p></details>
<details><summary>Is the generated text random each time?</summary><p>Yes. Sentences are built from a word list with random lengths, so each click gives a different result.</p></details>
<details><summary>What is the maximum I can generate?</summary><p>Up to 100 paragraphs, sentences or words per click. Click again to generate more.</p></details>
</div>
"""),
# ---------------------------------------------------------------- text cleaner
dict(
slug="text-cleaner", name="Text Cleaner", cat="text", ico="Tc",
title="Text Cleaner – Remove Line Breaks, Extra Spaces & Duplicates",
desc="Clean up messy text. Remove line breaks, extra spaces, empty lines and duplicate lines, or sort lines alphabetically. Free online tool.",
short="Remove line breaks, extra spaces, empty or duplicate lines.",
ui="""
<div class="field"><label for="tc-in">Messy text</label><textarea id="tc-in" placeholder="Paste text copied from a PDF, email or spreadsheet…"></textarea></div>
<div class="row">
 <label class="check"><input type="checkbox" id="tc-breaks"> Join lines (remove line breaks)</label>
 <label class="check"><input type="checkbox" id="tc-spaces" checked> Collapse extra spaces</label>
 <label class="check"><input type="checkbox" id="tc-empty" checked> Remove empty lines</label>
 <label class="check"><input type="checkbox" id="tc-trim" checked> Trim each line</label>
 <label class="check"><input type="checkbox" id="tc-dupes"> Remove duplicate lines</label>
 <label class="check"><input type="checkbox" id="tc-sort"> Sort lines A–Z</label>
</div>
<div class="btns"><button class="btn" id="tc-go" type="button">Clean text</button><button class="btn ghost" id="tc-copy" type="button">Copy result</button></div>
<p id="tc-note" class="count-note" aria-live="polite"></p>
<div class="field"><label for="tc-out">Clean text</label><textarea id="tc-out" readonly></textarea></div>
""",
content="""
<p>Text copied from a PDF, an email chain or a spreadsheet often arrives with broken lines, double spaces and blank rows. The text cleaner fixes all of that in one pass. Tick the fixes you want, click Clean text, and copy the tidy version.</p>
<h2>How to use it</h2>
<ol>
<li>Paste your text into the first box.</li>
<li>Tick the clean-up options you need. Sensible defaults are already selected.</li>
<li>Click “Clean text”. The result appears below with a note of how many lines changed.</li>
</ol>
<h2>Common jobs this solves</h2>
<ul>
<li><strong>Fixing PDF copy-paste.</strong> PDFs break sentences at the end of every printed line. “Join lines” puts each paragraph back together while keeping blank lines between paragraphs.</li>
<li><strong>Cleaning a list of emails or keywords.</strong> Turn on “Remove duplicate lines” and “Sort lines A–Z” to get a unique, ordered list.</li>
<li><strong>Preparing text for a form or database.</strong> Collapsing spaces and trimming lines removes invisible characters that cause mismatches.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Does “Join lines” merge my paragraphs too?</summary><p>No. Single line breaks inside a paragraph are joined with a space, but a blank line between paragraphs is kept so your structure stays intact.</p></details>
<details><summary>Is duplicate removal case-sensitive?</summary><p>Yes. “Apple” and “apple” are treated as different lines. Use the Case Converter first if you want them treated the same.</p></details>
<details><summary>Is there a size limit?</summary><p>The tool handles tens of thousands of lines comfortably in a modern browser.</p></details>
</div>
"""),
# ---------------------------------------------------------------- slug generator
dict(
slug="slug-generator", name="URL Slug Generator", cat="text", ico="/s",
title="URL Slug Generator – SEO-Friendly Permalinks",
desc="Turn any title into a clean, SEO-friendly URL slug. Removes accents, symbols and stop words, with lowercase and hyphen options.",
short="Turn a page title into a clean, SEO-friendly URL slug.",
ui="""
<div class="field"><label for="sg-in">Title or text</label><input id="sg-in" type="text" placeholder="e.g. 10 Best Café Ideas for Small Spaces!"></div>
<div class="row">
 <div class="field"><label for="sg-sep">Separator</label><select id="sg-sep"><option value="-">Hyphen (-)</option><option value="_">Underscore (_)</option></select></div>
 <div class="field"><label for="sg-max">Max length</label><input id="sg-max" type="number" min="10" max="200" value="60"></div>
</div>
<label class="check"><input type="checkbox" id="sg-stop"> Remove stop words (a, the, of, and…)</label>
<div class="result"><span class="lbl">Your slug</span><div class="big code" id="sg-out" style="font-size:1.3rem;word-break:break-all">—</div></div>
<div class="btns"><button class="btn ghost" id="sg-copy" type="button">Copy slug</button></div>
""",
content="""
<p>A slug is the readable part of a web address that identifies a page, like <code>/best-cafe-ideas</code>. This generator turns any title into a slug that is lowercase, uses hyphens between words and drops characters that break or clutter URLs. The slug updates as you type.</p>
<h2>How to use it</h2>
<ol>
<li>Type or paste your article or product title.</li>
<li>Pick a separator and a maximum length. Hyphens are recommended for SEO.</li>
<li>Optionally remove short stop words to make the slug tighter.</li>
<li>Copy the slug into WordPress, Shopify or your CMS permalink field.</li>
</ol>
<h2>What makes a good slug</h2>
<ul>
<li><strong>Short and descriptive.</strong> Three to five meaningful words is usually enough. People and search engines can tell what the page is about at a glance.</li>
<li><strong>Hyphens, not underscores.</strong> Google’s own URL guidance recommends hyphens to separate words, because underscores can join words together when read by machines.</li>
<li><strong>Lowercase only.</strong> Some servers treat <code>/Page</code> and <code>/page</code> as different addresses, which can create duplicates.</li>
<li><strong>No dates unless needed.</strong> A slug without a year stays accurate when you update the article later.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What happens to accented letters?</summary><p>They are converted to their plain form, so “café” becomes “cafe” and “über” becomes “uber”. This keeps the URL readable everywhere.</p></details>
<details><summary>Should I change the slug of a published page?</summary><p>Only if you set up a 301 redirect from the old address. Otherwise existing links and search rankings point to a page that no longer exists.</p></details>
<details><summary>Should I remove stop words?</summary><p>It is optional. Removing them shortens the URL, but keep them if the slug reads strangely without them.</p></details>
</div>
"""),
# ---------------------------------------------------------------- age calculator
dict(
slug="age-calculator", name="Age Calculator", cat="calc", ico="Ag",
title="Age Calculator – Exact Age in Years, Months and Days",
desc="Calculate your exact age in years, months and days from your date of birth, plus total days lived and days until your next birthday.",
short="Find exact age in years, months and days, and days to next birthday.",
ui="""
<div class="row">
 <div class="field"><label for="ag-dob">Date of birth</label><input id="ag-dob" type="date"></div>
 <div class="field"><label for="ag-on">Age on this date</label><input id="ag-on" type="date"></div>
</div>
<div class="btns"><button class="btn" id="ag-go" type="button">Calculate age</button></div>
<div class="result" id="ag-out" aria-live="polite"></div>
""",
content="""
<p>The age calculator works out exactly how old someone is in years, months and days on any date. It also shows the total number of months, weeks and days lived and counts down to the next birthday. Leave the second date as today, or change it to find someone’s age on a past or future date, such as an exam cut-off or a visa application.</p>
<p>Only know the year? See the <a href="/how-old-am-i">age by birth year chart</a>, or work backwards with <a href="/what-year-was-i-born">what year was I born</a>.</p>
<h2>How to use it</h2>
<ol>
<li>Enter the date of birth.</li>
<li>Leave “Age on this date” as today, or pick another date.</li>
<li>Click “Calculate age” to see the full breakdown.</li>
</ol>
<h2>How age is calculated</h2>
<p>The calculator counts complete years first, then complete months, then the remaining days. When a month is shorter than the birth day, the monthly anniversary falls on that month’s last day, so someone born on 31 January is one month old on 28 February (or 29 February in a leap year). Any days after the last full month are counted as remaining days.</p>
<p>People born on 29 February have a birthday only in leap years. In other years this calculator treats 1 March as the next birthday, which is the convention used in many countries, including the UK, for legal age.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Can I calculate age for a future date?</summary><p>Yes. Set the second date in the future to see how old you will be then, for example on the day of a competition or retirement.</p></details>
<details><summary>Does it count leap years?</summary><p>Yes. Total days lived uses the real calendar, so every 29 February in the period is included.</p></details>
<details><summary>Is my date of birth stored?</summary><p>No. The calculation runs in your browser and nothing is saved or sent.</p></details>
</div>
"""),
# ---------------------------------------------------------------- BMI
dict(
slug="bmi-calculator", name="BMI Calculator", cat="calc", ico="Bm",
title="BMI Calculator – Body Mass Index for Adults (kg/cm or lb/ft)",
desc="Calculate your Body Mass Index with metric or imperial units. See your BMI category and the healthy weight range for your height.",
short="Work out body mass index in metric or imperial units.",
ui="""
<div class="field"><span class="lbl">Units</span>
<label class="check" style="display:inline-flex;margin-right:16px"><input type="radio" name="bm-u" value="m" checked> Metric (kg, cm)</label>
<label class="check" style="display:inline-flex"><input type="radio" name="bm-u" value="i"> Imperial (lb, ft, in)</label></div>
<div class="row" id="bm-metric">
 <div class="field"><label for="bm-kg">Weight (kg)</label><input id="bm-kg" type="number" min="1" step="0.1" placeholder="70"></div>
 <div class="field"><label for="bm-cm">Height (cm)</label><input id="bm-cm" type="number" min="30" step="0.1" placeholder="175"></div>
</div>
<div class="row" id="bm-imp" hidden>
 <div class="field"><label for="bm-lb">Weight (lb)</label><input id="bm-lb" type="number" min="1" step="0.1" placeholder="154"></div>
 <div class="field"><label for="bm-ft">Height (ft)</label><input id="bm-ft" type="number" min="1" step="1" placeholder="5"></div>
 <div class="field"><label for="bm-in">Height (in)</label><input id="bm-in" type="number" min="0" step="0.1" placeholder="9"></div>
</div>
<div class="btns"><button class="btn" id="bm-go" type="button">Calculate BMI</button></div>
<div class="result" id="bm-out" aria-live="polite"></div>
""",
content="""
<p>Body Mass Index (BMI) is a quick screening number that compares weight with height. This calculator works with kilograms and centimetres or pounds, feet and inches, tells you which standard adult category your result falls into, and shows the weight range that counts as “healthy” for your height.</p>
<h2>How to use it</h2>
<ol>
<li>Choose metric or imperial units.</li>
<li>Enter your weight and height.</li>
<li>Click “Calculate BMI” to see your number, category and healthy range.</li>
</ol>
<h2>The BMI formula</h2>
<div class="formula">BMI = weight (kg) ÷ height (m)²<br>BMI = 703 × weight (lb) ÷ height (in)²</div>
<p>For example, someone who weighs 70 kg and is 1.75 m tall has a BMI of 70 ÷ (1.75 × 1.75) = 22.9.</p>
<h2>Adult BMI categories</h2>
<ul>
<li>Below 18.5 – underweight</li>
<li>18.5 to 24.9 – healthy weight</li>
<li>25 to 29.9 – overweight</li>
<li>30 and above – obesity</li>
</ul>
<p>These are the World Health Organization ranges for adults aged 18 and over. Some health services use lower cut-offs for people of South Asian, Chinese and other Asian backgrounds, because health risks start to rise at a lower BMI.</p>
<h2>What BMI does not tell you</h2>
<p>BMI does not separate muscle from fat, so athletes can score as “overweight” while being very fit. It also ignores where fat is stored, age and sex. Treat it as a starting point and speak to a doctor or qualified health professional about your own health.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Can children use this calculator?</summary><p>No. Children and teenagers need BMI-for-age percentiles, which compare them with others of the same age and sex. Ask a pediatrician for that check.</p></details>
<details><summary>Is BMI accurate during pregnancy?</summary><p>No. Weight gain in pregnancy is expected, so BMI is not a useful measure at that time.</p></details>
</div>
<p><em>This calculator is for general information only and is not medical advice.</em></p>
"""),
# ---------------------------------------------------------------- percentage
dict(
slug="percentage-calculator", name="Percentage Calculator", cat="calc", ico="%",
title="Percentage Calculator – Percent Of, Change & Difference",
desc="Free percentage calculator. Find X% of a number, what percent one number is of another, and percentage increase or decrease.",
short="Find X% of a number, percent change and more.",
ui="""
<div class="panel" style="border-top-width:1px;padding:16px">
 <span class="lbl">What is X% of Y?</span>
 <div class="row"><input id="pc-a1" type="number" aria-label="Percent" placeholder="15"><input id="pc-a2" type="number" aria-label="Of number" placeholder="200"></div>
 <p class="big" id="pc-a" aria-live="polite" style="font-size:1.4rem;margin:10px 0 0">—</p>
</div>
<div class="panel" style="border-top-width:1px;padding:16px">
 <span class="lbl">X is what percent of Y?</span>
 <div class="row"><input id="pc-b1" type="number" aria-label="Part" placeholder="30"><input id="pc-b2" type="number" aria-label="Whole" placeholder="120"></div>
 <p class="big" id="pc-b" aria-live="polite" style="font-size:1.4rem;margin:10px 0 0">—</p>
</div>
<div class="panel" style="border-top-width:1px;padding:16px">
 <span class="lbl">Percentage change from X to Y</span>
 <div class="row"><input id="pc-c1" type="number" aria-label="From" placeholder="80"><input id="pc-c2" type="number" aria-label="To" placeholder="100"></div>
 <p class="big" id="pc-c" aria-live="polite" style="font-size:1.4rem;margin:10px 0 0">—</p>
</div>
""",
content="""
<p>This percentage calculator handles the three questions people ask most often: what a percentage of a number is, what percent one number is of another, and how much something has gone up or down in percentage terms. Results update as you type.</p>
<h2>How to use it</h2>
<p>Pick the box that matches your question and fill in both numbers. You do not need to type the % sign.</p>
<h2>The formulas</h2>
<div class="formula">X% of Y = (X ÷ 100) × Y<br>X as % of Y = (X ÷ Y) × 100<br>% change = ((New − Old) ÷ Old) × 100</div>
<h3>Worked examples</h3>
<ul>
<li><strong>Tip or tax:</strong> 15% of 200 = 0.15 × 200 = 30.</li>
<li><strong>Exam score:</strong> 30 out of 120 = 30 ÷ 120 × 100 = 25%.</li>
<li><strong>Price rise:</strong> from 80 to 100 = (100 − 80) ÷ 80 × 100 = 25% increase.</li>
</ul>
<h2>A common mistake</h2>
<p>A 20% fall followed by a 20% rise does not bring you back to where you started. If a price drops from 100 to 80, it needs to rise by 25% to reach 100 again, because the second percentage is calculated on the smaller number. The percentage change box makes this easy to check.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What is the difference between percent and percentage points?</summary><p>If an interest rate moves from 4% to 5%, it has risen by one percentage point, but by 25 percent in relative terms. Use percentage points when comparing two percentages directly.</p></details>
<details><summary>Can I use negative numbers or decimals?</summary><p>Yes. All three calculators accept decimals and negative values.</p></details>
</div>
"""),
# ---------------------------------------------------------------- loan
dict(
slug="loan-calculator", name="Loan & EMI Calculator", cat="calc", ico="Ln",
title="Loan Calculator – Monthly Payment (EMI), Interest & Schedule",
desc="Calculate your monthly loan payment (EMI), total interest and total cost. See a full amortization schedule for car, home or personal loans.",
short="Monthly payment, total interest and amortization schedule.",
ui="""
<div class="row">
 <div class="field"><label for="ln-p">Loan amount</label><input id="ln-p" type="number" min="0" value="25000"></div>
 <div class="field"><label for="ln-r">Annual interest rate (%)</label><input id="ln-r" type="number" min="0" step="0.01" value="7.5"></div>
 <div class="field"><label for="ln-y">Term (years)</label><input id="ln-y" type="number" min="0" step="0.5" value="5"></div>
</div>
<div class="btns"><button class="btn" id="ln-go" type="button">Calculate payment</button></div>
<div class="result" id="ln-out" aria-live="polite"></div>
<details id="ln-sched-wrap" hidden style="margin-top:14px"><summary class="lbl" style="cursor:pointer">Yearly amortization schedule</summary><div id="ln-sched" style="overflow-x:auto"></div></details>
""",
content="""
<p>The loan calculator shows what a loan will really cost you each month and over its whole life. Enter the amount, the yearly interest rate and the term, and you get the monthly payment (often called EMI, or equated monthly instalment), the total interest and a year-by-year breakdown of how much of each payment goes to interest and how much reduces the balance.</p>
<h2>How to use it</h2>
<ol>
<li>Enter the amount you plan to borrow.</li>
<li>Enter the annual interest rate quoted by the lender (APR or nominal rate).</li>
<li>Enter the term in years, for example 5 for a car loan or 30 for a mortgage.</li>
<li>Click “Calculate payment” and open the schedule to see each year.</li>
</ol>
<h2>The EMI formula</h2>
<div class="formula">M = P × r × (1 + r)<sup>n</sup> ÷ ((1 + r)<sup>n</sup> − 1)</div>
<p>Here <strong>P</strong> is the loan amount, <strong>r</strong> is the monthly interest rate (annual rate ÷ 12 ÷ 100) and <strong>n</strong> is the number of monthly payments. For a 25,000 loan at 7.5% over 5 years, r = 0.00625 and n = 60, giving a payment of about 500.95 a month and roughly 5,057 in total interest.</p>
<h2>Ways to pay less interest</h2>
<ul>
<li><strong>Shorten the term.</strong> Monthly payments go up, but total interest drops sharply.</li>
<li><strong>Make extra payments.</strong> Early in a loan most of each payment is interest, so paying extra toward the balance then has the biggest effect. Check that your lender does not charge prepayment fees.</li>
<li><strong>Compare rates.</strong> Even half a percentage point makes a large difference on a long mortgage.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Does this include fees, insurance or taxes?</summary><p>No. It covers principal and interest only. Mortgages often add property tax and insurance to the monthly bill, and loans can carry origination fees.</p></details>
<details><summary>What if the interest rate is 0%?</summary><p>The calculator divides the loan evenly across the months, so the payment is simply the amount divided by the number of payments.</p></details>
</div>
<p><em>Results are estimates for planning. Your lender’s figures may differ slightly because of rounding and fees.</em></p>
"""),
# ---------------------------------------------------------------- discount
dict(
slug="discount-calculator", name="Discount Calculator", cat="calc", ico="Ds",
title="Discount Calculator – Sale Price & Savings",
desc="Find the sale price after a percentage discount, how much you save, and the final price with sales tax. Supports double discounts.",
short="Sale price after discount, savings and price with tax.",
ui="""
<div class="row">
 <div class="field"><label for="ds-p">Original price</label><input id="ds-p" type="number" min="0" step="0.01" value="80"></div>
 <div class="field"><label for="ds-d">Discount (%)</label><input id="ds-d" type="number" min="0" max="100" step="0.1" value="25"></div>
 <div class="field"><label for="ds-d2">Extra discount (%)</label><input id="ds-d2" type="number" min="0" max="100" step="0.1" value="0"></div>
 <div class="field"><label for="ds-t">Sales tax (%)</label><input id="ds-t" type="number" min="0" step="0.01" value="0"></div>
</div>
<div class="stats" aria-live="polite">
 <div class="stat"><b id="ds-final">—</b><span>You pay</span></div>
 <div class="stat"><b id="ds-save">—</b><span>You save</span></div>
 <div class="stat"><b id="ds-eff">—</b><span>Total discount</span></div>
</div>
""",
content="""
<p>Shopping a sale? The discount calculator shows the price you will actually pay, how much money you save, and the combined effect of stacked discounts such as “30% off plus an extra 10% at checkout”. Add your local sales tax to see the final total at the till.</p>
<h2>How to use it</h2>
<ol>
<li>Enter the original price and the discount percentage.</li>
<li>If there is a second discount, enter it in “Extra discount”. Leave it at 0 otherwise.</li>
<li>Add sales tax if it is charged on top of the sale price.</li>
</ol>
<h2>How stacked discounts work</h2>
<p>Two discounts are not added together. The second one applies to the already reduced price. So 30% off followed by an extra 10% off is a total discount of 37%, not 40%:</p>
<div class="formula">Final = Price × (1 − d1/100) × (1 − d2/100) × (1 + tax/100)</div>
<p>On a 100 item: 100 × 0.70 = 70, then 70 × 0.90 = 63. You save 37.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is tax calculated before or after the discount?</summary><p>In most places, including US states, sales tax is charged on the discounted price, which is how this calculator works.</p></details>
<details><summary>How do I find the original price from a sale price?</summary><p>Divide the sale price by (1 − discount/100). A 60 item that is 25% off was originally 60 ÷ 0.75 = 80.</p></details>
</div>
"""),
]
