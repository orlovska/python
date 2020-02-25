# 
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:

        if equal < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            equal, smaller = equal + 1, smaller + 1

        elif equal == pivot:
            equal =+ 1
            
        else:
            larger =- 1
            A[equal], A[larger] = A[larger], A[equal]
    return A
