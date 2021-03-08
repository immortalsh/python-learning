# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:25:38 2020

@author: Lenovo
"""

with open('pi_digits.txt','a') as file_object:
    file_object.write("victory\n")

with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents)
    