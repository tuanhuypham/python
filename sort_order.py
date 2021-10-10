 '''Câu hỏi:
Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
Gợi ý: dùng list sort'''

''''mã giã 
chuỗi do người dùng nhập
phân tách bởi dấu phẩy
in ra chuỗi theo thứ tự bảng chữ cái
phân tách bởi dấu phẩy 
'''
#dùng input cho du lieu vao 
#dung split de phan tach nhung gi input dua vao boi dau phay
#in ra ket qua va dung tuple chuyen doi du lieu thanh dang chuoi 
#dung list sort de sap xep thu tu cac chu cai


incoming = input(" hãy nhập chuỗi vào: ")
incoming = incoming.split(",")
incoming.sort()

print("đã sắp xếp thứ tự : ",tuple(incoming))
