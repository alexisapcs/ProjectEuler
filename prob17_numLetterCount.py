## If the numbers 1 to 5 are written out in words:
## one, two, three, four, five, then there are
## 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
## If all the numbers from 1 to 1000 (one thousand)
## inclusive were written out in words,
## how many letters would be used?

proper = [0, len("one"), len("two"), len("three"), len("four"), len("five"), len("six"), len("seven"), len("eight"), len("nine"), len("ten"), len("eleven"), len("twelve"), len("thirteen"), len("fourteen"), len("fifteen"), len("sixteen"), len("seventeen"), len("eighteen"), len("nineteen")]

tenth = [len("twenty"), len("thirty"), len("forty"), len("fifty"), len("sixty"), len("seventy"), len("eighty"),len("ninety")]

def below100(n):
    if (n < 20):
        return proper[n];
    
    return tenth[(int)(n / 10) - 2] + proper[n % 10]

def numberLength(n):
    
    if (n < 100):
        return below100(n)

    res = 0;
    h = (int)(n / 100) % 10;
    t = (int)(n / 1000);
    s = n % 100;

    if (n > 999):
        res+= below100(t) + len("thousand")
    if (h != 0):
        res+= proper[h] + len("hundred")
    if (s != 0):
        res+= len("and") + below100(s)
    return res;

sum = 0
for x in range(1, 1001):
    sum+=numberLength(x)

print(sum)
