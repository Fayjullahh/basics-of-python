#Built-in funtion: 1.print(),2.input(),3.type(),4.int(),foat(),string(),tuple(),list()etc. 5.abs(),6.pow(),7.min(),max(),8.round(),9.divmod(),10.bin(),oct(),hex(),11.id(),12.ord(),13.len(),14.sum()

#1
print("Hello world") #already we know many things about print()
#2
# a = input("Enter the number: ") #already we know many things about input 
#3
x = 5
print(type(x))
print(type(3.44))
print(type(1+7j))
print(type("Hello"))
print(type([1,2,3,4]))
print(type((1,2,3,4)))
#4
print(int(3.22))
print(float(3))
print(list("Hello"))
print(tuple("Hello"))
print(set("Helloo"))
#5
print(abs(-5))
#6
print(pow(2,3))
print(pow(2,-3))
#7
print(min(3,4))
print(max(3,4))
#8
print(round(3.44))
print(round(3.4445,2))
#9
print(divmod(4,2)) #(integer division,mod)
print(divmod(5,3))
#10
print(bin(4))
print(hex(14))
print(oct(14))
#11
a = 5
print(id(a)) # return memory address of the a variable
#12
print(ord("D")) #return the ascii value of a character
#13
print(len([1,2,3,5]))
#14
print(sum([1,2,3,4]))
