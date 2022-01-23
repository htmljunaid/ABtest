# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 21:19:25 2022

@author: Junaid
"""

from scipy import stats
from statsmodels.stats.power import TTestIndPower
from statistics import stdev
import statistics


Control = [4.95,3,8.59,4.6,8.37,6.57,6.71,4.66,5.46,3.22,3.48,4.8,7.76,6.3,5.88,6.62,4.34,4.17,4.01,5.5,8.32,5.53,5.59,3.78,3.35,4.38,4.25,7.62,5.43,7.29]
Test = [6.06,6.05,7.37,7.09,6.6,8.61,7.7,7.44,9.46,9.02,8.27,6.74,8.75,5.35,5.86,6.11,7.43,5.7,8.22,9.85,8.99,8.49,8.35,7.29,6.12,6.71,8.74,7.42,5.43,6.9]
Difference = [-1.11,-3.05,1.22,-2.49,1.77,-2.04,-0.99,-2.78,-4,-5.8,-4.79,-1.94,-0.99,0.95,0.019,0.51,-3.09,-1.53,-4.21,-4.35,-0.67,-2.96,-2.76,-3.51,-2.77,-2.33,-4.49,0.2,0,0.39]

a = statistics.mean(Control)
b = statistics.mean(Test)
c = statistics.mean(Difference)
z = statistics.pstdev(Difference)

t_value,p_value=stats.ttest_ind(Control,Test, alternative = "less")

print('Test statistic is %f'%float("{:.6f}".format(t_value)))

print('p-value for one tailed test is %f'%p_value)

alpha = 0.05

    
TTestIndPower.power(self = 0, effect_size = ((a-b)/z) , nobs1 = 30, alpha = alpha, ratio=1, df=29, alternative='smaller')
