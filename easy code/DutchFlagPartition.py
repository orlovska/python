# Write a program that takes an array A and an index i into A,
# and rearranges the elements such that all elements less than A[r] (the "pivot") 
# appear first, followed by elements equal to the pivot, 
# followed by elements greater than the pivot.
# Hint: Think about the partition step in quicksort.

def dutch_flag_partition(pivot_index, A):
    #dutch_flag_partition(4, [0,2,7,8,3,4,9,10,14,5,1])
    pivot = A[pivot_index]
    # pivot = 3
# First pass: group elernents smaller than pivot 
    smaller = 0
    for i in range(len(A)): #(0,1,2)
        if A[i] < pivot: # (1) 0 < 3 (2) 2 < 3 (10) 1 < 3
            A[i], A[smaller] = A[smaller], A[i]  # same, same, A[10] = 7, A[2] = 1 -> [0,2,1....7]
            smaller += 1
            # smaller = 1, 2
# Second pass; group elements Targer than pivot 
    larger = len(A) - 1
    # larger = 10
    for i in reversed(range(len(A))): #(10, 9, 8... 3)
        if A[i] < pivot: 
            break
        elif A[i] > pivot: #(1) 7 > 3 (2) 5 > 3 (3) 14 > 3 .... 8 > 3
            A[i], A[larger] = A[larger] , A[i] #same, same, same ....A[3] = 3, A[4] = 8
            larger -= 1
            # larger = 9,8,7.... 4
    return A
