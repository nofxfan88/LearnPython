def convert(spam):

    sentence = ''
    for word in spam[:-1]:
        sentence += str(word) + ', '

    sentence += 'and ' + str(spam[-1])
    return sentence

spam = [1, 2, 3, 4]

print(convert(spam))
