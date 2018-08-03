# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:14:55 2018

@author: n10027301
"""

import math
def quadratic(a,b,c):
    if a == 0:
        raise TypeError('a不能为0')
        
    if not isinstance(a,(int,float)) or  not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('Bad operand type')
        
    delta = math.pow(b,2) - 4*a*c
    
    if delta < 0:
        return '无实根'
    elif delta==0:
        x1= (math.sqrt(delta)-b)/(2*a)
        print('x=', x1)
        print('error='+a*x1*x1+b*x1+c)
    else:
        x1= (math.sqrt(delta)-b)/(2*a)
        x2=-(math.sqrt(delta)+b)/(2*a)
        print('x1=%.2f, x2=%.2f'%(x1, x2))
        print('error1=', a*x1*x1+b*x1+c)
        print('error2=', a*x2*x2+b*x2+c)



#77=10.69（13.375-t)t
a=10.69
b=13.375
c=77
quadratic(-a,a*b,-c)



