def divs(num):
    for x in range(1, 21):
        if num%x != 0:
            return False
    return True

i = 2500
while divs(i) != True:
    i += 20
print(i)
