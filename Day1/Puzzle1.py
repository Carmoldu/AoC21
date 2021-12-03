with open('input.txt', 'r') as f:
    depths = f.read().splitlines()

depths = list(map(int, depths))

increased = 0
for i, depth in enumerate(depths):
    if i == 0:
        continue
    else:
        if (depth - depths[i-1]) > 0:
            increased += 1

print(increased)