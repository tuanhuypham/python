



a = int(input("nhập số a vào "))
b = int(input("nhập số b vào "))

def UCLN(a,b):
    if b == 0 :
        return a
    return UCLN(b,a % b)
print("Ước số chung lớn nhất của", a, "và", b, "là:",UCLN(a, b))

