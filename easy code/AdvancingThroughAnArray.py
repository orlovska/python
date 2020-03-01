# Write a program which takes an array of n integers, 
# where A[i] denotes the maximum you can advance from index 1, 
# and retums whether it is possible to advance to the last index 
# starting from the beginning of the array.
# Hint: Analyze each location, starting from the beginning.

def can_reach_end(A):
    
    if len(A) == 1:
        return True
    count, index = 1, -2
    while A[index] < count:
        count, index = count + 1, index - 1
        if count == len(A): 
            return False
    return can_reach_end((A[:index+1]))
         


    