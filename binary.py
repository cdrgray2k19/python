x = input('integer:\n')

while True:
    try:
        x = int(x)
        break
    except:
        x = input('integer please:\n')

binary = ''
count = 0

while x > 0:
    y = x%2
    binary += str(y)
    x //= 2
    count += 1
    
    if count % 4 == 0 and x > 0:
        binary += ' '

if count % 4 != 0:

    remainder = 4 - (count % 4)

    for i in range(0, remainder):
        binary += '0'

print(binary[::-1])