import pygame
import random
import time

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (  30, 130,   0)
ORANGE   = ( 235,  80,  25)

class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("1659690884711.png"), (50, 50))
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("1659693881172.png"), (70, 70))
        self.rect = self.image.get_rect()


    def update(self):
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("1659692702021.png"), (40, 40))
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.y -= 7

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Coding")

all_sprites_list = pygame.sprite.Group()

block_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()

for i in range(40):
    block = Block(ORANGE)

    block.rect.x = random.randrange(1200)
    block.rect.y = random.randint(50, 550)

    block_list.add(block)
    all_sprites_list.add(block)

player = Player()
all_sprites_list.add(player)

done = False

clock = pygame.time.Clock()

score = 0
player.rect.y = 650

font = pygame.font.SysFont("Broadway", 30)
font_end = pygame.font.SysFont("Broadway", 100)

text_end = font_end.render("GAME OVER!", True, (0, 0, 0))

while not done:


    text = font.render("Score: " + str(score), True, (0, 0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    all_sprites_list.update()

    for bullet in bullet_list:

        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)

        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    screen.fill(WHITE)

    all_sprites_list.draw(screen)

    screen.blit(text, (0, 0))

    if score == 40:
        screen.blit(text_end, (300,300))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()