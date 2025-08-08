name = input("Enter the name: ")
print("My name is {0}".format(name))

#let's make addition operation using users input

num1 = input("Enter the first number: ") #suppose num1= 4
print("")
num2 = input("Enter the second number: ") #suppose num2= 4
print("First number is {0} and Second number is {1}".format(num1,num2))

result = num1+num2 

print("The result is : {0}".format(result)) #the output will be 44. Because the input function will give string . We need to convert the string if possible.

print(type(num1))
print(type(num2))
print(type(result))

num1 = int(num1)
num2 = int(num2)
result = num1+num2
print(type(num1))
print(type(num2))
print(type(result))
print(result)