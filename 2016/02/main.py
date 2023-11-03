"""
Solution to 2. day of advent of code 2016
https://adventofcode.com/2016/day/2
"""

from os.path import realpath, dirname, join

class Keypad:
    code: list = [[],[]]
    keypad:list[list[int]] = [[1,2,3],[4,5,6],[7,8,9]]
    keypad2:list[list[int]] = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,"A","B","C",0],[0,0,"D",0,0]]
    position: list[int]= [1,1]
    position2: list[int] = [2,0]

    def solve_one_part(self, sequence:list[str])->tuple[int]:
        
        for com in sequence:
            if com=="U": 
                self.position[0]-=1

                if self.keypad2[self.position2[0]-1][self.position2[1]]!=0:
                    self.position2[0]-=1
                if self.position2[0]<0: self.position2[0]=0

            elif com=="D": 
                self.position[0]+=1
                
                try:
                    if self.keypad2[self.position2[0]+1][self.position2[1]]!=0:
                        self.position2[0]+=1
                except:
                    pass
                # if self.position2[0]>4: self.position2[0]=4


            elif com=="R": 
                self.position[1]+=1

                try:
                    if self.keypad2[self.position2[0]][self.position2[1]+1]!=0:
                        self.position2[1]+=1
                except:
                    pass
                # if self.position2[1]>4: self.position2[1]=4

                

            else: 
                self.position[1]-=1

                if self.keypad2[self.position2[0]][self.position2[1]-1]!=0:
                    self.position2[1]-=1
                
                if self.position2[1]<0: self.position2[1]=0
                


            if self.position[1]<0: self.position[1]=0
            if self.position[1]>2: self.position[1]=2
            if self.position[0]<0: self.position[0]=0
            if self.position[0]>2: self.position[0]=2

        return (self.keypad[self.position[0]][self.position[1]], self.keypad2[self.position2[0]][self.position2[1]])

    def solve_code(self, sequences:list[list[str]]):
        for sequence in sequences:
            res = self.solve_one_part(sequence)
            self.code[0].append(res[0])
            self.code[1].append(res[1])


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        data = [[comand for comand in commands] for commands in file.read().split("\n")]

    print(data)
    k = Keypad()
    k.solve_code(data)
    print(k.code)


if __name__ == "__main__":
    main()