'''

mean = alpha / (alpha + beta)

variance = (alpha * beta) / ((alpha + beta)^2 * (alpha + beta + 1))

'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a = 0.5
b = 0.5
x = np.arange(0.01, 1, 0.01)
y = stats.beta.pdf(x, a, b)
plt.plot(x, y)
plt.title('Beta: a=%.1f, b=%.1f' % (a,b))
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.show()


