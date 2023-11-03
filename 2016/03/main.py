"""
Solution to 3. day of advent of code 2016
https://adventofcode.com/2016/day/3
"""

from os.path import realpath, dirname, join




def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [[int(side) for side in triangle.split()] for triangle in file.read().split("\n  ")]
    valid_triangle = [triangle for triangle in data if sorted(triangle)[2]<(sorted(triangle)[0]+sorted(triangle)[1])]
    # print(data)
    print(len(valid_triangle))
    triangles2 = [[data[idx*3][0],data[idx*3+1][0],data[idx*3+2][0]] for idx, _ in enumerate(data[::3])]+[[data[idx*3][1],data[idx*3+1][1],data[idx*3+2][1]] for idx, _ in enumerate(data[::3])]+[[data[idx*3][2],data[idx*3+1][2],data[idx*3+2][2]] for idx, _ in enumerate(data[::3])]
    valid_triangle = [triangle for triangle in triangles2 if sorted(triangle)[2]<(sorted(triangle)[0]+sorted(triangle)[1])]
    print(len(valid_triangle))


if __name__ == "__main__":
    main()