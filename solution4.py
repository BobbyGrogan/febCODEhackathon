import matplotlib.pyplot as plt
import csv

dates = []
sales = []
allblue =[]
allbana =[]
allchoc = []

with open("csvs/Hinsdale.csv", 'r') as file:
	data = csv.reader(file)
	for n in data:
		if int(n[0]) > 0:
			date = int(n[0])
			sale = float(n[6])
			dates.append(date)
			sales.append(sale)
	plt.plot(dates, sales)
	plt.title("Sales over time")
	plt.ylabel("Sales in Dollars")
	plt.xlabel("Days")
	plt.ylim(0, 2000)
	plt.show()


with open("csvs/Hinsdale.csv", 'r') as file:
	data = csv.reader(file)
	for n in data:
		if int(n[0]) > 0:
			blue = int(n[7])
			choc = int(n[8])
			bana = int(n[9])
			allblue.append(blue)
			allchoc.append(choc)
			allbana.append(bana)
	fig, ax = plt.subplots()
	ax.plot(dates, allblue)
	ax.plot(dates, allchoc)
	ax.plot(dates, allbana)
	plt.ylim(0, 340)
	plt.show()
