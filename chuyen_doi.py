
'''Câu hỏi:
Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một list và một tuple chứa mọi số.


Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''

'''values=input("Nhập vào các giá trị ngau nhien :")
A=values.split(",")
B=tuple(A)
print(A)
print(B)'''

values = input("nhập vào giá trị cần chuyển đổi :")
resul = values.split(",")

print("list :",resul)
print("tuple :",tuple(resul))