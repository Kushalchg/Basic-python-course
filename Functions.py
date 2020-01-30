def summation():   #function defination
    a=2
    b=5
    print(a+b)


summation()     #function call


#function with parameter

def say_hello(name):            #FUNCTION DEFINARION
    print("hello "+name)


say_hello("kushal")         #FUNCTION CALL
say_hello("ayush")







#we can also use multipal parameter

def say_hello(name,age):            #FUNCTION DEFINARION
    print("hello "+name +" you are"+age)


say_hello("kushal","20")         #FUNCTION CALL
say_hello("ayush","33")



#we can also pass the integer value of other type of value


def say_hello(name,age):            #FUNCTION DEFINARION
    print("hello "+name +" you are "+str(age))


say_hello("kushal",20)         #FUNCTION CALL
say_hello("ayush",33)