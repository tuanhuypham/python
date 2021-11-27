a = int(input("nhập cạnh a vào : "))
b = int(input("nhập cạnh b vào : "))
c = int(input("nhập cạnh c vào : "))

if b - c < a < b + c and a < b + c:
    print("tam giác")
else:
    print("không phải tam giác")