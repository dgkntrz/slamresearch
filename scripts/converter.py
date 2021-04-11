import csv
filename = input("Enter file to convert to csv: ")
out = input("Enter output file name: ")
fname = out + ".csv" 
with open(fname, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["#timestamp [ns]", "p_RS_R_x [m]", "p_RS_R_y [m]", "p_RS_R_z [m]", "q_RS_w []", "q_RS_x []", "q_RS_y []", "q_RS_z []"])
	file = open(filename,"r")
	lines = file.readlines()
	arr = []
	for line in lines:
		arr = line.split()
		if "\n" in line:
			writer.writerow(arr)
			print(arr)
			arr = []
