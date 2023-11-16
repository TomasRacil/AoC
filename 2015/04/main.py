"""
Solution to 4. day of advent of code 2015
https://adventofcode.com/2015/day/4
"""

import hashlib


def main():
    """
    main
    """
    
    secret:str = "iwrupvqb"
    number:int = 1
    to_found:int = 5
    
    while True:
        test = secret+str(number)
        result = hashlib.md5(test.encode()).hexdigest()
        if result[:to_found]=="0"*to_found:
            print(number)
            to_found+=1
        number+=1
        if to_found>6:break;
    
    
if __name__ == "__main__":
    main()