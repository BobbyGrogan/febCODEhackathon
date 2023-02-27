import statistics as st
import csv

allbana = []
allchoc = []
allblue = []
allpeople = []

with open("csvs/Hinsdale.csv", 'r') as file:
	data = csv.reader(file)
	for n in data:
		if n[0] == '0':
			bana = int(n[9])
			choc = int(n[8])
			blue = int(n[7])
		elif n[0] != 0:
			peoplenow = [n[2],n[3],n[4],n[5]]
			allpeople.append(peoplenow)
			b = bana
			c = choc
			l = blue
			bana = int(n[9])
			choc = int(n[8])
			blue = int(n[7])
			allbana.append((b-bana)/b)
			allchoc.append((c-choc)/c)
			allblue.append((l-blue)/c)

flatpeople = [item for sublist in allpeople for item in sublist]
peopleset = set(flatpeople)
uniquepeople = (list(peopleset))

with open("csvs/Hinsdale.csv", 'r') as file:
	data = csv.reader(file)
	for person in uniquepeople:
		print(person)
		data = csv.reader(file)
		for n in data:
			peoplenow = [n[2],n[3],n[4],n[5]]
			if person in peoplenow:
				
