# While the problem is the same, the increase in time requires some serious re-writing
# so that the code is scalable

import numpy as np

with open('input.txt', 'r') as f:
    fish = f.read()

time_left = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for f in fish.split(','):
    time_left[int(f)] += 1

for day in range(256):
    fish_reproducing = time_left[0]

    for rep_cycle in time_left.keys():
        if rep_cycle != 8:
            time_left[rep_cycle] = time_left[rep_cycle + 1]

    time_left[6] += fish_reproducing
    time_left[8] = fish_reproducing

    print(f'Day: {day} // {time_left}')

print(sum(list(time_left.values())))
