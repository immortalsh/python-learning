# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:15:23 2020

@author: Lenovo
"""

#alien.py
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        #每个外星人最初都在屏幕左上角附近
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #存储外星人的准确位置
        self.x=float(self.rect.x)
        
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        """向右移动外星人"""
        self.x+=self.ai_settings.alien_speed_factor
        self.rect.x=self.x
        