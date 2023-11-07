"""
Solution to 3. day of advent of code 2017
https://adventofcode.com/2017/day/3
"""

from os.path import realpath, dirname, join


def find_shortest_path(number: int)->list[int]:
    layer, last_number = 0, 1
    while number>=last_number:
        layer+=1
        for i in range(1,8,2):
            temp=last_number+layer*i
            if abs(number-temp)<=layer:
                print(layer,abs(number-temp))
                break
        last_number+=layer*8
    return layer+abs(number-temp)



def main():
    """
    main
    """

    print(find_shortest_path(325489))




if __name__ == "__main__":
    main()