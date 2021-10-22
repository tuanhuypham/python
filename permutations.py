from itertools import permutations 

s,n = input().split(' ')


p = (permutations(sorted(s),int(n)))

for j in p:
    print(''.join(j))
