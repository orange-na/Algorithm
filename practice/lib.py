# from itertools import permutations
# from collections import Counter
# import string

# arr = [1, 2, 3, 1, 1, 2]
# strings = 'abc'
# N = 10

# a = permutations(strings)
# print(list(a))

# b = Counter(arr)
# print(b)

# print(list(reversed(arr)))

# alphabet = string.ascii_lowercase
# print(alphabet)

# ans = {}
# ans["w"] = ""
# ans["w"] += "a"
# ans["b"] = "b"
# print(ans)

# print(chr(97)) ## chr(97) = 'a'
# print(ord("a")) ## ord('a') = 97


# q = [0 for _ in range(N)]
# print(q)


N = 4
A = [12, 34, 56, 78]
X = 1000

sum_A = sum(A)
B = X//sum_A
C = X%sum_A

tmp = 0
for i in range(N):
  tmp += A[i]
  if tmp >= C:
    B = B*N + (i+1)
    print(B)
    exit()
