import pygame
import random
import time
from record import record

#image_path = "/data/data/org.test.myapp/files/app/"
x_cocos = random.randint(0, 1900)
x_cocos1 = random.randint(0, 1900)
x_cocos2 = random.randint(0, 1900)
x_cocos4 = random.randint(0, 1900)
y_cocos, y_cocos1 = 0, 0
y_cocos2, y_cocos4 = 0, 0
x_crab = 1100
y_crab = 800
x_start = 1000
y_start = 500
clock = pygame.time.Clock()
time_to_execute = 5

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((2200, 1100))
pygame.display.set_caption("Попади в меня кокос")

font = pygame.font.Font(None, 60)
icon = pygame.image.load("images/crab.png")
bg_icon = pygame.image.load("images/bg.jpg")
bg = pygame.transform.scale(bg_icon, (2200, 1100))
crab_icon = [pygame.image.load("images/crableft/crableft1.png"), pygame.image.load("images/crableft/crableft2.png"), pygame.image.load("images/crableft/crableft3.png"), pygame.image.load("images/crableft/crableft4.png")]
cocos_icon = pygame.image.load("images/i.png")
cocos = pygame.transform.scale(cocos_icon, (180, 180))
bg_gameover_icon = pygame.image.load("images/bg_gameover.png")
bg_gameover = pygame.transform.scale(bg_gameover_icon, (2200, 1100))
start_button_image = pygame.image.load("images/start.png")
start_button = pygame.transform.scale(start_button_image, (200, 100))
restart_icon = pygame.image.load("images/restart.jpg")
restart = pygame.transform.scale(restart_icon, (200, 100))
bg_sound = pygame.mixer.Sound("sounds/bg.mp3")
pygame.display.set_icon(icon)

bg_sound.play(-1)

class InvisibleButton(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def check_click(self, pos):
        return self.rect.collidepoint(pos)
    

invisible_button = InvisibleButton(0, 0, 1100, 1100)
invisible_button1 = InvisibleButton(1100, 0, 1100, 1100)
frame = 0
running = True
button_pressed = False
start = False
gameover = False
menu = True
start_rect = None
restart_rect = None
start_time = None

while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_pressed = True
            pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(pos) and menu:
                menu = False
                start = True
                start_time = time.time()

            if gameover and restart_rect.collidepoint(pos):
                gameover = False
                start = True
                start_time = time.time()   

        if event.type == pygame.MOUSEBUTTONUP:
            button_pressed = False
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    if menu:
        screen.blit(start_button, (x_start, y_start))
        start_rect = pygame.Rect(x_start, y_start, start_button.get_width(), start_button.get_height())

    if start:
        print(x_crab)
        crab = pygame.transform.scale(crab_icon[frame], (300, 300))
        elapsed_time = time.time() - start_time
        text = font.render("Time: {:.2f}".format(elapsed_time), True, (0, 0, 0))
        text_record = font.render("Record: {:.2f}".format(record), True, (0, 0, 0))
        screen.blit(text_record, (1800, 10))
        screen.blit(text, (10, 10))
        screen.blit(crab, (x_crab, y_crab))
        crab_rect = pygame.Rect(x_crab, y_crab, crab.get_width(), crab.get_height())
        cocos_rect = pygame.Rect(x_cocos, y_cocos, cocos.get_width(), cocos.get_height())
        cocos_rect1 = pygame.Rect(x_cocos1, y_cocos1, cocos.get_width(), cocos.get_height())
        cocos_rect2 = pygame.Rect(x_cocos2, y_cocos2, cocos.get_width(), cocos.get_height())
        cocos_rect4 = pygame.Rect(x_cocos4, y_cocos4, cocos.get_width(), cocos.get_height())   

        if elapsed_time > 40:
            y_cocos += 40
            y_cocos1 += 40
            y_cocos2 += 40
            y_cocos4 += 40
            screen.blit(cocos, (x_cocos1, y_cocos1))
            screen.blit(cocos, (x_cocos2, y_cocos2))
            screen.blit(cocos, (x_cocos, y_cocos)) 
            screen.blit(cocos, (x_cocos4, y_cocos4)) 
        elif elapsed_time > 20:
            y_cocos += 40
            y_cocos1 += 40
            y_cocos2 += 40
            screen.blit(cocos, (x_cocos1, y_cocos1))
            screen.blit(cocos, (x_cocos2, y_cocos2))
            screen.blit(cocos, (x_cocos, y_cocos))  
        elif elapsed_time > 10:
            y_cocos += 35
            y_cocos1 += 35
            screen.blit(cocos, (x_cocos1, y_cocos1))
            screen.blit(cocos, (x_cocos, y_cocos))  
        elif elapsed_time > 5:
            screen.blit(cocos, (x_cocos1, y_cocos1))
            screen.blit(cocos, (x_cocos, y_cocos))  
            y_cocos1 += 30
            y_cocos += 30
        else:
            y_cocos += 25
            screen.blit(cocos, (x_cocos, y_cocos))   

        if x_crab > 1900:
            x_crab -= 30
        if x_crab < 0:
            x_crab += 30
        if y_cocos > 1000:
            y_cocos = 0
            x_cocos = random.randint(0, 2200)
        if y_cocos1 > 1000:
            y_cocos1 = 0
            x_cocos1 = random.randint(0, 2200)
        if y_cocos2 > 1000:
            y_cocos2 = 0
            x_cocos2 = random.randint(0, 2200)

        if crab_rect.colliderect(cocos_rect) or crab_rect.colliderect(cocos_rect1) or crab_rect.colliderect(cocos_rect2) or crab_rect.colliderect(cocos_rect4):
            
            start = False
            gameover = True
            if elapsed_time > record:
                with open("record.py", "w") as file:
                    file.write("record =" + str(elapsed_time))
                record = elapsed_time

        if button_pressed:
            pos = pygame.mouse.get_pos()
            if invisible_button.check_click(pos):
                x_crab -= 30
                frame = (frame + 1) % len(crab_icon)
            if invisible_button1.check_click(pos):
                x_crab += 30
                frame = (frame + 1) % len(crab_icon)
    if gameover:
        x_crab, y_crab = 1100, 800
        y_cocos, y_cocos1 = 0, 0
        y_cocos2, y_cocos4 = 0, 0
        x_cocos = random.randint(0, 1900)
        x_cocos1 = random.randint(0, 1900)
        x_cocos3 = random.randint(0, 1900)
        x_cocos4 = random.randint(0, 1900)
        screen.blit(bg_gameover, (0, 0))
        screen.blit(restart, (1000, 800))
        restart_rect = pygame.Rect(1000, 800, restart.get_width(), restart.get_height())
    pygame.display.update()
    clock.tick(20)