# population-dispersion.py
"""Calculate the Variacne and Standard Deviation of the results of 10 six-sided die rolls."""

import statistics as stats

results = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

print(stats.pvariance(results))
print(stats.pstdev(results))