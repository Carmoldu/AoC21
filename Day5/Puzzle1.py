import numpy as np

with open('input.txt', 'r') as f:
    vents_raw = f.read().splitlines()

# Process vents and find maximum and minimum coordinate to be able to initialize a "board" afterwards
vents = []
max_x = 0
max_y = 0
for vent_raw in vents_raw:
    vent_raw = vent_raw.split(' -> ')
    vent = []
    for point_raw in vent_raw:
        point_raw = point_raw.split(',')
        point = [int(coord) for coord in point_raw]

        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]

        vent.append(point)
    vents.append(vent)

board = np.zeros((max_y+1, max_x+1))

for vent in vents:
    start_point, end_point = vent
    x_start, y_start = start_point
    x_end, y_end = end_point

    x_step = 1 if x_start <= x_end else -1
    y_step = 1 if y_start <= y_end else -1

    if x_start == x_end:
        for y_coord in range(y_start, y_end+y_step, y_step):
            board[y_coord, x_start] += 1

    elif y_start == y_end:
        for x_coord in range(x_start, x_end+x_step, x_step):
            board[y_start, x_coord] += 1
    else:
        for x_coord, y_coord in zip(range(x_start, x_end+x_step, x_step), range(y_start, y_end+y_step, y_step)):
            board[y_coord, x_coord] += 1

over_2 = np.zeros(board.shape)
over_2[np.where(board >= 2)] = 1
print(np.sum(over_2))