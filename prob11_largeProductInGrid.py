##In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
##changes grid into 2d array
a = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
b = "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
c = "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
d = "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
e = "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"

f = "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
g = "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
h = "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
i = "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
j = "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"

k = "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
l = "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
m = "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
n = "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
o = "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"

p = "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
q = "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
r = "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
s = "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
t = "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

def str_to_arr(theStr):
    ans = theStr.split(" ")
    return ans

array = []
array.append(str_to_arr(a))
array.append(str_to_arr(b))
array.append(str_to_arr(c))
array.append(str_to_arr(d))
array.append(str_to_arr(e))
array.append(str_to_arr(f))
array.append(str_to_arr(g))
array.append(str_to_arr(h))
array.append(str_to_arr(i))
array.append(str_to_arr(j))
array.append(str_to_arr(k))
array.append(str_to_arr(l))
array.append(str_to_arr(m))
array.append(str_to_arr(n))
array.append(str_to_arr(o))
array.append(str_to_arr(p))
array.append(str_to_arr(q))
array.append(str_to_arr(r))
array.append(str_to_arr(s))
array.append(str_to_arr(t))

##What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

def isValid(row, col):
    if row >= 0 and row < 20 and col >= 0 and col < 20:
        return True
    return False

def up(row, col):
    total = 1
    if isValid(row-3, col): total *= int(array[row-3][col])
    if isValid(row-2, col): total *= int(array[row-2][col])
    if isValid(row-1, col): total *= int(array[row-1][col])
    if isValid(row, col): total *= int(array[row][col])
    return total

def down(row, col):
    total = 1
    if isValid(row+3, col): total *= int(array[row+3][col])
    if isValid(row+2, col): total *= int(array[row+2][col])
    if isValid(row+1, col): total *= int(array[row+1][col])
    if isValid(row, col): total *= int(array[row][col])
    return total

def left(row, col):
    total = 1
    if isValid(row, col-3): total *= int(array[row][col-3])
    if isValid(row, col-2): total *= int(array[row][col-2])
    if isValid(row, col-1): total *= int(array[row][col-1])
    if isValid(row, col): total *= int(array[row][col])
    return total

def right(row, col):
    total = 1
    if isValid(row, col+3): total *= int(array[row][col+3])
    if isValid(row, col+2): total *= int(array[row][col+2])
    if isValid(row, col+1): total *= int(array[row][col+1])
    if isValid(row, col): total *= int(array[row][col])
    return total

def diagRight(row, col):
    total = 1
    if isValid(row, col): total *= int(array[row][col])
    if isValid(row+1, col+1): total *= int(array[row+1][col+1])
    if isValid(row+2, col+2): total *= int(array[row+2][col+2])
    if isValid(row+3, col+3): total *= int(array[row+3][col+3])
    return total

def diagLeft(row, col):
    total = 1
    if isValid(row, col): total *= int(array[row][col])
    if isValid(row+1, col-1): total *= int(array[row+1][col-1])
    if isValid(row+2, col-2): total *= int(array[row+2][col-2])
    if isValid(row+3, col-3): total *= int(array[row+3][col-3])
    return total

biggest = 0
for y in range(3, 20):
    for x in range(20):
        if up(y, x) > biggest:
            biggest = up(y, x)
            
for y in range(0, 17):
    for x in range(20):
        if down(y, x) > biggest:
            biggest = down(y, x)

for y in range(20):
    for x in range(3, 20):
        if left(y, x) > biggest:
            biggest = left(y, x)

for y in range(20):
    for x in range(0, 17):
        if right(y, x) > biggest:
            biggest = right(y, x)

for y in range(20):
    for x in range(20):
        if diagRight(y, x) > biggest:
            biggest = diagRight(y, x)

for y in range(20):
    for x in range(20):
        if diagLeft(y, x) > biggest:
            biggest = diagLeft(y, x)
print(biggest)
    
