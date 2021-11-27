class SinhVien():
     def __init__(sv,ma,ten):
        sv.mssv = ma;
        sv.name = ten;
     def Inthongtin(sv):
        print("ma sinh vien : ",sv.mssv)
        print("ten sinh vien : ",sv.name)

SinhViena = SinhVien(1002002,"Tuấn Huy")
SinhViena.Inthongtin()
