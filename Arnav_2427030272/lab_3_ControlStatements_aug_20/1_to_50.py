"""
print nos 1-50
if div by 3 -> print figg
if div by 5 -> print buzz
if div by 3 and 5 -> figgbuzz
"""

for i in range(1, 51, 1):
    if i%3==0 and i%5==0:
        print(i,"- figgbuzz")
    elif i%3==0:
        print(i,"- figg")
    elif i%5==0:
        print(i,"- buzz")
    else: pass