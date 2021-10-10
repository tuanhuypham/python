
def somu(n):
    if x == 0 or n == 0:
        return 1
    else:
        return x *somu(n-1)
x = int(input("nhập số cần tính lũy thừa : "))
n = int((input("nhập mũ  cần lũy thừa : ")))

print(" kết quả "," = ",somu(n))