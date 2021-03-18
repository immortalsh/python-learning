
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:50:10 2020

@author: Lenovo
"""

#alien.py
alien_0={ 'x_position': 0, 'y_position': 25,'speed':'medium'}
print("Original x_postion: "+str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定移动多远
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print("New position: "+str(alien_0['x_position']))
del(alien_0['x_position'])
print(alien_0)

