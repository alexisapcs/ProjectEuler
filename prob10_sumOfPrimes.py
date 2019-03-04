#checks to see if number is prime
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        #print ('\t',f)
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

i = 1
total = 0
while i < 2000000:
    if is_prime(i):
        total += i
    i+=2
print(total+2)
