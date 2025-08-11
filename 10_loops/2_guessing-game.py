import random 
jackpot = random.randint(1,100)

guess = int(input("Enter your lucky number: "))

i =1
while guess != jackpot:
    print("You took {0} attempt".format(i))
    if(guess<jackpot):
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input("Enter your lucky number: "))
    i = i+1
print("You got the answer")
print("You took {0}th attempt".format(i))