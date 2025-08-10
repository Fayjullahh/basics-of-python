x = 2 # 2 = 010
y = 3 # 3 = 011
print(x & y)

# 010
# 011
#-------
##010 =2

print(x | y)

# 010
# 011
#--------
##011 = 3

print(x >> 1)

# 010 >> 1 means --> 1 number of bit from msb is shifted to right and last bit will be removed . output 001 . It divide by 2
# 011 >> 1 means --> 1 number of bit from msb is shifted to right and last bit will be removed . output 001
print(y>>1)

print(x << 1)

#010 << 1 means --> 1 number of bit from lsb is shifted to left by 1 bit and last bit from msb will be removed. output 110 = 4. It multiply by 2

print(y<<1)

print(~x) # -(x+1) = -(2+1) = -3
print(~-4) # -(-4+1) = -(-3) = 3