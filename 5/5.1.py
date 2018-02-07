def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)-1
    while equal < larger:
        if A[equal] < pivot:
            A[smaller],A[equal] = A[equal],A[smaller]
            smaller, equal = smaller + 1, equal +1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1

if __name__ == "__main__":
    A = [-3,0,1,5,1,1,3,4,4,2]
    print("raw_data: ",A)
    dutch_flag_partition(2,A)
    print("partitioned_data:", A)
