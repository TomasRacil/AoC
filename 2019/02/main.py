"""
Solution to 2. day of advent of code 2019
https://adventofcode.com/2019/day/2
"""

from os.path import realpath, dirname, join

def run_program(noun:int, verb:int, data:list)->int:
    data[1], data[2], inline=noun, verb, 0
    while inline<len(data):
        opt_code, position1, position2, output = data[inline], data[inline+1], data[inline+2], data[inline+3]
        if opt_code==1: data[output] = data[position1]+data[position2]
        elif opt_code==2: data[output] = data[position1]*data[position2]
        elif opt_code==99: break
        inline+=4
    return data[0]

def find_target(data:list, target:int)->tuple:
    for noun in range(0,100):
        for verb in range(0,100):
            if run_program(noun, verb, data[:])==target:
                return 100*noun+verb   


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [int(line) for line in file.read().split(',')]
    
    print(run_program(12,2,data[:]))
    print(find_target(data,19690720))
    
                
    

if __name__ == "__main__":
    main()