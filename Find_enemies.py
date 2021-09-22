import random

n = 21
neighbours = []
stack = []
visited = []
queue = []
path = []
maz = []
parents = []


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
        num, dirr = find_neighbours(d1, d2)
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


def dfs_find(maze, start, enemy):
    global maz
    maz = maze
    new_change()
    start = abs(start)
    enemy = abs(enemy)
    current = start
    neighbours.clear()
    visited.clear()
    stack.clear()
    path.clear()
    while current != enemy:
        #print("Current: ", current)
        if current not in visited:
            visited.append(current)
        d1, d2 = find_index(current)
        num, dirr = find_neighbours(d1, d2)
        if enemy in neighbours:
            stack.append(current)
            parents[enemy] = current
            stack.append(enemy)
            current = enemy
        elif num != 0:                                # если у клетки есть непосещенные соседи
            ran = random.randint(0, len(neighbours) - 1)
            next_cell = neighbours[ran]               # выбираем случайного соседа
            parents[next_cell] = current
            stack.append(current)                     # заносим текущую точку в стек
            current = next_cell                       # делаем соседнюю точку текущей и отмечаем ее посещенной
        elif len(stack) > 0:  # если нет соседей, возвращаемся на предыдущую точку
            current = stack.pop()
    current = enemy
    path.append(current)
    while current != start:
        current = parents[current]
        path.append(current)
    return path


def ucs_find(maze, start, enemy):
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
        num, dirr = find_neighbours(d1, d2)
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
            queue.sort()
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


def find_neighbours(k, o):
    global maz
    num = 0
    direction = []
    neighbours.clear()
    if k - 1 > 0 and (maz[k - 1][o] != 1) and maz[k - 1][o] not in visited:
        neighbours.append(maz[k - 1][o])
        num += 1
        direction.append([-1, 0])
    if k + 1 < n and (maz[k + 1][o] != 1) and maz[k + 1][o] not in visited:
        neighbours.append(maz[k + 1][o])
        num += 1
        direction.append([1, 0])
    if o + 1 < n and (maz[k][o + 1] != 1) and maz[k][o + 1] not in visited:
        neighbours.append(maz[k][o + 1])
        num += 1
        direction.append([0, 1])
    if o - 1 > 0 and (maz[k][o - 1] != 1) and maz[k][o - 1] not in visited:
        neighbours.append(maz[k][o - 1])
        num += 1
        direction.append([0, -1])
    #print("Num of directions: ", num)
    return num, direction


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