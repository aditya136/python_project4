import pygame
from pygame.locals import *

size = width, height = (1200, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)

pygame.init()
running = True

screen = pygame.display.set_mode((size))

pygame.display.set_caption("car game made by @aditya1366")
screen.fill((60, 220, 0))



pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height))

pygame.draw.rect(
    screen,
    (255, 240, 60),
    (width/2 - roadmark_w/2, 0, roadmark_w, height))


pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))


pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 + road_w/2 - roadmark_w*2, 0, roadmark_w, height))

pygame.display.update()

car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = width/2 + road_w/4, height*0.8

car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = width/2 - road_w/4, height*0.2

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()


pygame.quit()
