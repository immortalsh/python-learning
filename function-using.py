# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:48:18 2020

@author: Lenovo
"""

#function-use
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    f_name=input("First name: ")
    l_name=input("Last name: ")
    if f_name or l_name: 
        formatted_name=get_formatted_name(f_name, l_name)
        print("\nHello "+formatted_name+"!")
    else :
        break
    