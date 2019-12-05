import sys
import random

if (len(sys.argv) != 2):
    print("Usage instructions: python .\drunkard-walk.py <steps>")
    quit()

map_bounds = [["#"] * 50 for _ in range(50)]    # 50x50 map for our drunkard to walk in. Doing a [["#"] * 50] * 50 doesn't work since all the sublists are the exact same list.
starting_coords = [25, 25]
dir_array = ["N", "S", "W", "E"]

map_bounds[starting_coords[0]][starting_coords[1]] = "S"
for i in range(int(sys.argv[1])):
    char_to_write = "E" if i == (int(sys.argv[1]) - 1) else "."
    map_bounds[starting_coords[0]][starting_coords[1]] = "S" if starting_coords == [25, 25] else char_to_write
    # print(map_bounds)
    direction = dir_array[random.randrange(0, 4)]   # Pick a random direction
    if direction == "N" and starting_coords[0] < 48:
        starting_coords[0] += 1
    elif direction == "S" and starting_coords[0] > 1:
        starting_coords[0] -= 1
    elif direction == "W" and starting_coords[1] > 1:
        starting_coords[1] -= 1
    elif direction == "E" and starting_coords[1] < 48:  # Buffer of 1 so we don't hug edge (makes display ugly)
        starting_coords[1] += 1
    else:
        print("The drunkard tries to go", direction, "but stumbles due to an invisible wall placed by the developer limitations.")

for row in map_bounds:
    clean_str = ""
    for element in row:
        clean_str += element
    print(clean_str)
# for bound in map_bounds:
#     print(bound)