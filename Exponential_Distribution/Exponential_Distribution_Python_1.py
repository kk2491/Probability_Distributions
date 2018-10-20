'''

mean = 1 / lambda

variance = 1 /(lambda)^2

'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 

lambd =0.5 
x = np.arange(0, 15, 0.1)
y = lambd * np.exp(-lambd * x)

plt.figure(1)
plt.plot(x, y)
plt.title('Exponential: $\lambda$ = %.2f ' % lambd)
plt.xlabel('x')
plt.ylabel('Probability Density')
# plt.show()


data = stats.expon.rvs(scale = 2, size = 1000)
print("Mean : %g " % np.mean(data))
print ("SD : %g" % np.std(data, ddof = 1))

plt.figure(2)
plt.hist(data, bins = 20, normed = True)
plt.xlim(0, 15)
plt.title("Simulating Exponential Random Variables")
plt.show()

