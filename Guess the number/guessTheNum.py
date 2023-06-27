import random
import math

def GuessTheNumber(upper, lower):
    x = random.randint(lower,upper)
    chances = round(math.log(upper-lower+1,2))
    print("\n\tYou've only",
          chances,
          " chances to guess the integer\n")
    count = 0
    while count< chances:
        count+=1
        guess = int(input("Guess the number: "))

        if x == guess:
            print("Congratulations you did it in ",
              count, " try")
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
    
    if count >= chances:
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")


lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
GuessTheNumber(upper, lower)