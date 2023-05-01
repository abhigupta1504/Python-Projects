# Hangman Game.
import random
def out(ls,e):
    f,u=0,0
    for i in ls:
        if i in e[-1]:
            f=1
    for i in ls:
        if i in e:
            print(i,end='')
            continue
        else:
            print('_',end='')
            u+=1
            continue
    print()
    t=(f,u)
    return t
easy=['AND','FIX','OWN','ARE','FLY','ODD','APE','FRY','OUR','ACE','FOR','PET','ACT','GOT','PAT','ASK','GET','PEG','ARM','GOD','PAW','AGE','GEL','PUP','AGO','GAS','PIT','AIR','HAT','PUT','ATE','HIT','POT','ALL','HAS','POP','BUT','HAD','PIN']
medium=['BAKE','WORD','LIST','FOUR','FIVE','NINE','GOOD','BEST','CUTE','ZERO','HUGE','COOL','TREE','RACE','RICE','KEEP','LACE','BEAM','GAME','MARS','TIDE','RIDE','HIDE','EXIT','HOPE','COLD','FROM','NEED','STAY','COME']
hard=['ABOUT','ALERT','ARGUE','BEACH','CARRY','CLAIM','CREAM','DEBUT','ENTRY','FORTH','GROUP','DELAY','EQUAL','FORTY','GROWN','JUDGE','METAL','MEDIA','NEWLY','POWER','RADIO','ROUND','PANEL','PRESS','RAISE','ROUTE','PHASE','PRICE']
print("Rules : ")
print(' * You were travelling through the woods when you were hit on the back of your head and find out that a witch caught you....'.rjust(65))
print(' * Your friend is trying to save you from the witch but you must distract her to ambush her. Answer correctly to save yourself from being hanged...\n'.rjust(65))
print('\n')
print('Do you want to play?  (YES/NO)',end='',sep='  ')
s=input()
while s in 'YESyes':
    print('\n')
    print('Choose Level : \n 1: Easy  \n 2: Medium \n 3: Hard \n'.rjust(40))
    n=int(input())
    if n==1:
        word=random.choice(easy)
    elif n==2:
        word=random.choice(medium)
    elif n==3:
        word=random.choice(hard)
    else:
        print('Choose from 1,2 or 3')
        continue
    l=[]
    l.extend(word)
    let=random.choice(l)
    chk=out(l,let)
    c=10
    wrong=[]
    temp2=let
    while(c>=0):
        temp=temp2
        print('You Choose : ')
        s2=input()
        s2=s2.upper()
        temp=temp+s2
        print(temp)
        chk,u=out(l,temp)
        print(chk,u)
        if chk==0:
            temp=''
            wrong.append(s2)
        temp2+=temp
        c-=1
        print('Wrong Guesses:',*wrong)
        if u==0:
            print('You were able to defeat the match!!!'.rjust(65))
            print(f'System choose : {word}'.rjust(65))
            break
        elif c==9:
            print("         \n"
                  "         \n"
                  "         \n"
                  " ========\n")
            continue
        elif c==8:
            print("        |\n"
                  "        |\n"
                  "        |\n"
                  " ========\n")
            continue
        elif c==7:
            print("--------|\n"
                  "        |\n"
                  "        |\n"
                  " =======|\n")
            continue
        elif c==6:
            print("--------|\n"
                 " O      |\n"
                  "        |\n"
                  " =======|\n")
            continue
        elif c==5:
            print("--------|\n"
                 " O      |\n"
                 " |      |\n"
                  " =======|\n")
            continue
        elif c==4:
            print("--------|\n"
                 " O      |\n"
                "/|      |\n"
                  " =======|\n")
            continue
        elif c==3:
            print("--------|\n"
                 " O      |\n"
                "/|\     |\n"
                  " =======|\n")
            continue
        elif c==2:
            print("--------|\n"
                 " O      |\n"
                "/|\     |\n"
               "/=======|\n")
            continue
        elif c==1:
            print("--------|\n"
                 " O      |\n"
                "/|\     |\n"
                "/ \=====|\n")
            continue
        elif c==0:
            print("--------|\n"
                  "|       |\n" 
                  "|       |\n"
                  "O =======\n"
                "/|\       \n"
                 "/ \ \n")
            print('You failed to defeat the witch....'.rjust(65))
            print(f'System choose : {word} '.rjust(65))
            break
    print('\n')
    s=input("Do you want to play again? (Y/N)")
print("Thanks for playing!!!".rjust(65))
