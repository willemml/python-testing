y = [2] #this array will contain the prime numbers that are found

for i in range(3, 10000):
    isaprime = 1
    for u in range(0, len(y)):
        if (i % y[u]) == 0:
            isaprime = 0
            break
    if isaprime == 1:
        print(i)
        y.append(i)

print(y)
