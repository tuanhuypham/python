'''print('Danh sach tinh nang:')
print('1. Nhap Ten, Tuoi cua hoc sinh')
print('2. Hien thi danh sach da nhap')
print('3. Xem lai danh sach tinh nang')
print('4. Hien thi nhung hoc sinh tu 20 tuoi tro len') #[{'name': Tinh, 'age': 20}, {'name': Co, 'age': 5}, {'name': Huy, 'age': 20}] =>  tu 20 tuoi tro len: [Tinh, Huy]
print('5. Thoat chuong trinh')'''

studentlist = []
for x in range(10):
	print('nhap ten')
	inputname = input()
	print('nhap tuoi')
	inputage = input()
 
	student ={
	'name':inputname,
	'age':inputage
	}

	studentlist.append(student)
	print(studentlist)