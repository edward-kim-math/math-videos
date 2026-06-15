#!/usr/bin/env python3

import re
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: python extract_brackets.py <filename>")
    sys.exit(1)

infile = Path(sys.argv[1])

if not infile.exists():
    print(f"File not found: {infile}")
    sys.exit(1)

text = infile.read_text(encoding="utf-8")

# Find all occurrences of text inside [...]
#matches = re.findall(r'\[([^\[\]]*)\]', text)

# Find all occurences of text inside \note[item]{\alert<number>{text to extract}}
matches = re.findall(r'\\note\[item\]\{\\alert<\d+>\{([^{}]*)\}\}', text)

outfile = infile.with_suffix(".txt")

with open(outfile, "w", encoding="utf-8") as f:
    for match in matches:
        f.write(match + "\n")

print(f"Wrote {len(matches)} notes to {outfile}")



