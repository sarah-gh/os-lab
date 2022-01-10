import math

def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def pascals_triangle(rows):
    result = [] 
    for count in range(rows): 
        row = [] 
        for element in range(count + 1): 
            row.append(combination(count, element))
        result.append(row)
    return result

n=int(input("enter number: "))
for row in pascals_triangle(n):
    print(" ".join(str(x) for x in row))
