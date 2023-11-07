"""
Solution to 1. day of advent of code 2018
https://adventofcode.com/2018/day/1
"""

from os.path import realpath, dirname, join



def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [int(line) for line in file.read().split('\n')]
    print(sum(data))
    idx = 0
    frequencies = [0]
    while True:
        frequencies.append(frequencies[-1]+data[idx%len(data)])
        idx+=1
        if frequencies.count(frequencies[-1])>1:
            print(frequencies[-1])
            break

if __name__ == "__main__":
    main()