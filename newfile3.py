r = 5
#r=rows

a = 0

for i in range(r, 0, -1):

    a += 1

    for j in range(1, i + 1):

        print(a, end=" ")

    print("\r")
    r = 5
#r=rows and c=column

for r in range(1, r+1):

    for c in range(1, r + 1):

        print(c, end=" ")

    print("")
    r = 5
#r=rows

for i in range(r, 0, -1):

    num = i

    for j in range(0, i):

        print(num, end=" ")

    print("\r")
    r = 5

num = r

for i in range(r, 0, -1):

    for j in range(0, i):

        print(num, end=" ")

    print("\r")
    
    r = 6

for r in range(1, r):

    for column in range(r, 0, -1):

        print(column, end=" ")

    print("")
    
    rows = 5

for i in range(rows, 0, -1):

    for j in range(0, i + 1):

        print(j, end=’ ‘)

    print(“\r”)
    
    currentNumber = 1

stop = 2

rows = 5 # Rows you want in your pattern

for i in range(rows):

    for column in range(1, stop):

        print(currentNumber, end=" ")

        currentNumber += 1

    print("")

    stop += 2
    start = 1

stop = 2

currentNumber = stop

for row in range(2, 6):

    for col in range(start, stop):

        currentNumber -= 1

        print(currentNumber, end=" ")

    print("")

    start = stop

    stop += row

    currentNumber = stop
    