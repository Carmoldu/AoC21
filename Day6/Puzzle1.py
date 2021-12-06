import numpy as np

with open('input.txt', 'r') as f:
    fish = f.read()

fish = np.array([int(time) for time in fish.split(',')])

for day in range(80):
    fish_reproducing = np.where(fish == 0)
    fish = fish - 1

    fish = np.append(fish, [8] * fish_reproducing[0].size)
    fish[fish_reproducing] = 6

    print(f'Day: {day}')

print(fish.size)