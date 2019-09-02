#! python3

# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage; py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to the clipboard.

import shelve, pyperclip, sys, os

directory = os.path.join('C:\\', 'Users', 'bribake2', 'Documents', 'Github',
    'LearnPython', 'AutomateBoringStuff', 'Ch8 stuff')
mcbShelf = shelve.open(os.path.join(directory, 'mcb'))

# 2 argument cases
if len(sys.argv) == 3:
    # save clipboard keyword
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # delete keyword entry
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
# 1 argument cases
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # delete all keywords
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
