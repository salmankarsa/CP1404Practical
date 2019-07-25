sales = float(input("Enter Sales = $"))
while sales > 0:
    if sales < 1000:
        print(sales-sales*0.1)
        sales = float(input("Enter Sales = $"))
    elif sales > 1000:
        print(sales-sales*0.15)
        sales = float(input("Enter Sales = $"))
else:
    print("Invalid Value")
    sales = float(input("Enter Sales = $"))


