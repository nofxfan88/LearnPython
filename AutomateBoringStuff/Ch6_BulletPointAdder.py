#! python3
# Ch6_BulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the Clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
