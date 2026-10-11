import random
playing = True
number = str(random.randint(0,9))
print("im gonna pick a number from 0 to 9 and u have to guess it")
while playing:
    guess=int(input("GUESS"))
    if number == guess:
        print("U won")
        print("the number was=",number)
        break
    else:
        print("WRONG HAHAHA")
        