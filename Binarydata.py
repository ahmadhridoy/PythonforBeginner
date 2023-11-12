# hrilist = [1, 2, 3,4,5]
#
# a = bytes(hrilist)
# print(type(a))
# print(a)
#
# hrilist = [2,6,5,4]
#
# b = bytearray(hrilist)
# print(type(b))
# b[2]=120
# print(b)
# print(b[2])
'''
str = input()
count = 0
min_val = 10e9

di = {}

for i in range(len(str)) :
    if str[i] == 'C' :
        count -= 1
    elif str[i] == 'G' :
        count += 1

    di.update({i+1: count})
    min_val = min(min_val , count)

ans = []

for key, val in di.items() :
    if min_val == val :
        ans.append(key)

print(*ans)
'''

'''str1 = input()
str2 = input()

count = 0
for i in range(len(str1)) :
    if str1[i] != str2[i] :
        count += 1

print(count)'''

pat = input()
str = input()
d = int(input())
count = 0
lst = []
for i in range(len(str) - len(pat) + 1) :
    sub_str = str[i:i+len(pat)]
    count = 0
    for j in range(len(pat)) :
        if sub_str[j] != pat[j] :
            count += 1
    if count <= d :
     lst.append(i)


print(*lst)