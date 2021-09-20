import pygame
import time
import Find_enemies

import enemies
from enemies import*
import random
import Maze

# generation of maze with dfs algorithm
Maze.first_generation()
Maze.dfs()
Maze.final_generation()
maze = Maze.maz
maze_with_coins = Maze.maz_with_coins
xs = 525
ys = 600

pygame.init()
window = pygame.display.set_mode((xs, ys))
pygame.display.set_caption("Pacman")

# maze
width = 24
height = 24
n = 21
m = 21
xm = 10
ym = 17

mazem = [
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #1
    [0,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1,0], #2
    [0,1,2,1,1,2,1,1,1,2,1,2,1,1,1,2,1,1,2,1,0], #3
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #4
    [0,1,2,1,1,2,1,2,1,1,1,1,1,2,1,2,1,1,2,1,0], #5
    [0,1,2,2,2,2,1,2,2,2,1,2,2,2,1,2,2,2,2,1,0], #6
    [0,1,1,1,1,2,1,1,1,2,1,2,1,1,1,2,1,1,1,1,0], #7
    [0,0,0,0,1,2,1,2,2,2,2,2,2,2,1,2,1,0,0,0,0], #8
    [1,1,1,1,1,2,1,2,1,0,0,0,1,2,1,2,1,1,1,1,1], #9
    [0,0,0,0,0,2,2,2,1,0,0,0,1,2,2,2,0,0,0,0,0], #10
    [1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1], #11
    [0,0,0,0,1,2,1,2,2,2,2,2,2,2,1,2,1,0,0,0,0], #12
    [0,1,1,1,1,2,1,2,1,1,1,1,1,2,1,2,1,1,1,1,0], #13
    [0,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1,0], #14
    [0,1,2,1,1,2,1,1,1,2,1,2,1,1,1,0,1,1,2,1,0], #15
    [0,1,2,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,2,1,0], #16
    [0,1,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1,1,0], #17
    [0,1,2,2,2,2,1,2,2,2,1,2,2,2,1,2,2,2,2,1,0], #18
    [0,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,2,1,0], #19
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0],#20
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]  #21
    ]

# pacman char
x = xm + 2 * width + 12
y = ym + 9 * width + 12
radius = 10
speed = 24
coordinate = [2, 9]
distance = 23
lives = 3

# points
rmin = 3
rmax = 5
coins = 0
points = 176


def draw_text(words, pos, size, colour, font_name, centered=False):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(words, False, colour)
    text_size = text.get_size()
    if centered:
        pos[0] = pos[0] - text_size[0] // 2
        pos[1] = pos[1] - text_size[1] // 2
    window.blit(text, pos)


def start():
    draw_text('PUSH SPACE TO START', [
        160, 570], 15, (0, 128, 128), 'arial black')


def game_over():
    draw_text('GAME OVER', [210, 540], 15, (128, 0, 128), 'arial black')


def winner():
    draw_text('YOU WIN!', [215, 540], 15, (128, 0, 128), 'arial black')


def score():
    draw_text('SCORE: ' + str(coins), [10, 570], 15, (255, 255, 255), 'arial black')


def draw_maze():
    # draw maze
    for i in range(n):
        for j in range(m):
            pygame.draw.line(window, (107, 107, 107), (xm + j * width, ym + i * width),
                             (xm + j * width, ym + n * width))
            pygame.draw.line(window, (107, 107, 107), (xm + j * width, ym + i * width),
                             (xm + m * width, ym + i * width))
            if maze[i][j] < 0:
                pygame.draw.rect(window, (192, 192, 192), (xm + j * width, ym + i * width, width, width))
            if maze[i][j] == 1:
                pygame.draw.rect(window, (50, 100, 232), (xm + j * width, ym + i * width, width, width))
            elif maze_with_coins[i][j] != 1:
                pygame.draw.circle(window, (255, 255, 255), (xm + j * width + 12, ym + i * width + 12), rmin)




