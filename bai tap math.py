for a in range(20):
	print('1.tinh dien tich hinh vuong ')
	print('2.tinh dien tich hinh chu nhat')
	print('chu vi hinh tron:c=2*r*pi')
	print('3. tinh va toc cua xe chay')
	print('4.tinh dien tich hinh tron')
	print('5.ket thuc thuc chuong trinh')

	print('chon chuc nang tu 1 den 4')
	feature = input()
	if(feature == '1'):
		print('S hinh vuong: S=a*a')
		print('nhap canh a vao')
		a = input()
		s = int(a) * int(a)
		print('dien tich hinh vuong '+ str(s))

	elif(feature == '2'):
		print('S chu nhat:a*b')
		print('nhap chieu dai vao')
		dai = input()
		print('nhap chieu rong vao')
		rong = input()
		s = int(dai) * int(rong)
		print('dien tich hinh chu nhat'+str(s))

	elif(feature == '3'):
		print('van toc xe chay:v=s/t')
		print('nhap quang duong')
		s = input()
		print('nhap thoi gian vao')
		t = input()
		c = int(s) / int(t)
		print('van toc xe chay la'+str(c))
	elif(feature == '5' ):
		print('cam on ban da su dung chuong trinh,chuc ban thanh cong')
		break