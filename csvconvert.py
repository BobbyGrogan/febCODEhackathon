import pandas as pd    

# open the file
file = open('data/hinsdale.txt','r')
# read the file, reads the file line by line into a list
raw = file.readlines()

def format_line(line):
	conv = line.split(",")
	conv[0] = conv[0] + ", " + conv[1]
	del conv[1]
	inc = 1
	while inc < len(conv)-1:
		conv[inc] = conv[inc][1:]
		inc += 1
	print(conv)
	conv[-1] = int(conv[-1])
	conv[-2] = int(conv[-2])
	conv[-3] = int(conv[-3])
	conv[-4] = float(conv[-4].replace("$", ""))
	return conv

id = 0
reformatted = []
for n in raw:
	converted_line = format_line(n)
	converted_line.insert(0, id)
	id += 1
	reformatted.append(converted_line)

#header = ["id", "date", "employee1", "employee2", "employee3", "employee4", "employee5", "employee6", "employee7", "manager", "total_sales", "blueberry_sales", "chocolate_sales", "banana_sales"]
#reformatted.insert(0, header)

df = pd.DataFrame(reformatted)
df.to_csv('csvs/Hinsdale.csv', index=False)

# "Hinsdale", "Naperville", "Downers Grove", "Willowbrook", "Lombard"
