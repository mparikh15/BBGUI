x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
guess = (high + low ) / 2.0


while abs(guess**2 - x) >= epsilon:
    print ('low = ' + str(low) + 'high =' + str(high) + 'Guess = ' + str(guess))
    numGuesses += 1
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0

print ('numGuesses = ' + str(numGuesses))
print (str(ans) + ' is close to the square root of ' + str(x))
