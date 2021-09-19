ans = 0
def collatz(num):
    collatzsequence = [num]
    n = num
    while (n != 1):
        if ((n%2)==0):
            n = n/2
        else:
            n = (3*n) + 1
        collatzsequence.append(n)
    return collatzsequence
for i in range(3,1000000):
    if (ans < len(collatz(i))):
        ans = len(collatz(i))
        print(f"{i}")
