#SIMPLE CALCULATOR
print("Choose a operation to perform :")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

#CHOOSE THE OPERATION TO PERFORM 

operation=input("enter operation:")

#GET TWO INPUT VALUES FROM THE USER 
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

#THIS FUCNTION WILL ADD TWO NUMBERS AND PRINT THE OUTPUT 
def add(num1,num2):
    print("the sum is :"+str(int(num1)+int(num2)))

#THIS FUNCTION WILL SUBTRACT TWO NUMBERS AND PRINT THE OUTPUT 
def sub(num1,num2):
    print("the difference is :"+str(int(num1)-int(num2)))

#THIS FUNCTION WILL MULTIPLY TWO NUMBERS AND PRINT THE OUTPUT 
def mul(num1,num2):
    print("the multiplication is :"+str(int(num1)*int(num2)))

#THIS FUCNTION WILL DIVIDE TWO NUMBERS AND PRINT THE OUTPUT 
def div(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError as e:#checking for divide by zero exception
        print(e)
        return 0

#OPERATION
if operation=="1":
    add(num1,num2)
elif operation=="2":
   sub(num1,num2)
elif operation =="3":
    mul(num1,num2)
elif operation =="4":
    print(div(num1,num2)) 
else:
    print("invalid input")

