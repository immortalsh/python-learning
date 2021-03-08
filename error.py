# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:15:02 2020

@author: Lenovo
"""

import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as obj_1:
    json.dump(numbers,obj_1)