"""Tool registry part B: converters, generators, developer and image tools."""

TOOLS_B = [
# ---------------------------------------------------------------- date difference
dict(
slug="date-difference-calculator", name="Date Difference Calculator", cat="calc", ico="Dd",
title="Days Between Dates Calculator – Count Days, Weeks & Business Days",
desc="Count the days, weeks, months and business days between two dates. Option to include the end date. Free date duration calculator.",
short="Days, weeks and business days between two dates.",
ui="""
<div class="row">
 <div class="field"><label for="dd-a">Start date</label><input id="dd-a" type="date"></div>
 <div class="field"><label for="dd-b">End date</label><input id="dd-b" type="date"></div>
</div>
<label class="check"><input type="checkbox" id="dd-inc"> Include the end date (add 1 day)</label>
<div class="btns"><button class="btn" id="dd-go" type="button">Count days</button></div>
<div class="result" id="dd-out" aria-live="polite"></div>
""",
content="""
<p>Find out exactly how many days there are between two dates, along with the same span in weeks, months and years and the number of business days (Monday to Friday). It is useful for project deadlines, notice periods, countdowns to events and working out how long ago something happened.</p>
<h2>How to use it</h2>
<ol>
<li>Choose a start date and an end date. The order does not matter.</li>
<li>Tick “Include the end date” if both the first and last day should count, such as for a hotel stay or a leave request.</li>
<li>Click “Count days”.</li>
</ol>
<h2>Inclusive or exclusive?</h2>
<p>By default the calculator counts the gap between the dates, so from Monday to Friday is 4 days. If you are counting days you will actually be somewhere or working, include the end date and the answer becomes 5. Contracts and legal deadlines often specify which method applies, so check the wording.</p>
<h2>About business days</h2>
<p>Business days exclude Saturdays and Sundays. Public holidays vary by country and year, so they are not removed automatically. Subtract them yourself for an exact working-day count.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Does it handle leap years and daylight saving time?</summary><p>Yes. Dates are counted as calendar days, so leap days are included and clock changes do not shift the result.</p></details>
<details><summary>How are months counted?</summary><p>Complete calendar months are counted first, then the leftover days, the same way an age is calculated.</p></details>
</div>
"""),
# ---------------------------------------------------------------- unit converter
dict(
slug="unit-converter", name="Unit Converter", cat="convert", ico="Uc",
title="Unit Converter – Length, Weight, Temperature, Area, Volume, Speed",
desc="Convert between metric and imperial units: cm to inches, kg to lb, Celsius to Fahrenheit, square feet to square metres, litres to gallons and more.",
short="Length, weight, temperature, area, volume and speed.",
ui="""
<div class="field"><label for="uc-type">Measurement</label>
<select id="uc-type"><option value="length">Length</option><option value="mass">Weight / mass</option><option value="temp">Temperature</option><option value="area">Area</option><option value="volume">Volume</option><option value="speed">Speed</option></select></div>
<div class="row">
 <div class="field"><label for="uc-val">Value</label><input id="uc-val" type="number" step="any" value="1"></div>
 <div class="field"><label for="uc-from">From</label><select id="uc-from"></select></div>
 <div class="field"><label for="uc-to">To</label><select id="uc-to"></select></div>
</div>
<div class="btns"><button class="btn ghost" id="uc-swap" type="button">Swap units</button></div>
<div class="result" aria-live="polite"><div class="big" id="uc-out">—</div><div id="uc-all" style="margin-top:10px"></div></div>
""",
content="""
<p>The unit converter changes measurements between metric and imperial (US customary) units across six categories: length, weight, temperature, area, volume and speed. Pick a category, type a value and you see the converted figure instantly, plus a table of the same value in every other unit in that category.</p>
<h2>How to use it</h2>
<ol>
<li>Choose what you are measuring.</li>
<li>Enter the value and pick the units to convert from and to.</li>
<li>Use “Swap units” to reverse the direction.</li>
</ol>
<h2>Handy conversion factors</h2>
<ul>
<li>1 inch = 2.54 cm exactly, so 1 foot = 30.48 cm and 1 mile = 1.609344 km.</li>
<li>1 pound = 0.45359237 kg exactly, and 1 kg ≈ 2.2046 lb.</li>
<li>1 US gallon = 3.785411784 litres; a UK (imperial) gallon is larger at 4.54609 litres.</li>
<li>1 square metre ≈ 10.764 square feet, and 1 acre = 43,560 square feet.</li>
</ul>
<h2>Temperature is different</h2>
<p>Temperature scales have different zero points, so you cannot simply multiply:</p>
<div class="formula">°F = °C × 9/5 + 32<br>°C = (°F − 32) × 5/9<br>K = °C + 273.15</div>
<p>A quick mental check: 20 °C is a mild 68 °F, and 30 °C is a hot 86 °F.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Which gallon does the converter use?</summary><p>Both are available. Choose “US gallon” or “UK gallon” in the volume list.</p></details>
<details><summary>How precise are the results?</summary><p>Conversions use exact international definitions where they exist and are shown to up to six significant decimal places.</p></details>
</div>
"""),
# ---------------------------------------------------------------- color converter
dict(
slug="color-converter", name="Color Converter", cat="convert", ico="#",
title="Color Converter – HEX to RGB, RGB to HEX, HSL",
desc="Convert colors between HEX, RGB and HSL. Pick a color, preview it and check text contrast. Free color code converter for designers.",
short="Convert between HEX, RGB and HSL with a live preview.",
ui="""
<div class="row" style="align-items:end">
 <div class="field"><label for="co-pick">Pick a color</label><input id="co-pick" type="color" value="#2f5bea" style="width:100%;height:46px;border:1px solid var(--line);border-radius:8px;background:none"></div>
 <div class="field"><label for="co-hex">HEX</label><input id="co-hex" class="code" type="text" value="#2F5BEA"></div>
 <div class="field"><label for="co-rgb">RGB</label><input id="co-rgb" class="code" type="text"></div>
 <div class="field"><label for="co-hsl">HSL</label><input id="co-hsl" class="code" type="text"></div>
</div>
<p id="co-err" class="err" aria-live="polite"></p>
<div id="co-swatch" style="border-radius:12px;padding:28px;border:1px solid var(--line)">
 <div style="font-size:1.5rem;font-weight:700" id="co-sample">Sample text on this color</div>
 <div id="co-contrast" style="margin-top:6px"></div>
</div>
""",
content="""
<p>Designers and developers move between color formats all the time. This converter keeps HEX, RGB and HSL in sync: change any one and the others update, along with a preview swatch. It also tells you whether black or white text is more readable on that color and shows the contrast ratio.</p>
<h2>How to use it</h2>
<ol>
<li>Use the color picker, or type a value into the HEX, RGB or HSL box.</li>
<li>The other formats and the preview update automatically.</li>
<li>Copy whichever format your design tool or stylesheet needs.</li>
</ol>
<h2>The three formats</h2>
<ul>
<li><strong>HEX</strong> such as <code>#2F5BEA</code> writes red, green and blue as two hexadecimal digits each (00 to FF). It is the most common format in CSS and design apps.</li>
<li><strong>RGB</strong> such as <code>rgb(47, 91, 234)</code> gives the same three channels as numbers from 0 to 255.</li>
<li><strong>HSL</strong> such as <code>hsl(226, 82%, 55%)</code> describes hue (the position on the color wheel), saturation and lightness. It is the easiest format for making a lighter or darker shade of a color: just change the last number.</li>
</ul>
<h2>Contrast and accessibility</h2>
<p>The Web Content Accessibility Guidelines (WCAG) ask for a contrast ratio of at least 4.5:1 between normal text and its background, and 3:1 for large text. The preview checks both white and black text against your color and recommends the stronger one.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Can I enter 3-digit HEX codes?</summary><p>Yes. <code>#F80</code> is expanded to <code>#FF8800</code>.</p></details>
<details><summary>Do I need the # sign?</summary><p>No. The converter accepts HEX with or without it.</p></details>
</div>
"""),
# ---------------------------------------------------------------- base64
dict(
slug="base64-encoder-decoder", name="Base64 Encoder / Decoder", cat="dev", ico="64",
title="Base64 Encode and Decode Online – UTF-8 Safe",
desc="Encode text to Base64 or decode Base64 back to text. Supports UTF-8 characters and URL-safe Base64. Runs entirely in your browser.",
short="Encode text to Base64 or decode it back, UTF-8 safe.",
ui="""
<div class="field"><label for="b6-in">Input</label><textarea id="b6-in" class="code" placeholder="Text to encode, or Base64 to decode"></textarea></div>
<label class="check"><input type="checkbox" id="b6-url"> URL-safe (use - and _ , no padding)</label>
<div class="btns"><button class="btn" id="b6-enc" type="button">Encode</button><button class="btn" id="b6-dec" type="button">Decode</button><button class="btn ghost" id="b6-copy" type="button">Copy output</button></div>
<p id="b6-err" class="err" aria-live="polite"></p>
<div class="field"><label for="b6-out">Output</label><textarea id="b6-out" class="code" readonly></textarea></div>
""",
content="""
<p>Base64 turns any data into a string made of 64 safe characters: A–Z, a–z, 0–9, plus + and /. It is used to send binary data through systems that only handle text, such as email attachments, data URLs in web pages, and tokens in web APIs. This tool encodes text to Base64 and decodes it back, and it handles accented letters, Urdu, Arabic and emoji correctly by working in UTF-8.</p>
<h2>How to use it</h2>
<ol>
<li>Paste text into the input box and click Encode, or paste a Base64 string and click Decode.</li>
<li>Tick URL-safe if the string will go in a web address or a JSON Web Token.</li>
<li>Copy the output.</li>
</ol>
<h2>How Base64 works</h2>
<p>The encoder takes the input three bytes (24 bits) at a time and splits them into four groups of six bits. Each six-bit value, from 0 to 63, maps to one character of the Base64 alphabet. When the input length is not a multiple of three, “=” signs pad the end. That is why Base64 output is always about 33% longer than the original.</p>
<h2>Base64 is not encryption</h2>
<p>Anyone can decode Base64 instantly, so never use it to hide passwords or private data. It is an encoding for transport, not a security measure.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What does “invalid Base64” mean?</summary><p>The input contains characters outside the Base64 alphabet or has the wrong length. Check for missing characters at the end, or try ticking URL-safe if the string contains - or _.</p></details>
<details><summary>What is URL-safe Base64?</summary><p>It replaces + with - and / with _, and usually drops the = padding, so the result can sit inside a URL without extra encoding.</p></details>
</div>
"""),
# ---------------------------------------------------------------- timestamp
dict(
slug="unix-timestamp-converter", name="Unix Timestamp Converter", cat="dev", ico="Ts",
title="Unix Timestamp Converter – Epoch to Date and Date to Epoch",
desc="Convert Unix epoch timestamps (seconds or milliseconds) to human-readable dates in UTC and your local time zone, and dates back to timestamps.",
short="Epoch seconds or milliseconds to a readable date, and back.",
ui="""
<p>Current Unix time: <strong class="code" id="ts-now">—</strong></p>
<div class="field"><label for="ts-in">Timestamp (seconds or milliseconds)</label><input id="ts-in" class="code" type="text" inputmode="numeric" placeholder="1767225600"></div>
<div class="result" id="ts-out" aria-live="polite"></div>
<div class="field" style="margin-top:18px"><label for="ts-date">Date and time (your local time)</label><input id="ts-date" type="datetime-local" step="1"></div>
<div class="result" id="ts-out2" aria-live="polite"></div>
""",
content="""
<p>A Unix timestamp counts the seconds that have passed since 00:00:00 UTC on 1 January 1970, a moment known as the Unix epoch. Computers, databases and APIs store time this way because a single number is easy to compare and sort. This converter turns a timestamp into a readable date in both UTC and your own time zone, and turns a date back into a timestamp.</p>
<h2>How to use it</h2>
<ol>
<li>Paste a timestamp into the first box. The tool detects whether it is in seconds (10 digits) or milliseconds (13 digits).</li>
<li>Or pick a date and time in the second box to get its timestamp.</li>
</ol>
<h2>Seconds vs milliseconds</h2>
<p>Unix systems and most server languages, such as PHP and Python’s <code>time.time()</code>, work in seconds. JavaScript’s <code>Date.now()</code> and Java’s <code>System.currentTimeMillis()</code> return milliseconds. If a date comes out in the year 50,000 or in January 1970, you have probably mixed the two up.</p>
<h2>The year 2038 problem</h2>
<p>Older systems store the timestamp as a signed 32-bit integer, which runs out at 03:14:07 UTC on 19 January 2038. Modern systems use 64-bit numbers, which last for billions of years.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Do Unix timestamps include time zones?</summary><p>No. A timestamp is always UTC. The time zone only matters when you display it, which is why this tool shows both UTC and your local time.</p></details>
<details><summary>Do leap seconds count?</summary><p>No. Unix time ignores leap seconds, so every day is exactly 86,400 seconds.</p></details>
</div>
"""),
# ---------------------------------------------------------------- password
dict(
slug="password-generator", name="Password Generator", cat="generate", ico="**",
title="Strong Password Generator – Random & Secure",
desc="Generate strong, random passwords with your choice of length, letters, numbers and symbols. Uses your browser’s secure random generator.",
short="Strong random passwords with the options you choose.",
ui="""
<div class="result" style="display:block"><div class="big code" id="pw-out" style="font-size:1.4rem;word-break:break-all">—</div><div id="pw-strength" style="margin-top:6px"></div></div>
<div class="btns"><button class="btn" id="pw-go" type="button">Generate new</button><button class="btn ghost" id="pw-copy" type="button">Copy password</button></div>
<div class="field" style="margin-top:12px"><label for="pw-len">Length: <span id="pw-len-v">16</span></label><input id="pw-len" type="range" min="6" max="64" value="16" style="width:100%"></div>
<div class="row">
 <label class="check"><input type="checkbox" id="pw-up" checked> Uppercase A–Z</label>
 <label class="check"><input type="checkbox" id="pw-low" checked> Lowercase a–z</label>
 <label class="check"><input type="checkbox" id="pw-num" checked> Numbers 0–9</label>
 <label class="check"><input type="checkbox" id="pw-sym" checked> Symbols !@#$…</label>
 <label class="check"><input type="checkbox" id="pw-amb"> Avoid look-alikes (l, 1, O, 0)</label>
</div>
""",
content="""
<p>This password generator creates random passwords that are hard to guess and hard to crack. Choose the length and which character types to include, and a new password appears instantly. Passwords are made with <code>crypto.getRandomValues</code>, your browser’s cryptographically secure random number generator, and are never sent over the internet.</p>
<h2>How to use it</h2>
<ol>
<li>Set the length with the slider. 16 characters is a good default.</li>
<li>Choose the character types the website allows.</li>
<li>Click “Generate new” until you get one you like, then copy it into your password manager.</li>
</ol>
<h2>What makes a password strong</h2>
<p>Length matters most. Each extra character multiplies the number of possible passwords. A 16-character password using upper and lower case letters, numbers and symbols has about 104 bits of entropy, far beyond what any computer can try by brute force. A short password made from a real word, a name or a date can be guessed in seconds because attackers start with lists of common choices.</p>
<h2>Good password habits</h2>
<ul>
<li>Use a different password for every account, so one leak does not unlock everything.</li>
<li>Store them in a password manager rather than a notebook or spreadsheet.</li>
<li>Turn on two-factor authentication wherever it is offered.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is it safe to generate a password on a website?</summary><p>On this page the password is created by your own browser and never leaves your device. You can even disconnect from the internet after the page loads and it still works.</p></details>
<details><summary>What does the strength meter measure?</summary><p>It estimates entropy in bits from the length and the size of the character set. Above 80 bits is very strong for everyday accounts.</p></details>
</div>
"""),
# ---------------------------------------------------------------- QR code
dict(
slug="qr-code-generator", name="QR Code Generator", cat="generate", ico="Qr",
title="Free QR Code Generator – URL, Text, Wi-Fi (PNG Download)",
desc="Create QR codes for websites, text, email, phone numbers and Wi-Fi networks. Choose size and colors and download as PNG. No sign-up, no expiry.",
short="QR codes for links, text and Wi-Fi, downloadable as PNG.",
ui="""
<div class="field"><label for="qr-type">QR code for</label>
<select id="qr-type"><option value="url">Website link</option><option value="text">Plain text</option><option value="wifi">Wi-Fi network</option><option value="tel">Phone number</option><option value="email">Email address</option></select></div>
<div id="qr-f-main" class="field"><label for="qr-in" id="qr-in-lbl">Website link</label><input id="qr-in" type="text" value="https://example.com"></div>
<div id="qr-f-wifi" class="row" hidden>
 <div class="field"><label for="qr-ssid">Network name (SSID)</label><input id="qr-ssid" type="text"></div>
 <div class="field"><label for="qr-pass">Password</label><input id="qr-pass" type="text"></div>
 <div class="field"><label for="qr-enc">Security</label><select id="qr-enc"><option>WPA</option><option>WEP</option><option value="nopass">None</option></select></div>
</div>
<div class="row">
 <div class="field"><label for="qr-size">Size (px)</label><select id="qr-size"><option>256</option><option selected>512</option><option>1024</option></select></div>
 <div class="field"><label for="qr-fg">Color</label><input id="qr-fg" type="color" value="#1b2540" style="width:100%;height:42px"></div>
 <div class="field"><label for="qr-bg">Background</label><input id="qr-bg" type="color" value="#ffffff" style="width:100%;height:42px"></div>
</div>
<div style="text-align:center;margin-top:10px"><canvas id="qr-canvas" width="512" height="512" style="width:240px;height:240px;border:1px solid var(--line);border-radius:8px"></canvas></div>
<p id="qr-err" class="err" aria-live="polite"></p>
<div class="btns" style="justify-content:center"><button class="btn" id="qr-dl" type="button">Download PNG</button></div>
""",
content="""
<p>Make a QR code for a website, a message, a phone number, an email address or your Wi-Fi network. The code updates as you type, and you can download it as a sharp PNG image for printing on menus, flyers, business cards or packaging. Codes made here are static: they contain the data directly, never expire and do not route through any tracking service.</p>
<h2>How to use it</h2>
<ol>
<li>Choose what the QR code is for.</li>
<li>Fill in the link, text or Wi-Fi details.</li>
<li>Pick a size and colors, then click “Download PNG”.</li>
<li>Scan it with your phone camera to test before you print.</li>
</ol>
<h2>Tips for QR codes that scan every time</h2>
<ul>
<li><strong>Keep strong contrast.</strong> A dark code on a light background works best. Some phone cameras cannot read light codes on dark backgrounds.</li>
<li><strong>Print big enough.</strong> A common rule is that the code should be at least one tenth of the distance it will be scanned from. For a poster read from 2 metres, aim for 20 cm.</li>
<li><strong>Leave a quiet zone.</strong> Keep a clear margin around the code free of text or graphics. The generator adds one automatically.</li>
<li><strong>Shorter data, simpler code.</strong> Long URLs make dense codes that are harder to scan when printed small.</li>
</ul>
<h2>How Wi-Fi QR codes work</h2>
<p>A Wi-Fi code stores the network name, password and security type in a standard format. When guests scan it, Android and iPhone cameras offer to join the network without typing the password.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Do these QR codes expire?</summary><p>No. The information is stored inside the image itself, so the code works for as long as the link or details inside it are valid.</p></details>
<details><summary>Can I use them commercially?</summary><p>Yes. QR codes you create here are free to use on anything, including printed products and packaging.</p></details>
<details><summary>Can I change the link after printing?</summary><p>No, static codes cannot be edited. If you need to change the destination later, point the code to a page on your own website that you can update or redirect.</p></details>
</div>
"""),
# ---------------------------------------------------------------- random number
dict(
slug="random-number-generator", name="Random Number Generator", cat="generate", ico="Rn",
title="Random Number Generator – Pick Numbers in Any Range",
desc="Generate random numbers between any minimum and maximum, with or without repeats. Pick lottery numbers, draw winners or roll dice.",
short="Random numbers in any range, with or without repeats.",
ui="""
<div class="row">
 <div class="field"><label for="rn-min">Minimum</label><input id="rn-min" type="number" value="1"></div>
 <div class="field"><label for="rn-max">Maximum</label><input id="rn-max" type="number" value="100"></div>
 <div class="field"><label for="rn-n">How many</label><input id="rn-n" type="number" min="1" max="1000" value="1"></div>
</div>
<label class="check"><input type="checkbox" id="rn-uniq" checked> No repeats</label>
<label class="check"><input type="checkbox" id="rn-sort"> Sort results</label>
<div class="btns"><button class="btn" id="rn-go" type="button">Generate</button><button class="btn ghost" id="rn-copy" type="button">Copy</button></div>
<p id="rn-err" class="err" aria-live="polite"></p>
<div class="result"><div class="big code" id="rn-out" style="word-break:break-word">—</div></div>
""",
content="""
<p>Pick one or many random whole numbers between any two limits. Use it to choose a giveaway winner from numbered entries, assign groups in a classroom, pick lottery-style numbers or settle who goes first. The generator uses your browser’s secure random source, so every number in the range has an equal chance.</p>
<h2>How to use it</h2>
<ol>
<li>Set the lowest and highest number you want. Both are included.</li>
<li>Choose how many numbers to draw.</li>
<li>Keep “No repeats” ticked to draw like a raffle, where each number can come up only once.</li>
<li>Click Generate.</li>
</ol>
<h2>Fair and unbiased</h2>
<p>A naive approach to random numbers can make some values slightly more likely than others when the range does not divide evenly into the generator’s output. This tool uses rejection sampling, discarding the few raw values that would cause that bias, so the draw is uniform across the whole range.</p>
<h2>Ideas for using it</h2>
<ul>
<li>Run a social media giveaway: number the qualifying comments and draw one.</li>
<li>Roll dice: set 1 to 6 and allow repeats.</li>
<li>Choose a random page or question for revision practice.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Are these truly random?</summary><p>They come from a cryptographically secure pseudo-random generator built into your browser, which is suitable for draws, games and most security needs.</p></details>
<details><summary>Why do I get an error with “No repeats”?</summary><p>You asked for more unique numbers than the range contains. For example, there are only 10 numbers from 1 to 10.</p></details>
</div>
"""),
# ---------------------------------------------------------------- json
dict(
slug="json-formatter", name="JSON Formatter & Validator", cat="dev", ico="{}",
title="JSON Formatter and Validator – Beautify or Minify JSON",
desc="Format, validate and minify JSON online. Shows the exact line and column of syntax errors. Works offline in your browser.",
short="Beautify, minify and validate JSON with clear errors.",
ui="""
<div class="field"><label for="js-in">JSON</label><textarea id="js-in" class="code" placeholder='{"name":"SmartToolsy","tools":20}'></textarea></div>
<div class="row" style="align-items:end">
 <div class="field"><label for="js-ind">Indent</label><select id="js-ind"><option value="2">2 spaces</option><option value="4">4 spaces</option><option value="tab">Tab</option></select></div>
 <label class="check"><input type="checkbox" id="js-sort"> Sort keys A–Z</label>
</div>
<div class="btns"><button class="btn" id="js-fmt" type="button">Format</button><button class="btn" id="js-min" type="button">Minify</button><button class="btn ghost" id="js-copy" type="button">Copy output</button></div>
<p id="js-msg" aria-live="polite"></p>
<div class="field"><label for="js-out">Output</label><textarea id="js-out" class="code" readonly></textarea></div>
""",
content="""
<p>Paste JSON from an API response, a config file or a log and this tool makes it readable with consistent indentation, or squeezes it into one line to save space. It also validates the JSON and, when something is wrong, points to the line and column where the problem starts.</p>
<h2>How to use it</h2>
<ol>
<li>Paste your JSON into the input box.</li>
<li>Click Format to pretty-print it, or Minify to remove all whitespace.</li>
<li>Optionally sort object keys alphabetically to make two files easier to compare.</li>
</ol>
<h2>Common JSON errors</h2>
<ul>
<li><strong>Trailing commas.</strong> <code>[1, 2, 3,]</code> is valid in JavaScript but not in JSON.</li>
<li><strong>Single quotes.</strong> JSON strings and keys must use double quotes.</li>
<li><strong>Unquoted keys.</strong> <code>{name: "x"}</code> must be written <code>{"name": "x"}</code>.</li>
<li><strong>Comments.</strong> Standard JSON has no comments. Remove lines starting with // before validating.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is my data uploaded?</summary><p>No. Parsing uses your browser’s built-in JSON engine, so API keys or customer data in the JSON never leave your computer.</p></details>
<details><summary>How large a file can it handle?</summary><p>Several megabytes is fine in a modern browser. Very large files may take a moment to format.</p></details>
</div>
"""),
# ---------------------------------------------------------------- image compressor
dict(
slug="image-compressor", name="Image Compressor", cat="image", ico="Im",
title="Image Compressor – Reduce JPG, PNG & WebP File Size Online",
desc="Compress and resize images in your browser. Reduce JPG, PNG and WebP file size with adjustable quality. No upload, completely private.",
short="Shrink JPG, PNG and WebP images without uploading them.",
ui="""
<div class="field"><label for="im-file">Choose an image</label><input id="im-file" type="file" accept="image/jpeg,image/png,image/webp"></div>
<div class="row">
 <div class="field"><label for="im-q">Quality: <span id="im-q-v">75</span>%</label><input id="im-q" type="range" min="10" max="100" value="75" style="width:100%"></div>
 <div class="field"><label for="im-w">Max width (px)</label><input id="im-w" type="number" min="16" placeholder="Keep original"></div>
 <div class="field"><label for="im-fmt">Output format</label><select id="im-fmt"><option value="image/jpeg">JPG</option><option value="image/webp">WebP</option><option value="image/png">PNG</option></select></div>
</div>
<p id="im-msg" aria-live="polite" class="count-note"></p>
<div id="im-prev" hidden>
 <div class="stats"><div class="stat"><b id="im-o">—</b><span>Original</span></div><div class="stat"><b id="im-n">—</b><span>Compressed</span></div><div class="stat"><b id="im-s">—</b><span>Saved</span></div></div>
 <img id="im-img" alt="Compressed image preview" style="margin-top:14px;border-radius:8px;border:1px solid var(--line);max-height:360px;object-fit:contain">
 <div class="btns"><a class="btn" id="im-dl" download>Download image</a></div>
</div>
""",
content="""
<p>Large photos slow down websites, bounce back from email size limits and eat phone storage. This image compressor reduces the file size of JPG, PNG and WebP images right in your browser. Your image is never uploaded to a server, which makes it fast and keeps private photos private.</p>
<h2>How to use it</h2>
<ol>
<li>Choose an image from your device.</li>
<li>Adjust quality. Around 70–80% usually looks the same as the original at a fraction of the size.</li>
<li>Optionally set a maximum width. Resizing a 4000-pixel camera photo to 1600 pixels is often the biggest saving.</li>
<li>Pick JPG, WebP or PNG and download the result.</li>
</ol>
<h2>Which format should I choose?</h2>
<ul>
<li><strong>JPG</strong> is best for photos and works everywhere.</li>
<li><strong>WebP</strong> is a modern format that is typically 25–35% smaller than JPG at similar quality. All current browsers support it, which makes it ideal for websites.</li>
<li><strong>PNG</strong> is lossless and supports transparency, so it suits logos, screenshots and graphics with sharp edges. The quality slider does not shrink PNGs; resize them instead, or convert photos to JPG or WebP.</li>
</ul>
<h2>Why image size matters for websites</h2>
<p>Images are usually the heaviest part of a web page. Google uses page speed signals such as Largest Contentful Paint in its ranking systems, and visitors on mobile data leave slow pages quickly. Compressing images before uploading them is one of the easiest speed improvements you can make.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Are my images uploaded anywhere?</summary><p>No. Compression uses the HTML canvas in your browser. The image never leaves your device.</p></details>
<details><summary>Why did my file get bigger?</summary><p>If the original was already well compressed, re-saving at high quality or converting to PNG can increase the size. Lower the quality or choose JPG or WebP.</p></details>
<details><summary>Does it keep photo metadata?</summary><p>No. Location, camera and other EXIF data are removed, which is good for privacy when sharing photos online.</p></details>
</div>
"""),
]
