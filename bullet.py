import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对发射的子弹进行管理"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船的位置创建子弹对象"""
        super().__init__()
        self.screen = screen

        # 先创建后定位
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存子弹位置，小数表示
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """向上移动子弹"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)