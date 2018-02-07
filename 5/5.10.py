def apply_permutation(perm, A):
    for i in range(len(A)):
        next_pos = i
        while perm[next_pos] >= 0:
            A[i], A[perm[next_pos]] = A[perm[next_pos]], A[i]
            temp = perm[next_pos]
            perm[next_pos] -= len(perm)
            next_pos = temp
    perm[:] = [a + len(perm) for a in perm]

if __name__ == '__main__':
    perm = [3,1,2,0]
    A = ['a','b','c','d']
    apply_permutation(perm,A)
    print(A)