def can_move(j, i, dirr):
    if maze[(y + i + height // 2) // height - 1][(x + j + width // 2) // width - 1] != 1:
        #print([(y + i + height // 2) // height - 1],[(x + j + width // 2) // width - 1])
        #print("maze =", maze[(y + i + height // 2) // height - 1][(x + j + width // 2) // width - 1])
        return True
    else:
        #print([(y + i + height // 2) // height - 1], [(x + j + width // 2) // width - 1])
        #print("maze =", maze[(y + i + height // 2) // height - 1][(x + j + width // 2) // width - 1])
        return False

path = 0
enemy = 2
def press_keys():
    global direction, path, enemy
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = 1
    if keys[pygame.K_s]:
        direction = 2
    if keys[pygame.K_a]:
        direction = 3
    if keys[pygame.K_d]:
        direction = 4
    if keys[pygame.K_1]:
        path = 1
        find_path(en0)
    if keys[pygame.K_2]:
        path = 2
        find_path(en0)
    if keys[pygame.K_3]:
        path = 3
    if keys[pygame.K_LEFT]:
        enemy = (enemy + 1) % 4 + 1
        print(enemy)


def find_path(en):
    global maze
    ene = maze[(en.coordinate[1]+ height // 2) // height - 1][(en.coordinate[0]+ height // 2) // height - 1]
    if path == 1:
        maze = Find_enemies.dfs_find(maze, maze[(y + height // 2) // height - 1][(x + height // 2) // height - 1], ene)
    if path == 2:
        maze = Find_enemies.dfs_find(maze, maze[(y + height // 2) // height - 1][(x + height // 2) // height - 1], ene)


def moving():
    global y, x, direction
    if direction == 1 and can_move(0, -speed, direction):
        y -= speed
    elif direction == 2 and can_move(0, speed, direction):
        y += speed
    elif direction == 3 and can_move(-speed, 0, direction):
        if x - speed > 22:
            x -= speed
        else:
            x = 502
    elif direction == 4 and can_move(speed, 0, direction):
        if x + speed < 502:
            x += speed
        else:
            x = 22
    eating()


    #coordinate[0] = (x + width // 2) // width
    #coordinate[1] = (y + height // 2) // height
    #print(coordinate)


en0 = Enemy(0, xm, ym, width)
en1 = Enemy(1, xm, ym, width)
en2 = Enemy(2, xm, ym, width)
def draw_enemy():
    pygame.draw.circle(window, en0.pic, (en0.coordinate[0], en0.coordinate[1]), radius - 3)
    pygame.draw.circle(window, en1.pic, (en1.coordinate[0], en1.coordinate[1]), radius - 3)
    pygame.draw.circle(window, en2.pic, (en2.coordinate[0], en2.coordinate[1]), radius - 3)


def can_enemy_move(cy, cx, j, i):
    if maze[(cy + i + height // 2) // height - 1][(cx + j + width // 2) // width - 1] != 1:
        #print([(y + i + height // 2) // height - 1],[(x + j + width // 2) // width - 1])
        #print("maze =", maze[(cy + i + height // 2) // height - 1][(cx + j + width // 2) // width - 1])
        return True
    else:
        #print([(y + i + height // 2) // height - 1], [(x + j + width // 2) // width - 1])
        #print("maze =", maze[(cy + i + height // 2) // height - 1][(cx + j + width // 2) // width - 1])
        return False


def enemy_moving(en, choice):
    direct = list()
    flag = 0
    if can_enemy_move(en.coordinate[1], en.coordinate[0], 0, -speed):  # up
        direct.append(0)
        if 0 == choice:
            flag = 1
    if can_enemy_move(en.coordinate[1], en.coordinate[0], 0, speed):   # down
        direct.append(1)
        if 1 == choice:
            flag = 1
    if can_enemy_move(en.coordinate[1], en.coordinate[0], -speed, 0):  # left
        direct.append(2)
        if 2 == choice:
            flag = 1
    if can_enemy_move(en.coordinate[1], en.coordinate[0], speed, 0):   # right
        direct.append(3)
        if 3 == choice:
            flag = 1
    if flag != 1:
        choice = random.choice(direct)
    if choice == 0:
        en.coordinate[1] -= speed
    elif choice == 1:
        en.coordinate[1] += speed
    elif choice == 2:
        en.coordinate[0] -= speed
    elif choice == 3:
        en.coordinate[0] += speed
    return choice


def updating():
    global direction, count, f
    window.fill((0, 0, 0))
    end_game()
    draw_maze()
    score()
    if start_event:
        start()
    pygame.draw.circle(window, (255, 255, 0), (x, y), radius)  # pacman
    draw_enemy()
    for i in range(lives):
        window.blit(life, (400 + i * 30, 570))
    pygame.display.update()
    if f:
        time.sleep(2)
        #pygame.mixer.music.unpause()
        f = False


def eating():
    global coins, points
    if maze_with_coins[(y + height // 2) // height - 1][(x + width // 2) // width - 1] == 2:
        maze_with_coins[(y + height // 2) // height - 1][(x + width // 2) // width - 1] = 0
        coins += 10
        points -= 1


def is_dying(en):
    if en.coordinate[0] == x and en.coordinate[1] == y:
        return True

f = False

def die():
    global lives, x, y, f
    if is_dying(en0) or is_dying(en1) or is_dying(en2):
        lives -= 1
        pygame.mixer.music.pause()
        #sound1.play()
        f = True
        x = xm + 2 * width + 12
        y = ym + 9 * width + 12
        en0.coordinate = enemies.Enemy.set_coordinate(en0, xm, ym, width)
        en1.coordinate = enemies.Enemy.set_coordinate(en1, xm, ym, width)
        en2.coordinate = enemies.Enemy.set_coordinate(en2, xm, ym, width)
    if lives == 0:
        return True
    else:
        return False


def end_game():
    if points == 0:
        winner()
        return True
    if die():
        game_over()
        return True
    return False

#walkU = [pygame.image.load('stay.png'), pygame.image.load('u1.png'), pygame.image.load('u2.png'),
         #pygame.image.load('u1.png'), pygame.image.load('stay.png')]
#walkD = [pygame.image.load('stay.png'), pygame.image.load('d1.png'), pygame.image.load('d2.png'),
         #pygame.image.load('d1.png'), pygame.image.load('stay.png')]
#walkL = [pygame.image.load('stay.png'), pygame.image.load('l1.png'), pygame.image.load('l2.png'),
         #pygame.image.load('l1.png'), pygame.image.load('stay.png')]
#walkR = [pygame.image.load('stay.png'), pygame.image.load('r1.png'), pygame.image.load('r2.png'),
         #pygame.image.load('r1.png'), pygame.image.load('stay.png')]


life = pygame.image.load('heart.png')
direction = 0
count = 0
######################################################    MAIN     ######################################################


clock = pygame.time.Clock()
run = True
start_event = True
end = False

#pygame.mixer.music.load("Kirby.wav")
#pygame.mixer.music.play(-1)
#sound1 = pygame.mixer.Sound("Death.wav")
l = -1
c = -1
k = -1
while run:
    clock.tick(1)

    #pygame.time.delay(50)
    # 0.05 sec
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if start_event:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            start_event = False
    elif end_game():
        pass
    else:
        press_keys()
        if path != 0:
            find_path(en0)
        moving()
        c = enemy_moving(en0, c)
        k = enemy_moving(en1, k)
        l = enemy_moving(en2, l)
    updating()

pygame.quit()

