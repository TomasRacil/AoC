"""
Solution to 1. day of advent of code 2015
https://adventofcode.com/2015/day/1
"""

from os.path import realpath, dirname, join

def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [1 if char=='(' else -1 for char in file.read()]
    print(sum(data)) 
    floor:int = 0
    for idx,num in enumerate(data):
        floor+=num
        if floor==-1: 
            print(idx+1)
            break


if __name__ == "__main__":
    main()