# Game of Dice.
import random
num=int(input("Enter the number of times to roll the dice: "))
for i in range(num):
    dice=random.randint(1, 6)
    if(dice==1):
        print(" ------- ")
        print("|       |")
        print("|   ●   |")
        print("|       |")
        print(" ------- ")
        print('\n')
    elif(dice==2):
        print(" -------- ")
        print("| ●      |")
        print("|        |")
        print("|      ● |")
        print(" -------- ")
        print('\n')
    elif(dice==3):
        print(" ------- ")
        print("| ●     |")
        print("|   ●   |")
        print("|     ● |")
        print(" ------- ")
        print('\n')
    elif(dice==4):
        print(" ------- ")
        print("| ●   ● |")
        print("|       |")
        print("| ●   ● |")
        print(" ------- ")
        print('\n')
    elif(dice==5):
        print(" ------- ")
        print("| ●   ● |")
        print("|   ●   |")
        print("| ●   ● |")
        print(" ------- ")
        print('\n')
    else:
        print(" ------- ")
        print("| ●   ● |")
        print("| ●   ● |")
        print("| ●   ● |")
        print(" ------- ")
        print('\n')

