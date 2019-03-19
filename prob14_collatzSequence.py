## The following iterative sequence is defined for the set of positive integers:
##
## n → n/2 (n is even)
## n → 3n + 1 (n is odd)
##
## Using the rule above and starting with 13, we generate the following sequence:
##
## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
## It can be seen that this sequence (starting at 13 and finishing at 1)
## contains 10 terms. Although it has not been proved yet (Collatz Problem),
## it is thought that all starting numbers finish at 1.
##
## Which starting number, under one million, produces the longest chain?

def collatz(num):
    if num%2 == 0:
        return (int)(num/2)
    else:
        return (int)(3*num + 1)

topChain = 0
topChainIndex = 0
def collatz_count(num, count=0):
    if num == 1:
        return count+1
    else:
        return collatz_count(collatz(num), count+1)

for x in range(1, 1000000):
    guess = collatz_count(x, 0)
    if ( guess > topChain ):
        topChain = guess
        topChainIndex = x


print("the index of the highest chain is: ",  topChainIndex)


