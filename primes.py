y = [2] # this array will contain the prime numbers that are found
x = 100 # will check for primes up to this number
p = 1 # number of primes found

print("Looking for primes from 0 to " + str(x) + ".")
print("2 is a prime.")

for i in range(3, x):
    isaprime = 1
    for u in range(0, len(y)):
        if (i % y[u]) == 0:
            isaprime = 0
            break
    if isaprime == 1:
        print(str(i) + " is a prime.")
        y.append(i)
        p = p + 1

print("Found " + str(p) + " prime(s) from 0 to " + str(x) + ".")
