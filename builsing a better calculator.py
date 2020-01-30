

num1 = float((input("enter the first number")))
x = input("enter the operation")
num2 = float((input("enter the second number")))




#taking input from user


def calculator():

    if (x== '+'):
        print(num1+num2)
    elif(x == '-'):
        print(num1-num2)
    elif(x== '*'):
       print(num1*num2)
    elif(x=='/'):
        print(num1/num2)
    else:
        print("you entered invalid value")


calculator();
