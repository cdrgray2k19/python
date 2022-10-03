x = int(input('integer:\n'))
binary = ''
while x > 0:
    y = x%2
    binary += str(y)
    x //= 2
print(binary[::-1])