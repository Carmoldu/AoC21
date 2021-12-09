import numpy as np
from numpy import prod

with open('input.txt', 'r') as f:
    heightmap = f.read().splitlines()

heightmap = np.array([[int(number) for number in string] for string in heightmap])


def is_lowest_point(coordinates: (int, int), heightmap: np.array):
    y, x = coordinates

    is_left = x == 0
    is_right = x == (heightmap.shape[1] - 1)
    is_top = y == 0
    is_bottom = y == (heightmap.shape[0] - 1)

    return (
        (is_left or (heightmap[coordinates] < heightmap[y, x - 1]))
        and (is_right or (heightmap[coordinates] < heightmap[y, x + 1]))
        and (is_top or (heightmap[coordinates] < heightmap[y-1, x]))
        and (is_bottom or (heightmap[coordinates] < heightmap[y+1, x]))
    )


def find_basin_points(start_point: (int, int), heightmap: np.array):
    points_checked = [start_point]
    points_in_basin = [start_point]

    check_surrounding_points(start_point, heightmap, points_checked, points_in_basin)

    return points_in_basin


def check_surrounding_points(point, heightmap, points_checked, points_in_basin):
    y, x = point

    points_to_check = []
    if x != 0: points_to_check.append((y, x-1))
    if x != (heightmap.shape[1] - 1): points_to_check.append((y, x+1))
    if y != 0: points_to_check.append((y-1, x))
    if y != (heightmap.shape[0] - 1): points_to_check.append((y+1, x))

    for point in points_to_check:
        if point in points_checked:
            continue
        else:
            points_checked.append(point)

        if heightmap[point] != 9:
            points_in_basin.append(point)
            check_surrounding_points(point, heightmap, points_checked, points_in_basin)


lowest_points = np.zeros(heightmap.shape, dtype=bool)
lowest_points_coords = []
for x in range(heightmap.shape[1]):
    for y in range(heightmap.shape[0]):
        if is_lowest_point((y, x), heightmap):
            lowest_points[y, x] = True
            lowest_points_coords.append((y, x))

print(sum(heightmap[lowest_points]) + heightmap[lowest_points].size)


basin_sizes = []
for point_coords in lowest_points_coords:
    basin_points = find_basin_points(point_coords, heightmap)
    basin_sizes.append(len(basin_points))
basin_sizes.sort()
print(prod(basin_sizes[-3:]))

