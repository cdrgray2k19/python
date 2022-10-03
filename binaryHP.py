from math import log
x = int(input("integer:\n"))
values = []
binary = ''

while x > 0:
    index = (log(x, 2)//1)
    values.append(index)
    x -= 2**index

count = 0

for i in range(0, int(values[0]) + 1):
    if i in values:
        binary += '1'
    else:
        binary += '0'
    count += 1
    if count%4 == 0 and i != int(values[0]):
        binary += ' '

if count %4 != 0:

    remainder = 4 - (count%4)

    for i in range(0, remainder):
        binary += '0'

print(binary[::-1])