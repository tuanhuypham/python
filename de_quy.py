# bài 1: Viết 1 hàm tính fix(a,b,c) có công thức: (a + b*b - c)/2
# bài 2: Đệ quy: Nhập 1 số N, in từ 5 đến số 0 từng dòng 1
# bài 3: Đệ quy: Nhập 1 số N, tính tổng N + (N - 1) + (N - 2) + ... + 1



#bài 2: Đệ quy: Nhập 1 số N, in từ 5 đến số 0 từng dòng 
'''def demso(n):
	print(n)
	if(n > 1):
		demso(n-2)

demso(9)

#bài 1: Viết 1 hàm tính fix(a,b,c) có công thức: (a + b*b - c)/2

def fix(a,b,c):
	return  (a + b*b - c)/2


#print(fix(5,6,7))'''

#bài 3: Đệ quy: Nhập 1 số N, tính tổng N + (N - 1) + (N - 2) + ... + 1
def sum(n):
	if(n == 1):
		return 1
	return n + sum(n - 1)
n = int(input())
print(sum(5))



'''defnhanlen(n):
	if ( n == 0 ):
		return 2 * n+(n-1)
print(nhanlen(8))'''
