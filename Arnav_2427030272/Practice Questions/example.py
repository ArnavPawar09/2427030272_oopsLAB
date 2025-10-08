subTotal = 0
for i in range(4):
    p = int(input("enter price : "))
    subTotal+=p
disc_subTotal = subTotal
if subTotal>1000:
    disc_subTotal*=0.9
gst = disc_subTotal*0.12
grandTotal = disc_subTotal + gst
print("sub total =", subTotal)
print("discounted sub total =", disc_subTotal)
print("tax amount =", gst)
print("grand total =", grandTotal)