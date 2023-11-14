"""
Solution to 1. day of advent of code 2019
https://adventofcode.com/2019/day/1
"""

from os.path import realpath, dirname, join
from math import floor

def calculate_fuel(weight:int)->int:
    required_fuel=(floor(weight/3)-2)
    if required_fuel>0: return required_fuel + calculate_fuel(required_fuel)
    else: return 0

def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [int(line) for line in file.read().split('\n')]
    print(sum([(floor(weight/3)-2) for weight in data]))
    
    print(sum([calculate_fuel(weight) for weight in data]))
    

if __name__ == "__main__":
    main()