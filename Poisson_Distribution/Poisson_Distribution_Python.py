'''

lambda = rate at which the number of events occur

mean = lambda

variance = lambda

'''

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

rate = 2

n = np.arange(0,10)

y = stats.poisson.pmf(n ,rate)

print(y)

plt.figure(1)
plt.plot(n, y, '-o')
plt.title('Poisson : $\lambda$ = %i' % rate)
plt.xlabel("Number of accidents")
plt.ylabel("Probability of number of accidents")
# plt.show()

data = stats.poisson.rvs(mu = 2, loc = 0, size = 1000)
print("Mean : %g" % np.mean(data))
print("SD : %g" % np.std(data, ddof = 1))

plt.figure(2)
plt.hist(data, bins = 9, normed = True)
plt.xlim(0, 10)
plt.xlabel("Number of accidents")
plt.title("Simulating poisson Random variables")
plt.show()



