"""
    Problem Statement Name : Multiples of 3 or 5
    
    Description : 
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000.
        
    Answer : 234168

"""


def solution(r: int, multiple_1: int, multiple_2: int) -> int:
    
    return sum([x for x in range(r) if x%multiple_1 == 0 or x%multiple_2 == 0])


if __name__ == '__main__':
    
    print(solution(1000, 3, 5))





