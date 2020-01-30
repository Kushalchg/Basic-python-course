is_male= False
is_tall=True

if is_male:
    if is_tall:
        print("you are tall male")
    else:
        print("you are a short male")

else:
    if is_tall:
        print("you are tall but not male")
    else:
        print("nither you are man nor you are tall")


        #  OR statement

is_male = False
is_tall = True
if is_tall or is_male:
    print("you are tall or a male or both")
else:
    print("nither tall nor male")



#AND STATEMENT

#if the value fo two variable is true  then it return if statement otherwise it return else statement

is_male = False
is_tall =False
if is_tall and is_male:
    print("you are tall  male or you are not both of them")
else:
    print("you are either not male of not tall or both")



# ELSEIF STATEMENT in python it is denoted bu ELIF


is_male = False
is_tall =Trues
if is_tall and is_male:
    print("you are tall  male or you are not both of them")

elif is_male and not (is_tall):
    print("you are short male")
elif not(is_male) and is_tall:
    print("you are a tall but not male")

else:
    print("you are either not male of not tall or both")




