
def DemSoLuongChuSo(n):
    if (n < 10):
        return 1
    else:
        return DemSoLuongChuSo(n / 10) + 1
n = int(input("hãy nhập vào đây : "))

print("có ",DemSoLuongChuSo(n)," số nguyên")