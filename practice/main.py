from collections import defaultdict

n = 10

D = defaultdict(int)

def f(n):
    print(n)
    if n <= 1:
        return 0
    if n not in D:
        D[n] = f(n // 2) + f((n + 1) // 2) + n
        print(D)

    return D[n]
    
print(f(n))