import random

n = 21
neighbours = []
stack = []
visited = []
queue = []
path = []
maz = []
parents = []

weights = [
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #1
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #2
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #3
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #4
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #5
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #6
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #7
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #8
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #9
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #10
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #11
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #12
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #13
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #14
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #15
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #16
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #17
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #18
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0], #19
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0],#20
    [0,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,500,0]  #21
    ]


def update_weights():
    for i in range(n):
        for j in range(n):
            weights[i][j] = 500


def bfs_find(maze, start, enemy):
    global maz
    maz = maze
    new_change()
    start = abs(start)
    current = start
    enemy = abs(enemy)
    neighbours.clear()
    visited.clear()
    queue.clear()
    path.clear()
    while current != enemy:
        if current not in visited:
            visited.append(current)
        d1, d2 = find_index(current)
        num, dir, dirr = find_neighbours(d1, d2)
        if enemy in neighbours:
            parents[enemy] = current
            queue.append(enemy)
            current = enemy
        elif num != 0:  # если у клетки есть непосещенные соседи
            ran = random.randint(0, len(neighbours) - 1)
            next_cell = neighbours[ran]  # выбираем случайного соседа
            parents[next_cell] = current
            queue.append(next_cell)
            if next_cell not in visited:
                visited.append(next_cell)
        elif len(queue) > 0:  # если нет соседей, выбираем соседа в очереди как следующую точку
            current = queue.pop(0)

        else:  # если нет соседей и точек в стеке, но не все точки посещены, выбираем случайную из непосещенных
            unvisited_list = find_rand()
            current = random.choice(unvisited_list)
    current = enemy
    path.append(current)
    while current != start:
        current = parents[current]
        path.append(current)
    return path


def new_change():
    global maz, parents
    parents = [0] * (n * n + 2)
    for i in range(n):
        for j in range(n):
            if maz[i][j] < 0:
                maz[i][j] = -maz[i][j]




def choose_path(k, o):
    min = 10000
    neighbour = 0
    if k - 1 > 0 and (maz[k - 1][o] != 1):
        if min > weights[k - 1][o]:
            min = weights[k - 1][o]
            neighbour = maz[k - 1][o]
    if k + 1 < n and (maz[k + 1][o] != 1):
        if min > weights[k + 1][o]:
            min = weights[k + 1][o]
            neighbour = maz[k + 1][o]
    if o + 1 < n and (maz[k][o + 1] != 1):
        if min > weights[k][o + 1]:
            min = weights[k][o + 1]
            neighbour = maz[k][o + 1]
    if o - 1 > 0 and (maz[k][o - 1] != 1):
        if min > weights[k][o - 1]:
            neighbour = maz[k][o - 1]
    return neighbour


def h(a, b):
    i, j = find_index(a)
    k, l = find_index(b)
    return abs(i - k) + abs(j - l)


def find_neighbours(k, o):
    global maz
    num = 0
    dir = []
    dirr = []
    neighbours.clear()
    if k - 1 > 0 and (maz[k - 1][o] != 1) and maz[k - 1][o] not in visited:
        neighbours.append(maz[k - 1][o])
        num += 1
        dir.append(-1)
        dirr.append(0)
    if k + 1 < n and (maz[k + 1][o] != 1) and maz[k + 1][o] not in visited:
        neighbours.append(maz[k + 1][o])
        num += 1
        dir.append(1)
        dirr.append(0)
    if o + 1 < n and (maz[k][o + 1] != 1) and maz[k][o + 1] not in visited:
        neighbours.append(maz[k][o + 1])
        num += 1
        dir.append(0)
        dirr.append(1)
    if o - 1 > 0 and (maz[k][o - 1] != 1) and maz[k][o - 1] not in visited:
        neighbours.append(maz[k][o - 1])
        num += 1
        dir.append(0)
        dirr.append(-1)
    #print("Num of directions: ", num)
    return num, dir, dirr


def find_index(current):
    for i in range(n):
        for j in range(n):
            if current == maz[i][j]:
                #print("Current indexes: ", i, " ", j)
                return i, j


def find_rand():
    unvisited_list = []
    for i in range(n):
        for j in range(n):
            if maz[i][j] > 1:
                unvisited_list.append(maz[i][j])
    return unvisited_list
