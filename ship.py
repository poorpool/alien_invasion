import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        """初始化飞船与位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像和外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在center中存小树
        self.center = float(self.rect.centerx)

        # 移动标志
        self.move_right = False
        self.move_left = False

    def update(self):
        # 根据移动标志调整飞船位置
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx