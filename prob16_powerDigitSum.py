## 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##
## What is the sum of the digits of the number 2^1000?


def twoHund():
    product = 1
    for x in range(1, 101):
        product*=2
    return product

ans = 1;
for x in range(1, 11):
    ans*=twoHund()

num = str(ans)
sumo = 0
for i in range(0, len(num)):
    sumo += int(num[i])
print(sumo)
