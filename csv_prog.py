
import csv

sales = {}

with open("sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        product = row[0]
        quantity = int(row[1])
        price = int(row[2])

        amount = quantity * price

        if product in sales:
            sales[product] += amount
        else:
            sales[product] = amount

print("Total Sales by Product:")

for product, total in sales.items():
    print(product + ":", total)
