from numpy import random
import matplotlib.pyplot as plt
import seaborn as sn

sn.displot(random.normal(size=1000),kind='kde')
plt.show(block=True)