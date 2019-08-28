filename = 'myfile.txt'
message = 'Hello file world!'

file = open(filename, 'w')
file.write(message + '\n')
file.close()
