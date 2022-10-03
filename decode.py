'''
str = 'JU#XMOZ([OLXVbh0`d3^jik8Z:nejskaukrrd'
nums = []
for c in str:
    nums.append(ord(c))


def decode(order, str, i, y):
    if order == 0:
        print(str)
    else:
        str[i] += y
        for x in range(0,26):
            decode(order-1, str, i + 1, x)


for i in range(0,26):
    decode(3, nums, 0, 1)

str2 = ''

for i in nums:
    str2 += chr(i)

print(str2)'''