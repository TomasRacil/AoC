"""
Solution to 2. day of advent of code 2015
https://adventofcode.com/2015/day/2
"""

from os.path import realpath, dirname, join

def caculate_surface_size(dimenions:list[int])->int:
    sum1:int = dimenions[0]*dimenions[1]
    sum2:int = dimenions[1]*dimenions[2]
    sum3:int = dimenions[2]*dimenions[0]
    return min([sum1,sum2,sum3])+(sum1+sum2+sum3)*2

def calculate_ribon_lenght(dimenions:list[int])->int:
    lenght:int
    dimenions.sort()
    return dimenions[0]*dimenions[1]*dimenions[2]+(dimenions[0]+dimenions[1])*2 


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [[int(dim) for dim in present.split('x')] for present in file.read().splitlines()]
    
    paper = [caculate_surface_size(dim) for dim in data]
    bow = [calculate_ribon_lenght(dim) for dim in data]
    
    print(sum(paper))
    print(sum(bow))


if __name__ == "__main__":
    main()