#print format
name = "Fayjullah"
age = 25
print("My name is {0} and my age is {1}".format(name,age))
print("")
print("My python tutor is {0} and I learn from {1} and also learn from {other}".format("fayjullah","github",other="youtube"))
print("")
print("My python tutor is {0} ".format("fayjullah","github",other="youtube"))
print("My name is {name} and my age is {age}".format(name="Emon",age=25))
# print("My name is {name} and my age is {age}".format(name,age)) This throws error

#print functions hidden parameters

"""
The hidden parameters of print():
    1.vlues,...,
    1. sep 
    2. end
    we can print multiple or more values seperating by commas
    default value of sep is whitespace. sep = " "
    default value of end is \n(new line). end= '\n'
"""
print('Welcome','to','my','github',2025)
print('Welcome','to','my','github',2025,sep = "-")
print('Welcome','to','my','github',2025,sep = "-" ,end=' \'')
print('Welcome','to','my','github',2025,sep = "-" ,end=' \\')
print('Welcome','to','my','github',2025,sep = "-" ,end=' hehe')

