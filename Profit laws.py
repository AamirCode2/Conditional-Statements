AC = float(input(" Please enter actual product price: "))
SA = float(input(" Please enter sale amount: "))

if (SA > AC):
 amount = SA - AC
    print("Total profit, {0}". format(amount))

else:
    print("NO profit!!!")