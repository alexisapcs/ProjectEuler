def sum_of_square(num):
    i = 1
    total = 0
    while i <= num:
        total += i*i
        i += 1
    return total

def square_of_sum(num):
    i = 1
    total = 0
    while i <= num:
        total += i
        i += 1
    return total*total

print(sum_of_square(100))
print(square_of_sum(100))
print(square_of_sum(100)-sum_of_square(100))
    
