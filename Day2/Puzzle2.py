with open('input.txt', 'r') as f:
    orders = f.read().splitlines()
orders = [(order.split()[0], int(order.split()[1])) for order in orders]

horizontal = 0
depth = 0
aim = 0

for order in orders:
    if order[0] == 'forward':
        horizontal += order[1]
        depth += aim * order[1]
    elif order[0] == 'down':
        aim += order[1]
    elif order[0] == 'up':
        aim -= order[1]

print(horizontal*depth)