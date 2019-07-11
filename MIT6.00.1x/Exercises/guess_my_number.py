print('Please think of a number between 0 and 100!')

low = 0
high = 100

reply = ''
prompt = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "

guess = int((high + low) / 2)

while reply != 'c':
    print('Is your secret number ' +  str(guess) + '?')
    reply = input(prompt)

    if reply == 'h':
        high = guess
        guess = int((high + low) / 2)
    elif reply == 'l':
        low = guess
        guess = int((high + low) / 2)
    elif reply == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: ' + str(guess))
