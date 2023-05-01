# OTP or Captcha Verification.
import random
import string
length=6
code_type=random.randint(1, 3)
if code_type==1:
    digits = random.sample(range(0, 9), length)
    code="".join(map(str, digits))
    print("Enter OTP:", code)
    user_input=input()
elif code_type==2:
    captcha="".join(random.choices(string.ascii_letters + string.digits, k=length))
    print("Enter captcha:", captcha)
    user_input=input()
else:
    digits=random.sample(range(0, 9), length)
    otp="".join(map(str, digits))
    captcha="".join(random.choices(string.ascii_letters + string.digits, k=length))
    print("OTP:", otp)
    print("Enter the OTP:")
    user_input1=input()
    print("Captcha:", captcha)
    print("Enter the Captcha:")
    user_input2=input()
    user_input=[user_input1,user_input2]
if code_type==1 and user_input==code:
    print("OTP accepted!")
elif code_type==2 and user_input==captcha:
    print("Captcha accepted!")
elif code_type==3 and user_input==[otp, captcha]:
    print("OTP and Captcha accepted!")
else:
    print("Code incorrect.")