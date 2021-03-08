# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 00:07:16 2020

@author: Lenovo
"""

#bullet.py
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen=screen
        
        #在(0,0)处创建一个子弹矩形
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        
        #存储用小数表示的子弹位置
        self.y=float(self.rect.y)
        
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
    def update(self):
        """向上移动子弹"""
        self.y-=self.speed_factor
        #更新位置
        self.rect.y=self.y
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)