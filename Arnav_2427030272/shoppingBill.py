subTotal=0
for i in range(4):
    p=int(input("enter price : "))
    subTotal+=p
if subTotal>1000:
    disc_subTotal=subTotal*0.9
else: disc_subTotal=subTotal
gst=disc_subTotal*(1+0.12)
grandTotal = disc_subTotal+gst
print("sub total =", subTotal)
print("discounted sub total =", disc_subTotal)
print("tax amount =", gst)
print("grand total =", grandTotal)