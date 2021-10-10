a = str(input())
if a == "":
	print(0)
else:
	c = []
	c.append(a)
	c = list(dict.fromkeys(a))
	d = len(c)
	print(d)

first_name = input()
last_name = input()
print("hello",first_name, last_name,"!","You just delved into python.")

