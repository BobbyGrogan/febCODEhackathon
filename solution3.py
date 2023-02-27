import csv

with open("csvs/Naperville.csv", 'r') as file:
	data = csv.reader(file)
	for n in data:
		blue = float(n[13])*2
		choc = float(n[14])*2.5
		bana = float(n[15])*3
		shouldbe = blue + choc + bana
		if float(n[12]) != shouldbe:
			peoplenow = [n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],n[10],n[11]]
			print(peoplenow)
