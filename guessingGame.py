import random
number = random.randint(1, 9)
chanceCount = 0
while chanceCount < 5:
    introString = int(input("enter the number between 1 and 9: "))
    if (introString > number):
        print("Your guess is too large")
    elif (introString == number):
        print("Congratulations! You guessed it correctly")
        break:
    else :
        print("YOU LOST!!")
    chanceCount = chanceCount + 1
    
