"""
3. in an E-Commerce system, applyDiscount(price, discount) is frequently used. 
   management asked to reduce repetetive function definitions (use lambda).
"""

pr = 100
disc = 23
applyDiscount = lambda price, discount: price*(1-discount/100)
print(applyDiscount(pr, disc))