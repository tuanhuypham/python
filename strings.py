student = [
    "tinh",  
    "huy",  
    "xuong",
    "co"  
]
print('nhap ten hoc sinh can tim')
wantedremove = input()
while wantedremove in student:
    if wantedremove in student:
        student.remove(wantedremove)
        print(student)
    else:
        print('Khong co hoc sinh trong danh sach')
