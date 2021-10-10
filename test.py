# bài 1 cộng hai số ngẫu nhiên từ 0 đến 100


# import random

# print("hãy tính nhẩm đừng dùng máy tính ",random.randint(1,100),"+",(random.randint(1, 100)))

#bài 2 ước chung lớn nhất của a và b


# def uscln(a, b):
#     if (b == 0):
#         return a;
#     return uscln(b, a % b);

# a = int(input("Nhập số nguyên dương a = "))
# b = int(input("Nhập số nguyên dương b = "))
# print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))

#bài 3 Tính x mũ n
# x0 = 1
# xn = x * xn-11


# bài 4 đếm số nguyên
# def DemSoLuongChuSo(n):
#     if (n < 10):
#         return 1
#     else:
#         return DemSoLuongChuSo(n / 10) + 
# n = int(input("hãy nhập vào đây : "))

# print("có ",DemSoLuongChuSo(n)," số nguyên"