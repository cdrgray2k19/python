#d->b visa versa
#h->d visa versa
#h->b visa versa

def DtoB(x):
    binary = ''
    count = 0

    while x > 0:
        y = x%2
        binary += str(y)
        x //= 2
        count += 1
        
        if count%4 == 0 and x > 0:
            binary += ' '

    if count %4 != 0:

        remainder = 4 - (count%4)

        for i in range(0, remainder):
            binary += '0'
    if len(binary) == 0:
        binary += '0000'
    
    return binary[::-1]

def BtoD(x):
    denary = 0
    count = 0
    x = str(x)
    x = x[::-1]
    for i in x:   
        if i == '1':
            i = int(i)
            denary += 2**count
        count += 1
    
    return denary

def DtoH(x):
    hex = ''
    while x > 0:
        y = x%16
        if y > 9:
            y = chr((y - 9 + 64))
        hex += str(y)
        x //= 16
    if len(hex) == 0:
        hex += '0'
    return hex[::-1]


def HtoD(x):
    x = str(x)
    x = x[::-1]
    denary = 0
    count = 0
    for i in x:
        try:
            i = int(i)
        except:
            i = ord(i) - 64 + 9
            i = int(i)
        denary += (16**count) * i
        count += 1

    return denary

def HtoB(x):
    x = str(x)
    binary = ''
    for i in x:
        try:
            i = int(i)
        except:
            i = ord(i) - 64 + 9
            i = int(i)
        
        binary += DtoB(i)
        binary += ' '

    return binary



def BtoH(x):
    count = 1
    hex = ''
    nibble = ''
    remainder = len(x)%4
    if remainder != 0:
        x = x[::-1]
        for i in range(0, remainder):
            x += '0'
        x = x[::-1]
    
    for i in x:
        nibble += i
        if count%4 == 0:
            denary = BtoD(nibble)
            digit = DtoH(denary)
            hex += digit
            nibble = ''
        
        count += 1

    return hex


name = input('hello welome to the data converison program!\nWhat is your name?\n')

print('Hello', name)


while True:

    print('what conversion would you like to do?\n1. Denary to Binary\n2. Binary to Denary\n3. Denary to Hex\n4. Hex to Denary\n5. Hex to binary\n6. Binary to Hex')
    choice = input('Your answer:\n')
    while True:
        try:
            if int(choice) > 0 and int(choice) < 7:
                break
            else:
                choice = input('Please choose a valid option\n')
        except:
            choice = input('Please choose a valid option\n')

    choice = int(choice)

    if choice == 1:
        num = input('Denary value:\n')
        while True:
            try:
                num = int(num)
                break
            except:
                num = input('Enter valid denary value:\n')
        
        print(DtoB(int(num)))

    elif choice == 2:
        num = input('Binary value(no spaces):\n')
        while True:
            Binary = True
            for i in num:
                try:
                    i = int(i)
                    if not (i > -1 and i < 2):
                        Binary = False
                except:
                    Binary = False

            if Binary == True:
                break
            else:
                num = input('Enter valid binary value(no spaces):\n')


        print(BtoD(num))

    elif choice == 3:
        num = input('Denary value:\n')
        while True:
            try:
                num = int(num)
                break
            except:
                num = input('Enter valid denary value:\n')
        print(DtoH(int(num)))

    elif choice == 4:
        num = input('Hex value:\n')
        
        while True:
            Hex = True
            for i in num:
                try:
                    i = int(i)
                    if not (i > -1 and i < 10):
                        Hex = False
                except:
                    i = ord(i)
                    if not(i > 64 and i < 71):
                        Hex = False

            if Hex == True:
                break
            else:
                num = input('Enter valid hex value:\n')

        print(HtoD(num))

    elif choice == 5:
        num = input('Hex value:\n')
        
        while True:
            Hex = True
            for i in num:
                try:
                    i = int(i)
                    if not (i > -1 and i < 10):
                        Hex = False
                except:
                    i = ord(i)
                    if not(i > 64 and i < 71):
                        Hex = False

            if Hex == True:
                break
            else:
                num = input('Enter valid hex value:\n')

        
        print(HtoB(num))
    
    elif choice == 6:
        num = input('Binary value(no spaces):\n')
        
        while True:
            Binary = True
            for i in num:
                try:
                    i = int(i)
                    if not (i > -1 and i < 2):
                        Binary = False
                except:
                    Binary = False

            if Binary == True:
                break
            else:
                num = input('Enter valid binary value(no spaces):\n')
        
        print(BtoH(num))

    else:
        print('error occured')

    again = input('would you like to use the program again?\n').lower()
    if again != 'yes':
        print('Goodbye', name)
        break
    else:
        print('Welcome back', name)