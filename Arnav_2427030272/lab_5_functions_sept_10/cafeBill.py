"""
2. a cafe allows customer to order multiple items. WAF to calculate totalBill(*items)
   where each item is given as a tuple (name, price). This function should return
   the total bill
"""

def totalBill(*items):
    bill=0
    for i in range(len(items)):
        bill+=items[i][1]
    print("total bill :", bill)
totalBill(("bread", 20), ("brush", 10), ("apple", 40))
