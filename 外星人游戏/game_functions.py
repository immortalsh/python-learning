# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:02:31 2020

@author: Lenovo
"""

#game_functions.py
import sys
import pygame
from bullet import Bullet
from alien import Alien
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.quit()
       
        
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(ai_settings,screen,ship,bullets):
    """响应按键与鼠标"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event, ship)

def create_alien(ai_settings,alien_width):
    """计算每行容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x=int(available_space_x/(2 * alien_width))
    return number_aliens_x
def create_fleet(ai_settings,screen,aliens):
    """创建外星人群"""
    #创建第一个外星人
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x=int(available_space_x/(2 * alien_width))
    #创建第一行外星人
    for alien_number in range(number_aliens_x):
        alien=Alien(ai_settings,screen)
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        aliens.add(alien)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullet_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
def update_aliens(aliens):
    aliens.update()
