# Guess the number game.
import random
print('*******Welcome to Guess the Number Game*******'.center(100))
print('Rules : ',' * Max score :: 100',' * Every wrong guess will reduce 5 points.',sep='\n')
def game():
    a=random.randint(1,100)
    c=0
    d=0
    k=0
    while(a!=d):
        print('\nGuess the number :: ',end='')
        b=int(input())
        if a==b:
            print('Congrats!! you win')
            print('The No.is:',a)
            k=1
        elif a>b and a-b>=10:
            print('Smaller and far from the number....')
            c+=1
        elif a>b and a-b<10:
            print('Smaller but close to the number....')
            c+=1
        elif a<b and b-a>=10:
            print('Greater and far from the number....')
            c+=1
        else:
            print('Greater but close to the number....')
            c+=1
        d=b
    if k==1:
        print('You got it :')
        print('Max score :: 100',f"Your score :: {100-c*5}")
        print('\nDo you want to play again? :: (y/n)')
        y=input()
        return y
print('\n')
print('Do you want to play? (y/n) ')
per=input()
if per=='y' or per=='Y':
    re=game()
    print(re)
    while(re not in 'Nn'):
        re=game()
    print('\nThank You!'.rjust(30))    
else:
    print('\nThank You!'.rjust(30))
        
    
    