import sys
import random

if (len(sys.argv) != 3):
    print("Usage instructions: python .\drunkard-walk.py <grid_size> <steps>")
    quit()


def create_map():
    SQUARE_SIZE = int(sys.argv[1])
    map_bounds = [["#"] * SQUARE_SIZE for _ in range(SQUARE_SIZE)]    # 50x50 map for our drunkard to walk in. Doing a [["#"] * 50] * 50 doesn't work since all the sublists are the exact same list.
    starting_coords = [int(SQUARE_SIZE/2), int(SQUARE_SIZE/2)]
    dir_array = ["N", "S", "W", "E"]
    map_bounds[starting_coords[0]][starting_coords[1]] = "S"
    for i in range(int(sys.argv[2])):
        char_to_write = "E" if i == (int(sys.argv[1]) - 1) else " "
        map_bounds[starting_coords[0]][starting_coords[1]] = "S" if starting_coords == [int(SQUARE_SIZE/2), int(SQUARE_SIZE/2)] else char_to_write
        # print(map_bounds)
        direction = dir_array[random.randrange(0, 4)]   # Pick a random direction
        if direction == "N" and starting_coords[0] < SQUARE_SIZE - 2:
            starting_coords[0] += 1
        elif direction == "S" and starting_coords[0] > 1:
            starting_coords[0] -= 1
        elif direction == "W" and starting_coords[1] > 1:
            starting_coords[1] -= 1
        elif direction == "E" and starting_coords[1] < SQUARE_SIZE - 2:  # Buffer of 1 so we don't hug edge (makes display ugly)
            starting_coords[1] += 1
        else:
            pass
            # print("The drunkard tries to go", direction, "but stumbles due to an invisible wall placed by the developer limitations.")
    return map_bounds

def print_map(bounds):
    for row in bounds:
        clean_str = ""
        for element in row:
            clean_str += element
        print(clean_str)

result = create_map()
# print_map(result)