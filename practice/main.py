from itertools import permutations

string = 'abc'
perms = list(permutations(string))

print(perms)

for i in range(len(perms)):
    perms[i] = ''.join(perms[i])

print(perms)
perms.sort()
print(perms)