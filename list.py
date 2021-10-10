a = []
n = int(input())
a.append(n)
a.remove(n)
a.insert(0,5)
a.insert(1,10)
a.insert(0,6)
print(a)
a.remove(6)
a.append(9)
a.append(1)
a.sort()
print(a)
a.pop(3)
a.reverse()
print(a)

# đề yêu cầu
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# kết quả đề
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]