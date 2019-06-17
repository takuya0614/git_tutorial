import numpy as np
import matplotlib.pyplot as plt

def my_func(x):
     return 2*(x**3)-9*(x**2)+12*x


xs = np.linspace(0,3)
plt.plot(xs,my_func(xs))




