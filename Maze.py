import random

n = 21

nm = 11
mazm = [ [0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1]
]

maz = [
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #1
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #2
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #3
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #4
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #5
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #6
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #7
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #8
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #9
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #10
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #11
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #12
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #13
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #14
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #15
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #16
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #17
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #18
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #19
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],#20
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]  #21
    ]

maz_with_coins = [
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #1
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #2
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #3
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #4
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #5
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #6
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #7
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #8
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #9
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #10
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #11
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #12
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #13
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #14
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #15
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #16
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #17
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], #18
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], #19
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],#20
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]  #21
    ]

c = 2
def first_generation():
    global c
    for i in range(n):
        for j in range(n):
            if(i%2 !=0 and j%2 !=0) and (i < n - 1 and j < n - 1):
                maz[i][j] = c
                c += 1
            else:
                maz[i][j] = 1


def final_generation():
    global c
    for i in range(n):
        for j in range(n):
            if maz[i][j] == 1:
                maz_with_coins[i][j] = 1
            else:
                maz_with_coins[i][j] = 2

    break_walls()
    maz[9][2] = c
    c += 1
    maz[9][9] = c
    c += 1
    maz[9][10] = c
    c += 1
    maz[9][11] = c
    c += 1


def break_walls():
    global c
    ran = random.randint(15, 25)
    for k in range(ran):
        i  = random.randint(1, 18)
        if i%2 != 0:
            i += 1
        j = random.randint(1, 18)
        if j%2 != 0:
            j += 1
        if maz[i][j] == 1 and ((maz[i - 1][j] == 1 and maz[i + 1][j] == 1
                                and maz[i][j + 1] != 1 and maz[i][j - 1] != 1)) \
                or ((maz[i - 1][j] != 1 and maz[i + 1][j] != 1
                     and maz[i][j + 1] == 1 and maz[i][j - 1] == 1)):
            maz[i][j] = c
            c += 1


neighbours = []
stack = []
visited = []
queue = []


def bfs():
    global c
    current = maz[1][1]
    while len(visited) != 100:
        if current not in visited:
            visited.append(current)
        d1, d2 = find_index(current)
        num, dirr = find_neighbours(d1, d2)
        if num != 0:  # если у клетки есть непосещенные соседи
            ran = random.randint(0, len(neighbours) - 1)
            next_cell = neighbours[ran]  # выбираем случайного соседа
            queue.append(next_cell)
            if next_cell not in visited:
                visited.append(next_cell)
            maz[d1 + dirr[ran][0]][d2 + dirr[ran][1]] = c  # убираем стену между текущей и соседней точками
            c += 1
        elif len(queue) > 0:  # если нет соседей, выбираем соседа в очереди как следующую точку
            current = queue.pop(0)
        else:  # если нет соседей и точек в стеке, но не все точки посещены, выбираем случайную из непосещенных
            unvisited_list = find_rand()
            current = random.choice(unvisited_list)
    neighbours.clear()
    visited.clear()
    queue.clear()


def dfs():
    global c
    current = maz[1][1]
    while len(visited) != 100:
        if current not in visited:
            visited.append(current)
        d1, d2 = find_index(current)
        num, dirr = find_neighbours(d1, d2)
        if num != 0:                               # если у клетки есть непосещенные соседи
            ran = random.randint(0, len(neighbours) - 1)
            next_cell = neighbours[ran]  # выбираем случайного соседа
            stack.append(current)                      # заносим текущую точку в стек
            maz[d1 + dirr[ran][0]][d2 + dirr[ran][1]] = c  # убираем стену между текущей и сосендней точками
            c += 1
            current = next_cell                        # делаем соседнюю точку текущей и отмечаем ее посещенной
        elif len(stack) > 0:  # если нет соседей, возвращаемся на предыдущую точку
            current = stack.pop()
        else:  # если нет соседей и точек в стеке, но не все точки посещены, выбираем случайную из непосещенных
            unvisited_list = find_rand()
            current = random.choice(unvisited_list)
    neighbours.clear()
    visited.clear()
    stack.clear()


def find_neighbours(k, o):
    num = 0
    direction = []
    neighbours.clear()
    if k - 2 > 0 and (maz[k - 2][o] > 1) and maz[k - 2][o] not in visited:
        neighbours.append(maz[k - 2][o])
        num += 1
        direction.append([-1, 0])
    if k + 2 < n and (maz[k + 2][o] > 1) and maz[k + 2][o] not in visited:
        neighbours.append(maz[k + 2][o])
        num += 1
        direction.append([1, 0])
    if o + 2 < n and (maz[k][o + 2] > 1) and maz[k][o + 2] not in visited:
        neighbours.append(maz[k][o + 2])
        num += 1
        direction.append([0, 1])
    if o - 2 > 0 and (maz[k][o - 2] > 1) and maz[k][o - 2] not in visited:
        neighbours.append(maz[k][o - 2])
        num += 1
        direction.append([0, -1])
    return num, direction


def find_index(current):
    for i in range(n):
        for j in range(n):
            if current == maz[i][j]:
                return i, j


def find_rand():
    unvisited_list = []
    for i in range(n):
        for j in range(n):
            if maz[i][j] > 1:
                unvisited_list.append(maz[i][j])
    return unvisited_list


def rint():
    for i in range(n):
        print(maz[i])