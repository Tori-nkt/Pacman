import random

from enemies import*
MAX, MIN = 1000, -1000
player_coordinate = []
best_move = 0
# 1  up
# 2  down
# 3  left
# 4  right
maze = [
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
maze_with = [
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
possible_moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
enemi = []
n = 21
path = []
max_val = 0
flag = True

def final_generation(maz):
    for i in range(n):
        for j in range(n):
            if maz[i][j] == 1:
                maze[i][j] = 1
            else:
                maze[i][j] = 0


def call_minimax(mazes, coordinates, ene, maze_with_c):
    global maze, player_coordinate, enemi, maze_with, max_val, best_move, flag
    flag = True
    final_generation(mazes)
    maze_with = maze_with_c
    enemi = ene
    for i in range(4):
        maze[enemi[i][0]][enemi[i][1]] = i + 4
    player_coordinate = coordinates
    path.clear()
    path.append([player_coordinate[0], player_coordinate[1]])
    test = random.randint(2, 7)
    max_val = 0
    best_move = 0
    max_val = minimax(0, True, MIN, MAX, 6)
    if max_val == 0 and flag:
        best_move = -1
    return best_move


def heuristic():
    global flag
    temp = 0
    for i in range(len(path)):
        if maze[path[i][0]][path[i][1]] > 3:
            flag = False
            return -1
        if maze_with[path[i][0]][path[i][1]] == 2:
            temp += 1
    return temp


def can_move(player, moves, num_enemy):
    if player:
        i = player_coordinate[0] + possible_moves[moves][0]
        j = player_coordinate[1] + possible_moves[moves][1]
        if maze[i][j] != 1:
            return True
        else:
            return False
    else:
        i = enemi[num_enemy][0] + possible_moves[moves][0]
        j = enemi[num_enemy][1] + possible_moves[moves][1]
        if maze[i][j] != 1:
            return True
        else:
            return False


def move(player, moves, num):
    operation = 1
    if moves < 0:
        operation = -1
    moves = abs(moves) - 1
    if player:
        player_coordinate[0] = player_coordinate[0] + possible_moves[abs(moves)][0] * operation
        player_coordinate[1] = player_coordinate[1] + possible_moves[abs(moves)][1] * operation

    else:
        enemi[num][0] = enemi[num][0] + possible_moves[abs(moves)][0] * operation
        enemi[num][1] = enemi[num][1] + possible_moves[abs(moves)][1] * operation
        maze[enemi[num][0]][enemi[num][1]] = num + 4


def minimax(depth, player, alpha, beta, test):
    global best_move, max_val
    if depth == test:
        return heuristic()
    moves = 4
    minmax = 0
    if player: minmax = MIN
    else:
        minmax = MAX
        moves = 16

    for i in range(moves):
        if can_move(player, i % 4, i // 4):
            move(player, (i % 4) + 1, i // 4)
            if player:
                path.append([player_coordinate[0], player_coordinate[1]])
            val = minimax(depth + 1, not player, alpha, beta, test)
            if player:
                path.pop(len(path) - 1)
            move(player, -((i % 4)+1), i // 4)
            if player:
                minmax = max(minmax, val)
                alpha = max(alpha, minmax)
                if depth == 0 and max_val <= val:
                    max_val = val
                    best_move = i + 1
            else:
                minmax = min(minmax, val)
                beta = min(beta, minmax)
            if beta <= alpha:
                break
    if best_move == -1:
        return heuristic()
    return minmax
