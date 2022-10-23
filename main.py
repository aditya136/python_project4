import pygame
from pygame.locals import *
import random

size = width, height = (1200, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4

speed = 1

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
car_loc.center = right_lane, height*0.8

car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0

while running:
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # randomly select lane
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
# if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:



for event in pygame.event.get():
    if event.type == QUIT:
        running = False

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()


pygame.quit()