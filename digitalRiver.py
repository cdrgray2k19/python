# river 1 = 1, 2, 4, 8, 16, 23, 28, 38, 49, 62

#1, 2, 4, 8, 7, 5, 10, 11, 13

# river 3 = 3, 6, 12, 15, 21, 24, 30, 33, 39, 51, 57, 69
# river 9 = 9, 18, 27, 36, 90, 99, 117, 126

#459 - 477 - 495 - 513

river1Sum = [1, 2, 4, 8, 7, 5, 10, 11, 13, 14, 16, 19, 17, 20, 22, 23, 29, 25, 26, 28, 32, 31]

'''def river(n):
    riv = [n]
    ss = [n]
    while True:
        val = riv[len(riv)-1]
        total = int(riv[len(riv)-1])
        s = 0
        for char in val:
            total += int(char)
            s += int(char)
        if total > 16384:
            break
        riv.append(str(total))
        if s not in ss:
            ss.append(s)
    return ss

print(river('1'))'''

n = input()
if int(n) % 9 == 0:
    print('river 9 found at' + n)
elif int(n) % 3 == 0:
    print('river 3 found at' + n)
else:
    val = n
    while True:
        total = 0
        for char in val:
            total += int(char)
        val = str(int(val) + total)
        