"""
Solution to 2. day of advent of code 2017
https://adventofcode.com/2017/day/2
"""

from os.path import realpath, dirname, join

def find_result_evenly_divisible_values(numbers:list[int])->int:
    for idx, divident in enumerate(sorted(numbers,reverse=True)):
        for divisor in sorted(numbers, reverse=True)[idx:]:
            if divident%divisor == 0 and divident/divisor!=1:
                return int(divident/divisor)


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [[int(number) for number in row.split('\t')] for row in file.read().split('\n')]
    check_sum = sum([max(row)-min(row) for row in data])
    print(check_sum)
    evenly_divisible = [find_result_evenly_divisible_values(row)   for row in data]
    print(sum(evenly_divisible))
    # followup_numbers = [number for idx,number in enumerate(data) if data[idx-1]==number]
    # print(sum(followup_numbers))
    # halfway_across_numbers = [number for idx,number in enumerate(data) if data[idx-int(len(data)/2)]==number]
    # print(sum(halfway_across_numbers))


if __name__ == "__main__":
    main()