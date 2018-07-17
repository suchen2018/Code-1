# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 18:15:18 2018

@author: Chen
"""

import random

class Man:
    flu=False
    test=False
    
all_people=[]

for i in range(10000):
    m=Man()
    
    if random.random()<0.01:
        m.flu=True
    
    if m.flu and random.random()<0.9:
         m.test=True
        
    if not m.flu and random.random()<0.09:
        m.test=True
        
    all_people.append(m)
    
positive_people=[m for m in all_people if m.test]
print(len(positive_people))

positive_flu=[m for m in positive_people if m.flu]
print(len(positive_flu))

print(len(positive_flu)/len(positive_people))
        