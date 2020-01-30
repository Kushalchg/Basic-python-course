monthconversion={ "jan":"janary",
"feb":"feburary",
"mar":"march",
"apr":"april",
"may":" fifth month",
"jun":"june",
"jul":"july",
"aug":"augest",
"sep":"september is my birthday month",
"oct":"octover",
"nov":"november",
"dec":"december"


}
print(monthconversion["sep"])


#another way to call dictionary

print(monthconversion.get("dec"))

#when we pass a value wich doesnot exist in key then it return none value

print(monthconversion.get("xyz"))

#we can also asign value when there doesnot exist key value

print(monthconversion.get("ww","your key doesnot exist"))