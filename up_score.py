
arr = list(map(int, input().split()))
arr = list(dict.fromkeys(arr))
arr.remove(max(arr))
print(max(arr))