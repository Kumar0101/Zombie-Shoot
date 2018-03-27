import pygame
import random
pygame.init()

width = 800
height = 380

#colors
white = (255,255,255)
red =(255,0,0)

screen = pygame.display.set_mode((width,height))

#images
bg_img = pygame.image.load("images/bg.png")
aim_pointer = pygame.image.load("images/aim_pointer.png")
zombie_1 = pygame.image.load("images/z1.gif")
zombie_2 = pygame.image.load("images/z2.gif")
zombie_3 = pygame.image.load("images/z3.png")
zombie_4 = pygame.image.load("images/z4.gif")

bullet = pygame.image.load("images/bullet.png")
gunImage = pygame.image.load("images/gun1.png")


#music
shotSound = pygame.mixer.Sound("sounds/gunshot.wav")

bgMusic = pygame.mixer.Sound("sounds/background.wav")
bgMusic.play()


def score(counter):
    font = pygame.font.SysFont(None,40)
    text = font.render("Score"+str(counter),True,red)
    screen.blit(text,(10,10))

def Game():
    #zpmbieList
    ZombieList = [zombie_1,zombie_2,zombie_3,zombie_4]
    zombieImage = random.choice(ZombieList)
    # zombie position
    zombie_X = random.randint(0, width - 250)
    zombie_Y = random.randint(0, height - 240)
    counter = 0
    # shot =4
    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                # shot -= 1
                # if shot >=0:
                 shotSound.play()
                 if rect_1.colliderect(rect_2):
                    print("Collision works")
                    zombieImage = random.choice(ZombieList)
                    zombie_X = random.randint(0, width - 250)
                    zombie_Y = random.randint(0, height - 240)
                    counter += 1

                    # if event.type ==pygame.KEYDOWN:
                    #     if event.key ==  pygame.K_r:
                    #         shot =4

        posX, posY = pygame.mouse.get_pos()

        # screen Blit
        screen.blit(bg_img, (0, 0))
        screen.blit(zombieImage, (zombie_X, zombie_Y))
        screen.blit(aim_pointer, (posX - 50, posY - 50))
        screen.blit(gunImage, (posX,height-100))
        screen.blit(bullet, (height, width))
        # for collision
        rect_1 = pygame.Rect(posX - 50, posY - 50, aim_pointer.get_width(), aim_pointer.get_height())
        rect_2 = pygame.Rect(zombie_X, zombie_Y, zombieImage.get_width(), zombieImage.get_height())
        score(counter)

        pygame.display.update()
Game()

