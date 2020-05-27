from sys import getsizeof
import collections
from operator import attrgetter

RECTANGLE = collections.namedtuple('RECTANGLE',('x','y','height','width'))
R1 = RECTANGLE(5, 4, 1, 1)
R2 = RECTANGLE(3, 3, 2, 3)
R3 = RECTANGLE(1, 2, 2, 3)
R4 = RECTANGLE(1, 1, 2, 1)
R5 = RECTANGLE(6, 5, 1, 2)
List = [R1, R2, R3, R4, R5]


print(getsizeof(List))

def rectangle_intersection(list):
    X = sorted(List, key=attrgetter('x','width'))

    Result = []

    index = 0
    while index != len(X)-1:
        RA, RB = X[index], X[index + 1]
        if RA.x + RA.width > RB.x:
            newX = max(RA.x, RB.x)
            newY = max(RA.y, RB.y)
            Xend = min(RA.x + RA.width, RB.x + RB.width)
            new_widht = Xend - newX

            Yend = min(RA.y + RA.height, RB.y + RB.height)
            new_height = Yend - newY

            Result.append(RECTANGLE(newX,newY,new_widht,new_height))
        
        index += 1

    return(Result)

print(rectangle_intersection(List))