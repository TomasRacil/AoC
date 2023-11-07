"""
Solution to 1. day of advent of code 2017
https://adventofcode.com/2017/day/1
"""

from os.path import realpath, dirname, join



def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [int(number) for number in file.read()]
    followup_numbers = [number for idx,number in enumerate(data) if data[idx-1]==number]
    print(sum(followup_numbers))
    halfway_across_numbers = [number for idx,number in enumerate(data) if data[idx-int(len(data)/2)]==number]
    print(sum(halfway_across_numbers))


if __name__ == "__main__":
    main()