import numpy as np
import matplotlib.pyplot as plt

data = {'Xyz':50, 'X':10, 'Y':5, 'Z':2, }

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (2, 4))



plt.bar(courses, values, color ='red',
        width = 0.25)

plt.xlabel("x-label")
plt.ylabel("y-label")
plt.title("Simple diagram")
plt.show()
