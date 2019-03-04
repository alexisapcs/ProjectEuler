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

#finds smallest prime number divisible from number
def smolPrime(num):
    for x in range(1, num): 
        if is_prime(x) and num%x == 0:
            return x
    return num

#recursion: if num is divisible by x then redo(num/x)
def nextPrime(num):
    if is_prime(num):
        return num
    else:
        print(num/smolPrime(num))
        return nextPrime(int(num/smolPrime(num)))
    
print(is_prime(600851475143))
print(smolPrime(600851475143))
nextPrime(600851475143)
