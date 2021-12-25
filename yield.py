def topten():
    n = 1
    while n < 10:
        value = n * n
        yield value
        n += 1

values = topten()

for i in values:
    print(i)