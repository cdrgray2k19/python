users = ["charlie", "luke", "arran", "eduardo", "ollie", "hughie"]

print(users)

numItems = len(users)

numItems = 6

while numItems > 1:

    for i in range(0,len(users)-1):
        if users[i] > users[i+1]:
            temp = users[i]
            users[i] = users[i+1]
            users[i+1] = temp

    numItems -= 1

print(users)