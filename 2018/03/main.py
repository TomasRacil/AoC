"""
Solution to 3. day of advent of code 2018
https://adventofcode.com/2018/day/3
"""

from os.path import realpath, dirname, join

def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data=[[int(item) 
               for item 
               in claim.split()[-2][:-1].split(',') + claim.split()[-1].split('x')]
              for claim 
              in file.read().split('\n')]
    all_squares=set()
    duplicit_squares=set()
    for claim in data:
        for x in range(claim[0],claim[0]+claim[2]):
            for y in range(claim[1],claim[1]+claim[3]):
                if (x,y) in all_squares: duplicit_squares.add((x,y)) 
                all_squares.add((x,y))
    print(len(duplicit_squares))

    for idx,claim in enumerate(data):
        not_touch = True
        for x in range(claim[0],claim[0]+claim[2]):
            for y in range(claim[1],claim[1]+claim[3]):
                if (x,y) in duplicit_squares: 
                    not_touch = False
                    break
            if not_touch==False:
                break
        if not_touch == True:
            print(idx+1)

                
                
    # count=0
    # for square in set(claimed_squares):
    #     if claimed_squares.count(square)>1:
    #         count+=1
    # print(count)



if __name__ == "__main__":
    main()