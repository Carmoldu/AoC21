with open('input.txt', 'r') as f:
    depths = f.read().splitlines()
depths = list(map(int, depths))

rolling_window_size = 3

increase_count = 0
for i, depth in enumerate(depths):
    if i < rolling_window_size:
        continue
    else:
        current_window = depth + depths[i-1] + depths[i-2]
        previous_window = depths[i-1] + depths[i-2] + depths[i-3]

        if current_window > previous_window:
            increase_count += 1

print(increase_count)