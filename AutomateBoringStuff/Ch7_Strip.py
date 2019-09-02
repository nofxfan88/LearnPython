#! python3
import re

def regexStrip(line, *args):

    result = line

    if len(args) > 0:
        chars = args[0]
    else:
        chars = ' '

    if chars == ' ':
        regex = re.compile(r'^\s*(\w*)\s*$')
        result = regex.sub(r'\1', result)
    else:
        # inject chars in a character class, then grab anything other than
        # chars in a non-greedy fashion (otherwise .* would grab everything
        # else)
        regex = re.compile(r'^[' + chars + ']*(.*?)[' + chars + ']*$')
        result = regex.sub(r'\1', result)

    return result

line = 'abc21test123abc12a'
print(line)
print(regexStrip(line, 'ba12c'))
