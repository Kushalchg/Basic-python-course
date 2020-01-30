# we use return statement in the function when we use print statement outside from the function
#it basically return the value of function which can be print outside from the function


def cube(num):
    num*num*num

print(cube(2))

#above code give the result none because we print the function outside the function and we don't use return ststement





#which give the actual value of function

def cube(num):

    return num*num*num

print(cube(2))



#another type we can use return type by using variable
def cube(num):
    return num*num*num


result=cube(5)
print(result)



#when we use return statement in the function it dosenot see the code below it.
#when function see return statement it break the function
#example

def cube(num):
    return num * num * num
    print("hello")




print(cube(2))