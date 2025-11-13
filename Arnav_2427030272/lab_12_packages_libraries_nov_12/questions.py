"""
1. import the required libraries numpy, pandas, matplotlib.
2. using numpy create arrays and perform mathematical operations.
3. using pandas create a dataframe and perform filtering and analysis.
4. using matplotlib plot graphs for visual representation of data.
"""

import numpy as n
import pandas as p
import matplotlib.pyplot as mp

arr = n.array([10, 20, 30, 40, 50])
print("array :",arr)
print("mean :", n.mean(arr))
print("squares :", n.square(arr))
print("standard deviation :", round(n.std(arr), 3))

print()

data = {'student':['a', 'b', 'c', 'd'], 
        'math':[85, 90, 78, 92], 
        'science':[88, 76, 95, 89]
    }
df = p.DataFrame(data)
print(df)
print("\nstudents with math > 80 :\n", df[df['math']>80])

print()

df.plot(x='student', y=['math', 'science'], kind='bar')
mp.title("marks comparison")
mp.xlabel("students")
mp.ylabel("marks")
mp.xticks(rotation=0)
mp.show()