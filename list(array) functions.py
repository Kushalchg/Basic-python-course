luckey_no=[3,2,6,75,4,3,2,45,6]
friends=["kushal","adesh","kashyap","kalyan","kushal","kushal"]

length=friends.__len__(); #use to find the length of array
print(length)

len=luckey_no.__len__()
print(len)


friends.sort()    #it accending the order
print(friends)


luckey_no.sort()  #it also keep array element in accending order
print(luckey_no)


friends1=friends.copy()  #It generally copy all the element of friends into friends1
print(friends1)


print(friends.count("kushal")) #It cound the specific word

friends.pop()   #It remove the last element of list(array)
print(friends)

friends.remove("adesh")     #it help to remove specific element of the array(list)
print(friends)

friends.clear()    #It clear entire array and give blank result
print(friends)