import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():
    # 初始游戏，创建屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 创建子弹编组
    bullets = Group()

    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    play_button = Button(ai_settings, screen, "Play")

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button)

run_game()