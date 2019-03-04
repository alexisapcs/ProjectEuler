def pythagorean_trip(a, b, c):
    if c > a and c > b:
        if (a*a) + (b*b) == (c*c):
            return True
    elif b > a and b > c:
        if (a*a) + (c*c) == (b*b):
            return True
    elif a > b and a > c:
        if (b*b) + (c*c) == (a*a):
            return True
    return False

for x in range(1, 998):
    for y in range(1, 998):
        for z in range(1, 998):
            if ( x + y + z ) == 1000:
                if pythagorean_trip(x, y, z):
                    print(x*y*z)
