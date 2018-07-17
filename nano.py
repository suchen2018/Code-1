# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 21:20:27 2018

@author: Chen
"""

import pandas as pd
import matplotlib.pyplot as plt

filename='data.xlsx'

#with open(filename, 'r') as f:
#    data=f.read()
#print(data[3])   
     
data = pd.read_excel(filename)
     
data.plot(x='Depth', y='Load')
plt.xlabel(r'Distance'+'$\ (\mu$'+'m)')
plt.ylabel(r'Load'+' (nN)')
plt.xlim(0,2500)
plt.ylim(0,250)

plt.show()