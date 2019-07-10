s = 'azcbobobegghakl' #test string

i = 0
longest = ''

while i < len(s):
    contender = ''
    for char in s[i : len(s)]:
        if contender == '':
            contender += char
        elif char >= contender[len(contender) - 1]:
            contender += char
        else:
            break
    if len(contender) > len(longest):
        longest = contender
    i += 1

print('Longest substring in alphabetical order is: ' + longest)
