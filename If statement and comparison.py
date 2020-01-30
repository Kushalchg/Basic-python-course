def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print("num1 is greatest among three")
    elif(num2>=num1 and num2>=num3):
        print("number two is gratest among")
    else:
        print("number three is grater among")
max_num(22,33,333)


#instant of using elif else we can also three if statement for three condition



#alternative method

def find_max(num1,num2,num3):
    if(num1>=num2 and num1>=num3):
        return num1
    elif(num2>=num1 and num2>=num3):
        return num2
    else:
        return num3
print(find_max(33,43,333))