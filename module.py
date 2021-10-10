print("bat dau")
start = input()
print ("over")
end = input() 

start = int(start)
end = int(end) + 1

for number in range(start,end):
	if(number % 7 == 0 and number % 11 == 0):
		print(number)