import random

integer_519 = random.randint(0,100)


while True:
    input_519 = int(input("Guess a number:"))
    if(input_519 < integer_519):
        print("Go higher!")
        continue
    elif(input_519 > integer_519):
        print("Go lower!")
        continue
    else:
        print("You guessed right!")
        break