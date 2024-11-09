'''#If the number of parameters is unknown, add a * before the parameter name:
def myfunction(*kids):
    print("The youngest child is " + kids[2])
myfunction("Emil","Tobias","Linus")'''

'''#You can also send parameters with the key = value syntax.
#This way the order of the parameters does not matter.
def myfunction2(child3,child2,child1):
    print("The youngest child is " + child3)
myfunction2("Emil","Tobias","Linus")'''


'''#If the number of keyword parameters is unknown, add a double ** before the parameter name:
def myfunction3(**kid):
    print("His last name is " + kid["fname2"])
myfunction3(fname1="Tobias", lname1 = "Hamid",lname2="roro",fname2="ilyas" )'''


'''#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
def myfunction4(country = "Norway"):
    print("I am from "+country)
myfunction4("Sweden")
myfunction4("India")
myfunction4()
myfunction4("Brazil")'''



'''#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def myfunction5(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]
myfunction5(fruits)'''


'''#To let a function return a value, use the return statement:
def myfunction6(x):
    return 5*x
print(myfunction6(3))
print(myfunction6(5))
print(myfunction6(9))'''

'''#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction7():
    pass
myfunction7()
print("function passed")'''


'''#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#To specify that a function can have only positional arguments, add , / after the arguments:

def myfunction8_1(x,y):
    print(x)
    print(y)

x=2
y=1
myfunction8_1(y=x,x=y)'''



'''#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def myfunction8_2(x):
    print(x)
myfunction8_2(x=3)'''

'''















'''