#! python3

import re

def testPassword(password):
    upperRegex = re.compile(r'[A-Z]+')
    lowerRegex = re.compile(r'[a-z]+')
    numberRegex = re.compile(r'[0-9]+')

    return (len(password) >= 8 and upperRegex.search(password) and
        lowerRegex.search(password) and numberRegex.search(password))

password = 'Passw0rd'

if testPassword(password):
    print('Great password!')
else:
    print('Error: password must contain at least 1 upper case and 1 lower case letter,')
    print('and at least 1 number')
