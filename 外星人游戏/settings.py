# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:45:00 2020

@author: Lenovo
"""

# settings.py
class Settings:
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        # 子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1为向右移，-1为向左移
        self.fleet_direction = 1
