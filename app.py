## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list

### 1) Produce the Average sales data per dat for each store. Be sure to map a location to each store. 

### 2) Sort the stores by most profitable. 

### 3) Get The Average Sales Data of all stores

### 4) Which stores are in danger of being closed (performing 20% below average sales?)
file_path = "SalesData.csv"  
data = csv_to_list(file_path)
#print(data)  # Output the list
total = {}
def avg(x):

    for row in x[1:]:
        name = row[0]
        sales = list(map(int, row[1:]))
        #len counts number of values so u dont gotta say 30
        total[name] = sum(sales)/len(sales)
avg(data)
def sort_avg(x):
     #uses lambda and sorted to sort each value from least to greatest, reverse makes it greatest to least
    return dict(sorted(x.items(), key=lambda item: item[1], reverse = True))
#print(total)
#print(sort_avg(total))
#print(every_avg)
fat = sum(total.values())
many = len(total)
every_avg = fat/many
uh_oh = {}
for x, y in total.items():
    if y < every_avg*0.8:
        uh_oh[x] = y
print(f"these stores are in danger of closing: {uh_oh}")
