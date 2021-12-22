import pygame
import sys
import random

pygame.init()
blok = 30 
MARGIN = 1
size = [590,720]
okn = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
orange = (250,150,0)
timer = pygame.time.Clock() 
con = pygame.font.SysFont('con', 45)
t = 3
class snake:
    def __init__(self,x,y):
        self.x = x
        self.y = y    
    def g(self):
        return 0 <= self.x <= 17 and 0 <= self.y <= 17

def apple_random():
    x = random.randint(0, 17)
    y = random.randint(0, 17)
    ww = snake(x,y)
    while ww in snake_blok:
        ww.x = random.randint(0, 17)
        ww.x = random.randint(0, 17)
    return (ww)
snake_blok = [snake(6,6),snake(7,6),snake(8,6)]
row = 1
col = 0
col1,row1 = 0,0
apple = apple_random()
speed, total = 0, 3
def f(collor,i,j):
    pygame.draw.rect(okn,collor,[15 + blok*j + MARGIN*(j+1),140+30*i +  MARGIN*(i+1),blok,blok])
k = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and col != 0:
                row = -1
                col = 0
            elif event.key == pygame.K_DOWN and col != 0:
                row = 1 
                col = 0
            elif event.key == pygame.K_LEFT and row != 0:
                row = 0
                col = -1
            elif event.key == pygame.K_RIGHT and row != 0:
                row = 0
                col = 1
    okn.fill(orange)
    pygame.draw.rect(okn,(200,150,0),[0,120,590,700-90])
    text = con.render(f"Размер: {total}",0,(10,10,10))
    okn.blit(text,(20,20))
    for i in range(18):
        for j in range(18):
            if (j+i) % 2 == 0:
                collor = (250,250,50)
            else:
                collor = (250,220,50)
            f(collor,i,j)
    head = snake_blok[-1]
    if not head.g():
        snake_blok = [snake(6,6),snake(7,6),snake(8,6)]
        total = 3
        k = 0
    if k == 1:
        snake_blok = [snake(6,6),snake(7,6),snake(8,6)]
        total = 3
        k = 0
    f((255,0,0),apple.x,apple.y)
    for l in snake_blok:
        f((20,200,0),l.x,l.y)
    pygame.display.flip()
    head = snake_blok[-1]
    if apple.x == head.x and apple.y == head.y:
        total += 1
        speed = total//8 + 1
        snake_blok.append(apple)
        apple = apple_random()
    new_head = snake(head.x + row,head.y+col)
    for z in snake_blok:
        if new_head.x == z.x and new_head.y == z.y:
            k = 1
    snake_blok.append(new_head)
    snake_blok.pop(0)
    timer.tick(3 + speed)

