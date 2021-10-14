# from itertools import product

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# print(*product(a,b))



class Pro():
    pass
from itertools import product

PDT = Pro()

PDT.a = list(map(int, input().split()))
PDT.b = list(map(int, input().split()))
PDT.C = print(*product(PDT.a,PDT.b))
