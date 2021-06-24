TX to GlyphOrderAndAliasDB
===============================================

tx2goadb is a small script for stripping raw dump data of tx tool in ADFDKO. This script was created to generate a format as required in GlyphOrderAndAliasDB file for adding OpenType features to a font file.

The [AFDKO](https://adobe-type-tools.github.io/afdko/AFDKO-Overview.html) is a set of tools for building OpenType font files from PostScript and TrueType font data.

## Usage

- Make sure you are in the virtual environment of AFDKO:

    - macOS & Linux

            source afdko_env/bin/activate

    - Windows

            afdko_env\Scripts\activate.bat


- Extract glyphs data from font object
	
		tx -dump -4 your_font_file.ttf

- Copy the output in a text file and name it <code>tx.txt</code>. The format of this file will be like shown below:

<pre>glyph[0] {.notdef,0x01}
glyph[1] {.null,U+0000}
glyph[2] {uni000D,U+000D}
glyph[3] {space,U+0020}
glyph[4] {S,U+0053}
...</pre>

- From the same source folder, generate 'GlyphOrderAndAliasDB' file by running this script
		
		tx2goadb.py

- A new file named 'GlyphOrderAndAliasDB' will be generated in the same folder. The stripped format will be as shown below:

<pre> .notdef	.notdef	
 .null	.null	 uni0000
 uni000D	uni000D	 uni000D
 space	space	 uni0020
 S	S	 uni0053
 M	M	 uni004D
 g	g	 uni0067</pre>

 - Use GlyphOrderAndAliasDB, features.fea and other feature files for adding OpenType features to the existing font file using [makeotf](http://adobe-type-tools.github.io/afdko/MakeOTFUserGuide.html)
