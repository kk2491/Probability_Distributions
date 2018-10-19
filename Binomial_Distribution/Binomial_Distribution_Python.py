'''
Python implementation of Binomial Distribution

Reference : http://mathworld.wolfram.com/BinomialDistribution.html

Reference : https://stattrek.com/probability-distributions/binomial.aspx

Mean = np

Variance = np * (1 - p)

'''

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

n = 10
p = 0.3

k = np.arange(0,11)

binomial = stats.binom.pmf(k, n, p)

print("Probability Mass Function : ", binomial)

mean = n * p
variance = n * p * (1 - p)
std_dev = np.sqrt(variance)

print("Mean : ", mean)
print("Variance : ", variance)
print("Standard Deviation : ", std_dev)


# Plot

plt.figure(1)
plt.plot(k, binomial, '-o')
plt.title('Binomial : n = %i , p = %.2f' %(n,p), fontsize = 15)
plt.xlabel("Number of successes")
plt.ylabel("Probability of successes")
# plt.show()

plt.figure(2)
binom_sim = data = stats.binom.rvs(n = 10, p =0.3, size = 10000)
print("Mean : %g" % np.mean(binom_sim))
print("SD : %g " % np.std(binom_sim, ddof = 1))
plt.hist(binom_sim, bins = 10, normed = True)
plt.xlabel("x")
plt.ylabel("Density")
plt.show()



