price = []
item = int(input("Input number of items: "))
for i in range(item):
    price2 = int(input("Price of Item: $"))
    price.append(price2)
sumPrice = sum(price)
if sumPrice >= 100:
    print("total price: $", sumPrice-sumPrice*0.10)
else:
    print("total price: $", sumPrice)