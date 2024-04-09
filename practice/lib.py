from itertools import permutations
from collections import Counter
import string
from itertools import permutations
from collections import defaultdict

arr = [1, 2, 3, 1, 1, 2, 7,2]
arr.append(55)
arr.pop()
print(arr)

arr2 = ['a', 'b', 'c']
strings = 'abc'
N = 10

a = permutations(strings)
print(list(a))

b = Counter(arr)
print(b)
print(max(b, key=b.get))
ans = defaultdict(int)
print(ans[5]+1)
print(ans)

print(list(reversed(arr)))

alphabet = string.ascii_lowercase
print(alphabet)

ans = {}
ans["w"] = ""
ans["w"] += "a"
ans["b"] = "b"
print(ans)

print(chr(97)) ## chr(97) = 'a'
print(chr(65)) ## chr(65) = 'A'
print(ord("a")) ## ord('a') = 97
print(ord("A")) ## ord('A') = 65

all_permutations = list(permutations(arr2))
print(all_permutations)



q = [0 for _ in range(N)]
print(q)

pairs = [(1, 10), (1, 5), (1, 1)]
pairs = sorted(pairs)  # タプルの最初の要素でソートされる
print(pairs)

pairs = [(-3, 2), (-1, 4), (-5, 1)]
pairs.sort(key=lambda x: (x[1], x[0]))  # タプルの2番目の要素でソートし、同じ場合は1番目の要素でソート
print(pairs)  

a = [tuple([0, i+1]) for i in range(3)]
for i in range(3):
    a[i] = (a[i][0] + 1, a[i][1])

print(a)


for i in range(0,10,2):
    print(i)

abcd = 'acbd'
aaa = list(sorted(abcd))
print(aaa)

tmp = [[0]] * 5
tmp[0] = 1
print(tmp)

aa = {1: 2, 3: 4}
print(aa.get(3))

text = "Python"
formatted_text = text.center(10, '*')
print(formatted_text)
