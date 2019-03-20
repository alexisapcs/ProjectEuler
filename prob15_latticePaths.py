##Starting in the top left corner of a 2×2 grid, and
##only being able to move to the right and down,
##there are exactly 6 routes to the bottom right corner.
##
##How many such routes are there through a 20×20 grid?

top = 1
for x in range(21, 41):
    top *= x

bottom = 1
for i in range(1, 21):
    bottom *= i
    
print( (int)(top/bottom) )
