#TASK-3 :PASSWORD GENERATOR 
#IMPORTING THE ESSENTIAL MODULES
import random
import string
#FUCNTION DEFINING THE PASSWORD
def gen_password(min_length,numbers=True,spl_char=True):
    letters=string.ascii_letters
    digits=string.digits
    spl=string.punctuation
    characters=letters
    if numbers:
        characters +=digits
    if spl_char:
        characters+=spl
    pwd=""
    meets_criteria=False
    has_number=False 
    has_spl=False
    while not meets_criteria or len(pwd)<min_length:
        new_char = random.choice(characters)
        pwd +=new_char

        if new_char in digits :
            has_number=True
        elif new_char in spl:
            has_spl=True

        meets_criteria=True
        if numbers:
            meets_criteria=has_number
        if spl_char:
            meets_criteria=meets_criteria and has_spl
    return pwd
min_length=int(input("enter the min length:"))
has_number=input("do you want to have numbers(y/n)? ").lower() == "y"
has_spl=input("do you want to have special characters(y/n)? ").lower()=="y"
pwd=gen_password(min_length,has_number,has_spl)
print("the generated password is :",pwd)
    