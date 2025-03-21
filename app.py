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
def avg(x):
    total = {}

    for row in x[1:]:
        name = row[0]
        sales = map(int, row[1:])
        total[name] = sum(sales)/30
    
    return total

allavg = avg(data)

print(allavg)