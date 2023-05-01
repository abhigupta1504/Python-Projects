# Rock, paper or scissor game.
import random
options=["rock","paper","scissor"]
while(True):
    user=input("Choose rock, paper, or scissor: ")
    print('\n')
    computer=random.choice(options)
    print("You choose:",user)
    print("Computer choose:",computer)
    if user==computer:
        print('\n')
        print("It's a tie!")
    elif user=="rock":
        if computer=="paper":
            print('\n')
            print("You lose!")
            break
        else:
            print('\n')
            print("You win!")
    elif user=="paper":
        if computer=="scissor":
            print('\n')
            print("You lose!")
            break
        else:
            print('\n')
            print("You win!")
    elif user=="scissor":
        if computer=="rock":
            print('\n')
            print("You lose!")
            break
        else:
            print('\n')
            print("You win!")
    else:
        print("Invalid input. Please choose rock, paper, or scissor.")
    print('\n')
    play_again = input("Do you want to play again? (y/n) : ")
    if play_again!="y":
        break


