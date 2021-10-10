#1 bài tính số phân bitnary

'''def bitnary(n):
	if (n<=1):
		return 2
	return 2 * bitnary( n - 1)

print(bitnary(-1))'''


# bài 2 in ra dãy fibonacci  vơi số n tối đa chi trướ  phải lớn hơn con số 0
'''def fibonacci(n):
    if n == 1 or n == 2: 
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) 
n = int(input("nhập vào N : "))
ab = " "
for x in range(0,n+1):
    ab+= str(fibonacci(x)) + " "
print(ab)'''




#Bài 3: Tính S = 1 + 2 + 3 + … + n
#Dễ dàng tìm được công thức tổng quát cho bài này là:

#S(0) = 0
#S(n) = S(n-1) + n

# '''def cong_don(n):
# 	if (n == 1):
# 		return 1
# 	return cong_don(n-1)+n 
# print(cong_don(-1))'''


# #bài 4 Tính x mũ n
# def somun(x,n):
#     if  x == 1 or x == 1:
#         return somun(x)'''
    
# # #bài 5 ước chung lớn nhất


# #3. Các bài tập mở rộng thêm (tất cả 5 bài):

def is_leap(year):
    if year <= 1900:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
year = int(input())
print(is_leap(year))