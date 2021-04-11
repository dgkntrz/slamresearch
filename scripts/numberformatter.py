from decimal import Decimal

a = 1403636579763555584
diff = 0
filename = input("Enter file to fix numbers to nanoseconds: ")
out = input("Enter output file name: ")
fname = out + ".txt" 
strn = ""
with open(fname, 'w', newline='') as file:
	file = open(filename,"r")
	lines = file.readlines()
	arr = []
	first = 0
	for line in lines:
		arr = line.split()
		number = float(arr[0])
		while (number < 1000000000000000000):
			number = number * 10

		if first == 0:
			num = Decimal(number)
			if (num > a):	
				dif = num-a
				print(a)
				print(num)
				print(dif)
				first = 1
			else:
				dif = a-num
				print(a)
				print(num)
				print(dif)
				first = 2
		if first == 1:
			arr[0] = str(Decimal(number) - dif)
		else:
			arr[0] = str(Decimal(number) + dif)
		strn += arr[0] + " " + arr[1] + " " + arr[2] + " " + arr[3] + " " + arr[4] + " " + arr[5] + " " + arr[6] + " " + arr[7] + "\n"
		

file = open("out.txt", "w")
file.write(strn)
file.close()
