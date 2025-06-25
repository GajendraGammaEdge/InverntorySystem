from numpy import random
import matplotlib.pyplot as plt
import seaborn as sn 

sn.displot(random.normal(size=1000),kind='kde')
plt.show(block=True)


x = random.normal(size=(2,3))
print(x) 

y = random.normal(loc=1, scale=3, size=(3,4))
print(y)