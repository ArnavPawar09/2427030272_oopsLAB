"""
4. WAF which calculates area : 
   if both L and W are provided, return rectangle area
   if only L is provided, return square area
"""

def area(length, width=1):
    if width==1:
        width=length
        area=length*width
        print("area of square =", area)
    else:
        area=length*width
        print("area of rectangle =", area)
    return
area(5, 10)