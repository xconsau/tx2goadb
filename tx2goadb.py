# tx to GlyphOrderAndAliasDB
# Strips raw data of tx output in a format
# required by GlyphOrderAndAliasDB file


import re
import sys
import os.path

count = 0

# Read input file
if os.path.isfile('tx.txt'):
	
	file1 = open('tx.txt', 'r')
	Lines = file1.readlines()

	# Output file to write on
	f = open("GlyphOrderAndAliasDB", "w")

	# Parse and strip content
	for line in Lines:
		txt = line.strip()
		
		# .notdef
		if count == 0:
			txt = txt.replace(",0x01", "")
		
		st = "glyph[{}]"
		rep = st.format(count)
		txt = txt.replace(rep, "")
		txt = txt.replace("{", "")
		txt = txt.replace(",-", "")
		txt = txt.replace(",U+", " uni")
		txt = txt.replace("}", "")

		# Double glyph names for second column entry
		first_word = txt.split()[0]
		txt = txt.replace(first_word, first_word + "\t" + first_word + "\t", 1)

		count+= 1
		f.write(txt + "\n")
	sys.exit('Success: File GlyphOrderAndAliasDB generated.')
else:
	sys.exit('Error: Could not find source file tx.txt')