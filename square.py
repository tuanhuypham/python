a = int(input("nhập cạnh vào :"))
s = input("Nhập công thức vào S hoặc P : ")

if s == "S":
    S = a*a
    print("hình vuông có cạnh =",a,"có diện tích =",S)
if s == "P":
    P = a*4
    print("chu vi hình vuông là :",P)
elif s != "P" and s != "S":
    print("công thức sai")