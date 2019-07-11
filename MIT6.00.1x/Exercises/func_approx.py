x = .006

low = 0
high = 1
epsilon = 0.00001

numguesses = 0

guess = (high + low) / 2.0

while abs(guess**2 - x) >= epsilon:
    if guess**2 < x :
        low = guess
    else:
        high = guess

    guess = (high + low) / 2.0
    numguesses += 1

print ("Number of guesses = " + str(numguesses))
print ("Approximate value = " + str(guess))
