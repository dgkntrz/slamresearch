import csv
strn = ""
with open(input("Enter file name: ")) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			number = int(row[0][0:16])
			number = number/1000000
			strn += row[0] +" " + str(number) +"\n"
			line_count += 1
	
print(str)
file = open("out.txt", "w")
file.write(strn)
file.close()
