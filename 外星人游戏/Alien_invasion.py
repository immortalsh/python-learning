# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:56:53 2020

@author: Lenovo
"""


import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien invasion")
    ship = Ship(ai_settings, screen)
    # 创建一个子弹编组
    bullets = Group()
    aliens = Group()
    # 创建一行外星人
    gf.create_fleet(ai_settings, screen, aliens)
    while True:  # 开始主循环
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings,aliens)


run_game()
