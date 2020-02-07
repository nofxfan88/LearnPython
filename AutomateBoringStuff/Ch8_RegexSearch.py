#! python3

# Search all files in a supplied folder, or current folder if none supplied
# for occurrences of a supplied regex pattern
import sys, re, os

def filterExtension(directory, extension):
    result = []
    regex = re.compile(r'.*' + extension)
    for filename in os.listdir(directory):
        if regex.match(filename):
            result.append(filename)

    return result

# Get user input of Regex pattern and folder to search.
searchFolder = ''

print(sys.argv)

if len(sys.argv) == 3:
    if not os.path.exists(sys.argv[2]):
        print('Folder does not exist')
        exit()
    searchFolder = os.path.abspath(sys.argv[2])
elif len(sys.argv) == 2:
    searchFolder = os.getcwd()
else:
    print('Usage: python Ch8_RegexSearch.py <regex> [folder]')

try:
    userRegex = re.compile(sys.argv[1])
except Exception as e:
    print('Invalid Regex pattern')
    exit()

# TODO: Loop through files print out matching lines with line numbers
# and file that matched.

for filename in filterExtension(searchFolder, '.txt'):
    file = open(os.path.join(searchFolder, filename))

    matches = []
    lineNum = 1

    for line in file:
        if userRegex.search(line):
            matches.append(str(lineNum) + ' ' + line)
        lineNum += 1
    if len(matches) > 0:
        print(filename)
        for line in matches: print(line, end='')
    file.close()

print(sys.argv)
