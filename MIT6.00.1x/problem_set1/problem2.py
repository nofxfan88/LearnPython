s = 'azcbobobegghakl' #test input

word = 'bob'
wordCount = 0
index = 0

while (index + len(word)) <= len(s):
    if s[index:index + len(word)] == 'bob':
        wordCount += 1
    index += 1

print('Number of times ' + word + ' occurs is: ' + str(wordCount))
