# bài 1 cộng hai số ngẫu nhiên từ 0 đến 100



# import random

# print("hãy tính nhẩm đừng dùng máy tính ",random.randint(1,100),"+",(random.randint(1, 100)))

# bài 2 ước chung lớn nhất của a và b



# a = int(input("nhập số a vào "))
# b = int(input("nhập số b vào "))

# def UCLN(a,b):
#     if b == 0 :
#         return a
#     return UCLN(b,a % b)
# print("Ước số chung lớn nhất của", a , "và", b, "là:",UCLN(a, b))


# bài 3 Tính x^n

# def somu(n):
#     if x == 0 or n == 0:
#         return 1
#     else:
#         return x *somu(n-1)
# a = int(input("nhập số cần tính lũy thừa : "))
# b = int((input("nhập mũ  cần lũy thừa : ")))

# print(" kết quả "," = ",somu())




# # bài 4 

# def DemSoLuongChuSo(n):
#     if (n < 10):
#         return 1
#     else:
#         return DemSoLuongChuSo(n / 10) + 1
# n = int(input("hãy nhập vào đây : "))

# print("có ",DemSoLuongChuSo(n)," số nguyên")

# bài 5 tính căn S(n)

# import math
# def S(n):
#     if n == 1 :
#         return 1
#     else:
#         return math.sqrt(n + S(n-1))
# n = int(input("nhập vào n để tính căn : "))
# print(S(n))





# def x(a,b):
#     print(a,b)
#     if(b==1):
#         return a
#     return x(a,b-1)*a
# print(x(5,5))