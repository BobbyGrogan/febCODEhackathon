import datetime
import random
import numpy
import math

store_locations = ["Hinsdale", "Naperville", "Downers Grove", "Willowbrook", "Lombard"]
manager_names = [["Cole", "Jason"], ["Janelle", "Ana", "Jacob", "Charmaine"], ["Kimberly", "Andres", "Max"], ["Rishika", "Caroline"], ["Dan", "Xiaoqing"]]
employee_names = [["Shreya", "Taiyo", "Sabiha", "Robert", "Evelyn", "Enris", "Maurizio"], ["Alton", "Satchel", "Charlie", "Jenna", "Chrissa", "Lauren", "Hillary", "Svelko", "Paul", "Anna", "George", "Alex", "Layla", "Edward", "James", "Austin", "Jake", "Valerie"], ["Mallory", "Mark", "Arnav", "Shiven", "Camil", "Grace", "Elena", "Jett", "Thomas", "Arun", "Neeraj", "Aryan", "Prashant", "Anushka"], ["Viha", "Songting", "Carlos", "Emmanuel", "Jesus", "Igor", "Vladimir", "Luca"], ["Bernadette", "Mary Anne", "Stephen", "Jack", "Angeline", "Kristine", "Samantha", "Alexey"]]
# managers: 2, 4, 3, 2, 2 - managers get paid $30 an hour
# employees: 6, 18, 14, 8, 8 - employees get paid $18 an hour
# overtime is paid if an employee works more than 40 hours per week, i.e. they work 6 days
# blueberry: $2.00, chocolate: $2.50, banana: $3.00

def select_employees(options=employee_names):
	day = []
	all = []
	for n in options:
		loc = []
		z = 0
		chosen = len(n)/2 - 1
		if random.randint(0, 100) > 70:
			chosen += 1
		while z < chosen:
			x = random.randint(0, len(n)-1)
			if x not in loc:
				loc.append(x)
				z += 1
		day.append(loc)
	all.append(day)
	return day

def get_employee_names(numbers, store):
	names = []
	for n in numbers:
		name = employee_names[store][n]
		names.append(name)
	return names

def change_employees(current, store):
	new = current
	proper = len(new)
	inc = 0
	for n in new:
		if random.randint(0, 100) > 70:
			new.remove(n)
			while len(new) < proper:
				employees = get_employee_names(select_employees()[store], store)
				if employees[0] not in new:
					new.append(employees[0])
					break
		inc += 1
	return new

def select_manager(options=manager_names):
	day = []
	all = []
	for n in options:
		x = random.randint(0, len(n)-1)
		day.append(x)
	all.append(day)
	return day

def get_item_sales(store, employees=employee_names):
	weights = [1, 3.8, 2, 1.5, 1.8]
	for n in employees:
		blueberry = math.ceil(numpy.random.normal(loc=77*weights[store], scale=10))
		chocolate = math.ceil(numpy.random.normal(loc=55*weights[store], scale=10))
		banana = math.ceil(numpy.random.normal(loc=50*weights[store], scale=10)) + 10
	return blueberry, chocolate, banana

def next_item_sales(store, previous):
	all = []
	previousblue = math.floor(previous[0])
	blue = math.ceil(numpy.random.normal(loc=previousblue*0.99, scale=1))
	all.append(blue)

	previouschoc = math.floor(previous[1])
	choc = math.ceil(numpy.random.normal(loc=previouschoc*0.99, scale=0.5))
	all.append(choc)

	previousbana = math.floor(previous[2])
	bana = math.ceil(numpy.random.normal(loc=previousbana*1, scale=3))
	all.append(bana)

	return all

def get_total_sales(item_sales):
	total = 2*item_sales[0] + 2.5*item_sales[1] + 3*item_sales[2]
	return total

def quirks(employees):
	total_sales = 0
	blueberry_sales = 0
	chocolate_sales = 0
	banana_sales = 0
	if "Svelko" in employees:
		if random.randint(0,100) > 60:
			total_sales -= 20
	if "Taiyo" in employees:
		toadd = math.ceil(numpy.random.normal(loc=5, scale=2))
		if toadd > 0:
			blueberry_sales += toadd
	if "Maurizio" in employees:
		toadd = math.ceil(numpy.random.normal(loc=5, scale=2))
		if toadd > 0:
			chocolate_sales += toadd
	if "Bernadette" in employees:
		toadd = math.ceil(numpy.random.normal(loc=5, scale=1.5))
		if toadd > 0:
			banana_sales += toadd
	return total_sales, blueberry_sales, chocolate_sales, banana_sales

def combine(store, times):
	inc = 0
	date = datetime.datetime(2021, 3, 11)
	manager = manager_names[store][select_manager()[store]]
	employees = get_employee_names(select_employees()[store], store)
	item_sales = get_item_sales(store)
	while inc < times:
		if inc%7 == 0:
			date += datetime.timedelta(days=1)
		else:
			if random.randint(0, 100) > 70:
				manager = manager_names[store][select_manager()[store]]
			employees = change_employees(employees, store)
			item_sales = next_item_sales(store, item_sales)
			mods = quirks(employees)
			date += datetime.timedelta(days=1)
			final_date = date.strftime("%B %d, %Y")
			item_sales[0] += mods[1]
			if inc > 120:
				if random.randint(0,100) > 60:
					item_sales[0] -= 3
					item_sales[1] -= 4
			item_sales[1] += mods[2]
			item_sales[2] += mods[3]
			total_sales = get_total_sales(item_sales) + mods[0]
			to_print = [final_date, employees, manager, "$" + str(total_sales), item_sales]
			to_print = str(to_print).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "")
			print(to_print)
		inc += 1

combine(0, 365)
