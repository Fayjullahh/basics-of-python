#range function

x = range(1,10) # 10 is not included
print(x)
l = list(x)
print(l)
l2 = list(range(14)) #if we give only one parameter, it take it as ending number which is not included
print(l2)

l3 = list(range(1,14,2)) # third parameter is for gaps.
print(l3)

#sequence
l4 = [1,2,3,4,5,"Hello"]
print(l4) #output shows the sequentialy values from the list l4

#for loop works only range function and sequential values

for i in range(1,11,2):
    print(i)

for item in l4:
    print(item)

for characters in "Bangladesh":
    print(characters)

