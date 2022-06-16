import pygame
import random
pygame.init()
win = pygame.display.set_mode((600, 600))
red = pygame.image.load('red_block.png')
red = pygame.transform.scale(red, (50, 50))
blue = pygame.image.load('blue_block.png')
blue = pygame.transform.scale(blue, (50, 50))
green = pygame.image.load('red_block.png')
green = pygame.transform.scale(green, (50, 50))
purple = pygame.image.load('purple_block.png')
purple = pygame.transform.scale(purple, (50, 50))
pink = pygame.image.load('pink_block.png')
pink = pygame.transform.scale(pink, (50, 50))
ball = pygame.image.load('ball.png')
ball = pygame.transform.scale(ball, (40, 40))
bar = pygame.image.load('bar.png')
bar = pygame.transform.scale(bar, (200, 40))
black = pygame.image.load('black.jpg')
black = pygame.transform.scale(black, (50, 50))
pygame.display.set_caption("block_breaker")
choices = [red, blue, green, purple, pink]


def choicer(choices):
    lst = []
    for x in range(0, 6):
        lst.append([])
        for y in range(0, 12):
            block = random.choice(choices)
            lst[-1].append(block)
    return lst


blocks = choicer(choices)
temp_x = 0
temp_y = 0
for p in range(0, len(blocks)):
    for q in range(0, len(blocks[0])):
        blocks[p][q] = [blocks[p][q], temp_x, temp_y]
        temp_x += 50
    temp_x = 0
    temp_y += 50

x = 200
y = 500
b_x = 280
b_y = 470
width = 40
height = 40
vel = 2
run = True
flip = False
ball_speed = 1
angle = 1
left_lean = False
right_lean = False
sub_flip = False
left_check = False
right_check = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if x <= 0:
        x = 0
    if x >= 400:
        x = 400
    if b_x <= 0:
        b_x = 0
        right_lean = True
    if b_x > 560:
        b_x = 560
        left_lean = True
    if b_y <= 0:
        b_y = 0
        flip = False
        left_lean = False
        right_lean = False
        left_check = False
        right_check = False
    if b_y > 570:
        quit()
    win.fill((0, 0, 0))
    win.blit(bar, (x, y))
    if left_lean:
        b_x -= 1.3
        right_lean = False
    if right_lean:
        b_x += 1.3
        left_lean = False
    cenbar_x = x+100
    cenball_x = b_x+15

    dist = ((cenball_x-cenbar_x)**2 + (b_y-y)**2)**(1/2)
    dist = dist-30
    if (b_y > y-33 and b_y < y) and (b_x+20 >= x and b_x-20 < x+200):
        flip = True
        left_lean = False
        right_lean = False
        angle = dist
    if flip:
        b_y -= ball_speed
        sub_flip = True
    else:
        b_y += ball_speed
    if sub_flip and (left_check == False) and (right_check == False):
        if cenbar_x > b_x:
            left_check = True
        if cenbar_x < b_x:
            right_check = True
    if left_check:
        b_x -= (angle/500)*10
    if right_check:
        b_x += (angle/500)*10
        sub_flip = False
    win.blit(ball, (b_x, b_y))
    max_blen = len(blocks)
    for p in blocks:
        for q in p:
            y_point = q[2]
            x_point = q[1]
            if (b_y <= y_point+40):
                if (b_x+30 > x_point-10 and b_x < x_point+50):
                    q[0] = black
                    q[1] = -50                     # somewhere in void
                    q[2] = -50
                    flip = False
                    left_lean = False
                    right_lean = False
                    left_check = False
                    right_check = False
                    break

    for p in blocks:
        for q in p:
            temp = q[0]
            win.blit(temp, (q[1], q[2]))
    pygame.display.update()
pygame.quit()
