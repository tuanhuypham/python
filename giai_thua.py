'''Câu hỏi:
Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
Gợi ý:
Trong trường hợp dữ liệu đầu vào được cung cấp, bạn hãy chọn cách để người dùng nhập số vào.'''

'''def my_factorial(n):

	if n == 1 :
		return 1
	else:
		return(n*my_factorial(n-1))
number=int(input("nhap gia thua can tim vao :"))
print("giai thua cua",number,"=",my_factorial(number))'''

y = int(input("nhập số cần giai thừa vào : "))
for a in range (1,y):
	y = y*a
print("kết quả giai thừa = ",y) 


