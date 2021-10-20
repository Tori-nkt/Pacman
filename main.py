import pygame
import time
import Find_enemies
import Find_point

import enemies
from enemies import*
import random
import Maze
import MiniMax
import csv

just_pressed = False
# generation of maze with dfs algorithm
Maze.first_generation()
Maze.dfs()
Maze.final_generation()
maze = Maze.maz
Maze.maz = maze
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

mazez = [
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #1
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #2
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #3
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #4
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #5
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #6
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #7
    [0,1,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #8
    [0,1,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #9
    [0,1,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #10
    [0,1,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #11
    [0,1,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #12
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #13
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0], #14
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #15
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
speed = 4
coordinate = [2, 9]
distance = 23
lives = 3

# points
rmin = 3
rmax = 5
coins = 0
points = Maze.num_of_coins

# moving without player
goal = 0
next_point = 0
pacman_path = []

current_move = -1


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
            #if maze[i][j] < 0:
                #pygame.draw.rect(window, (192, 192, 192), (xm + j * width, ym + i * width, width, width))
            if maze[i][j] == 1:
                pygame.draw.rect(window, (50, 100, 232), (xm + j * width, ym + i * width, width, width))
            elif maze_with_coins[i][j] == 2:
                pygame.draw.circle(window, (255, 255, 255), (xm + j * width + 12, ym + i * width + 12), rmin)


def can_move(j, i):
    global direction, just_pressed
    yy = 0
    xx = 0
    ymod = (y - ym) %12
    xmod = (x-xm)%12
    if direction == 1 and ymod == 0:
        yy = 12
    elif direction == 2 and ymod == 0:
        yy = -12
    elif direction == 3 and xmod == 0:
        xx = 12
    elif direction == 4 and xmod == 0:
        xx = -12

    if just_pressed:
        if ymod == xmod and maze[(y - ym - yy) // height + 1][(x - xm - xx) // height] != 1 \
                and maze[(y - ym - yy) // height - 1][(x - xm - xx) // height] != 1 \
                and maze[(y - ym - yy) // height][(x - xm - xx) // height + 1] != 1:
            direction = -1
            return False
        elif ymod == xmod and maze[(y - ym) // height + 1][(x - xm) // height] != 1 \
                and maze[(y - ym) // height - 1][(x - xm) // height] != 1 \
                and maze[(y - ym) // height][(x - xm) // height - 1] != 1:
            direction = -1
            return False
        elif ymod == xmod and maze[(y - ym) // height][(x - xm) // height - 1] != 1\
                and maze[(y - ym) // height][(x - xm) // height + 1] != 1\
                and maze[(y - ym) // height - 1][(x - xm) // height] != 1:
            direction = -1
            return False
        elif ymod == xmod and maze[(y - ym) // height][(x - xm) // height - 1] != 1 \
                and maze[(y - ym) // height][(x - xm) // height + 1] != 1\
                and maze[(y - ym) // height + 1][(x - xm) // height] != 1:
            direction = -1
            return False
    if maze[(y + i - ym - yy) // height][(x + j - xm - xx) // height] != 1:
        # print("x = ", x)
        # print("y = ", y)
        # print([(y + i + height // 2 - yy) // height - 1],[(x + j + width // 2 - xx) // width - 1])
        # print("maze =", maze[(y + i + height // 2 - yy) // height - 1][(x + j + width // 2 - xx) // width - 1])
        return True
    else:
        #print([(y + i - ym - yy) // height], [(x + j - xm - xx) // height])
        #print("maze =", maze[(y + i - ym - yy) // height][(x + j - xm - xx) // height])
        return False

path = 0
enemy = 2
def press_keys():
    global direction, path, enemy, just_pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = 1
        just_pressed = False
    if keys[pygame.K_s]:
        direction = 2
        just_pressed = False
    if keys[pygame.K_a]:
        direction = 3
        just_pressed = False
    if keys[pygame.K_d]:
        direction = 4
        just_pressed = False
    if keys[pygame.K_1]:
        path = 1
        just_pressed = True
        if enemy == 1:
            find_path(en0)
        elif enemy == 2:
            find_path(en1)
        else:
            find_path(en2)
    if keys[pygame.K_2]:
        just_pressed = True
        path = 2
        if enemy == 1:
            find_path(en0)
        elif enemy == 2:
            find_path(en1)
        else:
            find_path(en2)
    if keys[pygame.K_3]:
        just_pressed = True
        path = 3
        if enemy == 1:
            find_path(en0)
        elif enemy == 2:
            find_path(en1)
        else:
            find_path(en2)
    if keys[pygame.K_4]:
        path = 0
    if keys[pygame.K_LEFT]:
        enemy = (enemy + 1) % 3 + 1
        print(enemy)


def find_path(en):
    global maze, just_pressed
    ene = maze[(en.coordinate[1] + height // 2) // height - 1][(en.coordinate[0]+ height // 2) // height - 1]
    start_time = time.time()
    if path == 1:
        if just_pressed:
            start_time = time.time()
        plist = Find_enemies.astar_find(maze, maze[(y + height // 2) // height - 1][(x + height // 2) // height - 1], ene)
        if just_pressed:
            print("--- %s seconds --- for dfs" % (time.time() - start_time))
        change(plist)
    if path == 2:
        if just_pressed:
            start_time = time.time()
        plist = Find_enemies.bfs_find(maze, maze[(y + height // 2) // height - 1][(x + height // 2) // height - 1], ene)
        if just_pressed:
            print("--- %s seconds --- for bfs" % (time.time() - start_time))
        change(plist)
    if path == 3:
        if just_pressed:
            start_time = time.time()
        plist = Find_enemies.ucs_find(maze, maze[(y + height // 2) // height - 1][(x + height // 2) // height - 1], ene)
        if just_pressed:
            print("--- %s seconds --- for ucs" % (time.time() - start_time))
        change(plist)


def change(el):
    global maze
    for i in range(n):
        for j in range(n):
            if maze[i][j] in el:
                maze[i][j] = -maze[i][j]


def find_rand():  # find random coin in maze
    unvisited_list = []
    for i in range(n):
        for j in range(n):
            if maze_with_coins[i][j] > 1:
                unvisited_list.append(maze[i][j])
    return random.choice(unvisited_list)


def find_index(current):
    for i in range(n):
        for j in range(n):
            if abs(current) == abs(maze[i][j]):
                #print("Current indexes: ", i, " ", j)
                return i, j


def pac_coor(i):
    return (i + height // 2) // height - 1


def enemies_moving_by_pac(en, choice):
    global y, x
    if current_move == 0:
        if (abs(pac_coor(en.coordinate[0]) - pac_coor(x)) + abs(pac_coor(en.coordinate[1]) - pac_coor(y))
                          <= 3 and (en.coordinate[0] == x or en.coordinate[1] == y) \
                and current_move == 0):
            ene = maze[(en.coordinate[1] + height // 2) // height - 1][(en.coordinate[0] + height // 2) // height - 1]
            enemy_path = Find_point.bfs_find(maze, maze[(y + height // 2) // height - 1][(x + height // 2) // height - 1],
                                               ene)
            enemy_path.pop(0)
            if len(enemy_path)!= 0:
                en.stalker = enemy_path.pop(0)

            i, j = find_index(en.stalker)
            if pac_coor(en.coordinate[1]) - i == 1 and pac_coor(en.coordinate[0]) - j == 0:
                choice = 0
            elif pac_coor(en.coordinate[1]) - i == -1 and pac_coor(en.coordinate[0]) - j == 0:
                choice = 1
            elif pac_coor(en.coordinate[1]) - i == 0 and pac_coor(en.coordinate[0]) - j == 1:
                choice = 2
            elif pac_coor(en.coordinate[1]) - i == 0 and pac_coor(en.coordinate[0]) - j == -1:
                choice = 3
    else:
        direct = list()
        flag = 0
        if can_enemy_move(en.coordinate[1], en.coordinate[0], 0, -speed - 15):  # up
            direct.append(0)
            if 0 == choice:
                flag = 1
        if can_enemy_move(en.coordinate[1], en.coordinate[0], 0, speed + 4):  # down
            direct.append(1)
            if 1 == choice:
                flag = 1
        if can_enemy_move(en.coordinate[1], en.coordinate[0], -speed - 10, 0):  # left
            direct.append(2)
            if 2 == choice:
                flag = 1
        if can_enemy_move(en.coordinate[1], en.coordinate[0], speed + 11, 0):  # right
            direct.append(3)
            if 3 == choice:
                flag = 1
        if flag != 1:
            choice = random.choice(direct)

    if choice == 0:
        en.coordinate[1] -= speed  # up
    elif choice == 1:
        en.coordinate[1] += speed  # down
    elif choice == 2:
        en.coordinate[0] -= speed  # left
    elif choice == 3:
        en.coordinate[0] += speed  # right
    return choice


def moving_minimax():
    global y, x, direction, just_pressed, goal, pacman_path, next_point
    if len(pacman_path) != 0:
        change(pacman_path)
    pacman_path.clear()
    coor_list = []
    for i in range(4):
        coor_list.append([pac_coor(En[i].coordinate[1]), pac_coor(En[i].coordinate[0])])
    if current_move == 0:
        direction = MiniMax.call_minimax(maze, [pac_coor(y), pac_coor(x)], coor_list, maze_with_coins)
        if direction == -1:
            goal = 0
            moving()
            return
    xx = 0
    yy = 0
    if direction == 1:
        yy = 3
    elif direction == 2:
        yy = -15
    elif direction == 3:
        xx = 10
    elif direction == 4:
        xx = -10
    if direction == 1:
        y -= speed
    elif direction == 2:
        y += speed
    elif direction == 3:
        if x - speed >= 22:
            x -= speed
        else:
            x = 502
    elif direction == 4:
        if x + speed <= 502:
            x += speed
        else:
            x = 22
    just_pressed = True
    eating()
    die()


def moving():
    global y, x, direction, just_pressed, goal, pacman_path, next_point
    die()
    if goal == 0:
        goal = find_rand()
        pacman_path = Find_enemies.astar_find(maze, maze[(y + height // 2) // height - 1][(x + height // 2) // height - 1],
                                        goal)
        pacman_path.reverse()
        change(pacman_path)
        next_point = pacman_path.pop(0)
    xx = 0
    yy = 0
    if direction == 1:
        yy = 3
    elif direction == 2:
        yy = -15
    elif direction == 3:
        xx = 10
    elif direction == 4:
        xx = -10
    if goal != abs(maze[(y + yy + height // 2) // height - 1][(x + xx + height // 2) // height - 1]):
        if next_point == abs(maze[(y + yy + height // 2) // height - 1][(x + xx + height // 2) // height - 1]):
            maze[(y + yy + height // 2) // height - 1][(x + xx + height // 2) // height - 1] =\
                abs(maze[(y + yy + height // 2) // height - 1][(x + xx + height // 2) // height - 1])

            next_point = pacman_path.pop(0)
            i, j = find_index(next_point)
            if ((y + height // 2) // height - 1) - i == 1 and ((x + height // 2) // height - 1) - j == 0:
                direction = 1
            elif ((y + height // 2) // height - 1) - i == -1 and ((x + height // 2) // height - 1) - j == 0:
                direction = 2
            elif ((y + height // 2) // height - 1) - i == 0 and ((x + height // 2) // height - 1) - j == 1:
                direction = 3
            elif ((y + height // 2) // height - 1) - i == 0 and ((x + height // 2) // height - 1) - j == -1:
                direction = 4
    else:
        goal = 0
        direction = -1

    if direction == 1:
        y -= speed
    elif direction == 2:
        y += speed
    elif direction == 3:
        if x - speed >= 22:
            x -= speed
        else:
            x = 502
    elif direction == 4:
        if x + speed <= 502:
            x += speed
        else:
            x = 22
    just_pressed = True
    eating()
    die()


def moving_old():
    global y, x, direction, just_pressed
    if direction == 1 and can_move(0, -speed):
        y -= speed
    elif direction == 2 and can_move(0, speed):
        y += speed
    elif direction == 3 and can_move(-speed, 0):
        if x - speed >= 22:
            x -= speed
        else:
            x = 502
    elif direction == 4 and can_move(speed, 0):
        if x + speed <= 502:
            x += speed
        else:
            x = 22
    just_pressed = True
    eating()


en0 = Enemy(0, xm, ym, width)
en1 = Enemy(1, xm, ym, width)
en2 = Enemy(2, xm, ym, width)
en3 = Enemy(3, xm, ym, width)
En = [en0, en1, en2, en3]


def draw_enemy():
    for i in range(4):
        pygame.draw.circle(window, En[i].pic, (En[i].coordinate[0], En[i].coordinate[1]), radius - 3)


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
    if can_enemy_move(en.coordinate[1], en.coordinate[0], 0, -speed - 15):  # up
        direct.append(0)
        if 0 == choice:
            flag = 1
    if can_enemy_move(en.coordinate[1], en.coordinate[0], 0, speed + 4):   # down
        direct.append(1)
        if 1 == choice:
            flag = 1
    if can_enemy_move(en.coordinate[1], en.coordinate[0], -speed - 10, 0):  # left
        direct.append(2)
        if 2 == choice:
            flag = 1
    if can_enemy_move(en.coordinate[1], en.coordinate[0], speed + 11, 0):   # right
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
    if (en.coordinate[0] - 4 <= x <= en.coordinate[0] + 4) \
            and (en.coordinate[1] - 4 <= y <= en.coordinate[1] + 4):
        return True

f = False

def die():
    global lives, x, y, f, goal, current_move
    if is_dying(En[0]) or is_dying(En[1]) or is_dying(En[2]) or is_dying(En[3]):
        lives -= 1
        goal = 0
        current_move = -1
        pygame.mixer.music.pause()
        #sound1.play()
        f = True
        x = xm + 2 * width + 12
        y = ym + 9 * width + 12
        for i in range(4):
            En[i].coordinate = enemies.Enemy.set_coordinate(En[i], xm, ym, width)
    if lives == 0:
        return True
    else:
        return False


def end_game():
    if points == 0:
        if write_flag:
            write_statistic("Win")
        winner()
        return True
    if die():
        if write_flag:
            write_statistic("Lose")
        game_over()
        return True
    return False

write_flag = True
def write_statistic(winner):
    global write_flag
    data = winner + " " + str(coins)
    with open("data.txt", "a") as file:
        file.write(data + '\n')
    write_flag = False
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

for_enemies = [-1, -1, -1, -1]
while run:

    clock.tick(40)
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
        current_move += 1
        if current_move > 5:
            current_move = 0
        press_keys()
        if path != 0:
            if enemy == 1:
                find_path(en0)
            elif enemy == 2:
                find_path(en1)
            else:
                find_path(en2)
        for i in range(4):
            for_enemies[i] = enemies_moving_by_pac(En[i], for_enemies[i])
        moving_minimax()
        #moving()
        change(pacman_path)
    updating()

pygame.quit()

