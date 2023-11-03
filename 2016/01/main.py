"""
Solution to 1. day of advent of code 2016
https://adventofcode.com/2016/day/1
"""

from os.path import realpath, dirname, join

class Santa:
    north:int = 0
    east:int = 0
    direction:list = ["N","E","S","W"]
    visited: list[tuple]=[(0,0)]

    def navigate(self, directions:tuple[str,int])->int:
        for direction in directions:
            if direction[0]=="R":
                dir = self.direction.pop(0)
                self.direction.append(dir)
            else:
                dir = self.direction.pop()
                self.direction.insert(0,dir)
            
            if self.direction[0]=="N":
                reach = self.north+direction[1]
                while self.north!= reach:
                    self.north+=1
                    self.visited.append((self.north, self.east))
            elif self.direction[0]=="S": 
                reach = self.north-direction[1]
                while self.north!= reach:
                    self.north-=1
                    self.visited.append((self.north, self.east))
            elif self.direction[0]=="E": 
                reach = self.east+direction[1]
                while self.east!= reach:
                    self.east+=1
                    self.visited.append((self.north, self.east))
            else: 
                reach = self.east-direction[1]
                while self.east!= reach:
                    self.east-=1
                    self.visited.append((self.north, self.east))
            # # if (self.north, self.east) in self.visited:
            # #     print(self.north, self.east)
            # self.visited.append((self.north, self.east))

        return self.north + self.east
    
    def get_twice_visited(self)->int:
        twice_visisted = []
        for item in self.visited:
            if self.visited.count(item)>1:
                return sum(item)




def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [(dir[0],int(dir[1:])) for dir in file.read().split(", ")]

    santa = Santa()
    print(santa.navigate(data))
    print(santa.get_twice_visited())


if __name__ == "__main__":
    main()