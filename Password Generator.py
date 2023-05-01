# Secure Password Generator.
import random
import string
length = random.randint(8,12)
part = length//4
left = length%4
lower = ''.join((random.choice(string.ascii_lowercase) for x in range(part)))
uppar = ''.join((random.choice(string.ascii_uppercase) for x in range(part)))
nums = ''.join((random.choice(string.digits) for x in range(part)))
if(left == 0):
   chrs = ''.join((random.choice(string.punctuation) for x in range(part)))
else:
   chrs = ''.join((random.choice(string.punctuation) for x in range(left)))
password = lower + uppar + nums + chrs
temp = list(password)
random.shuffle(temp)
password = ''
for i in temp:
   password += i
print("Press enter to generte password",end='')
input()
print('\n')
print("\t\t\tPassword : " + password)