#! python3
import re, os

# Function applied during regex sub()
def madReplace(m):
    word = m.group(0).lower()

    if re.compile(r'^[aeiou]').match(word):
        print('Enter an %s:' % word)
    else:
        print('Enter a %s:' % word)

    return input()

# Create Regex to match ADJECTIVE, VERB, NOUN, ADVERB
madRegex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

#  Open input and output text files.
directory = os.path.join('C:\\', 'Users', 'bribake2', 'Documents', 'Github',
    'LearnPython', 'AutomateBoringStuff', 'Ch8 stuff')
inputFile = open(os.path.join(directory, 'mad_lib.txt'))
outputFile = open(os.path.join(directory, 'mad_lib_filled.txt'), 'w')

# Go through input line, apply regex.sub(), write to output file

for line in inputFile:
    outputFile.write(madRegex.sub(madReplace, line))

inputFile.close()
outputFile.close()
