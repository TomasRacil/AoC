"""
Solution to 3. day of advent of code 2019
https://adventofcode.com/2019/day/3
"""

from os.path import realpath, dirname, join

def get_coord(wire:list)->list:
    coord = [(0,0)]
    for dir,dist in wire:
        for _ in range(dist):
            if dir == 'U': coord.append((coord[-1][0],coord[-1][1]+1))
            elif dir =='D': coord.append((coord[-1][0],coord[-1][1]-1))
            elif dir =='L': coord.append((coord[-1][0]-1,coord[-1][1]))
            elif dir =='R': coord.append((coord[-1][0]+1,coord[-1][1]))
    return coord


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [[(command[0],int(command[1:])) for command in part.split(',')] for part in file.read().split('\n')]
    
    
    wire1 = get_coord(data[0])
    wire2 = get_coord(data[1])
    print(sorted([abs(item[0])+abs(item[1]) for item in set(wire1).intersection(set(wire2))])[1])
    
    print(sorted([wire1.index(intersection)+wire2.index(intersection) for intersection in set(wire1).intersection(set(wire2))])[1])
    
                
    

if __name__ == "__main__":
    main()