"""
Solution to 3. day of advent of code 2015
https://adventofcode.com/2015/day/3
"""

from os.path import realpath, dirname, join

def delivering(directions:list[chr])->set:
    visitited:list[tuple]=[(0,0)]
    curent_location = [0,0]
    for direction in directions:
        if direction == '>': curent_location[0]+=1
        if direction == '<': curent_location[0]-=1
        if direction == '^': curent_location[1]+=1
        if direction == 'v': curent_location[1]-=1
        visitited.append(tuple(curent_location))
    return set(visitited)


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [direction for direction in file.read()]
    
    santa = delivering(data)
    print(len(santa))
    santa = delivering(data[1::2])
    robosanta = delivering(data[0::2])
    print(len(santa|robosanta))


if __name__ == "__main__":
    main()