with open('input.txt', 'r') as f:
    crab_positions = [int(position) for position in f.read().split(',')]

position_count = {unique_position: crab_positions.count(unique_position)
                  for unique_position in set(crab_positions)}

print(position_count)

position_cost = {}
for position in range(min(crab_positions), max(crab_positions)+1):
    position_cost[position] = 0

    for crab_position, crabs_in_position in position_count.items():
        position_cost[position] += abs(crab_position - position) * crabs_in_position

print(position_cost)

min_cost_position = min(position_cost, key=position_cost.get)
print(f"Minimum cost position: {min_cost_position} // fuel cost: {position_cost[min_cost_position]}")