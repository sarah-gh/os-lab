arr=[0,1]
def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b
        arr.append(b)   # a will now be 1, and b will also be 1, (0 + 1)

n = int(input("Enter the num: "))

for index, fibonacci_number in zip(range(n), fib()):
    print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))

print('\n\nlist: ',arr)