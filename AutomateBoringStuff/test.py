import re, os

def madReplace(m):
    return m.group(0).lower()

testString = '''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
    unaffected by these events.'''

madRegex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

directory = os.path.join('C:\\', 'Users', 'bribake2', 'Documents', 'Github',
    'LearnPython', 'AutomateBoringStuff', 'Ch8 stuff')
inputFile = open(os.path.join(directory, 'mad_lib.txt'))

for line in inputFile:
    print(line)
