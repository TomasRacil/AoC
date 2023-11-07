"""
Solution to 2. day of advent of code 2018
https://adventofcode.com/2018/day/2
"""

from os.path import realpath, dirname, join

def find_difference(first_list:list[chr], second_list:list[chr])->int:
    # chars = set(first_list+second_list)
    # difference=0
    # for char in chars:
    #     difference+=abs(first_list.count(char)-second_list.count(char))
    # return difference
    difference=0
    for idx,char in enumerate(first_list):
        difference+=1 if char!=second_list[idx] else 0
    return difference



def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data=[row for row in file.read().split('\n')]

    firt_part= [[ row.count(char) for char in set(row)] for row in data]
    twice, trice =0,0

    for row in firt_part:
        if 2 in row: twice+=1
        if 3 in row: trice+=1
    
    print(twice, trice, twice*trice)
    for idx, row1 in enumerate(data):
        for row2 in data[idx+1:]:
            if find_difference(row1,row2)==1:
                print(row1,row2)
                print(set(row1).intersection(set(row2)))

    

if __name__ == "__main__":
    main()