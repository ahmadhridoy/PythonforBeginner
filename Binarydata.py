hrilist = [1, 2, 3,4,5]

a = bytes(hrilist)
print(type(a))
print(a)

hrilist = [2,6,5,4]

b = bytearray(hrilist)
print(type(b))
b[2]=120
print(b)
print(b[2])