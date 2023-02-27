import csv

months = ["March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "January", "February", "March"]
blues = []
chocs = []
banas = []
sales = []
managerpay = 0
employeespay = 0
inc = 0

def statement(info):
	print(info[0] + " at Jason's bakery in Hinsdale")
	print("\n")
	print("Incomes ------ ")
	print("From blueberry muffin sales: $" + str(info[1]))
	print("From chocolate muffin sales: $" + str(info[2]))
	print("From banana muffin sales: $" + str(info[3]))
	print("Total sales: $" + str(info[4]))
	print("\n")
	print("Costs ------")
	print("Cost of general employees: $" + str(info[5]))
	print("Cost of management: $" + str(info[6]))
	print("Cost of rent: $" + str(info[7]))
	print("Total costs: $" + str(info[8]))
	print("\n")
	print("Profit: $" + str(info[9]))

with open("csvs/Hinsdale.csv", 'r') as file:
	data = csv.reader(file)
	for n in data:
		if int(n[0]) > 0:
			if months[inc] in n[1]:
				blues.append(int(n[7]))
				chocs.append(int(n[8]))
				banas.append(int(n[9]))
				sales.append(float(n[6]))
				managerpay += 36*8
				employeespay += 4*18*8
			else:
				totalblue = sum(blues)
				totalchoc = sum(chocs)
				totalbana = sum(banas)
				totalsales = sum(sales)
				month = months[inc]
				rent = 4000
				costs = employeespay+managerpay+rent
				profit = totalsales-costs

				info = [month, totalblue*2, totalchoc*2.5, totalbana*3, totalsales, employeespay, managerpay, rent, costs, profit]
				statement(info)
				print("break")

				sales = []
				blues = []
				chocs = []
				banas = []
				managerpay = 0
				employeespay = 0
				inc += 1
