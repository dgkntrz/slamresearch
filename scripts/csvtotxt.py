import csv
str = ""
with open(input("Enter file name: ")) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {", ".join(row)}')
			line_count += 1
		else:
			str += row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[4] + " " + row[5] + " " + row[6] + " " + row[7] + "\n"
			line_count += 1
	
print(str)
file = open("out.txt", "w")
file.write(str)
file.close()
