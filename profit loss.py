actual__cost = float(input("Please enter the actual product price: "))
sale_amount = float(input("Please enter the sale price: "))

if (sale_amount > actual__cost):
    amount = sale_amount - actual__cost
    print("Total profit = ", amount)
else:
    print("No profit!")