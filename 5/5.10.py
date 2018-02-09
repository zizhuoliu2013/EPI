def apply_permutation(perm, A):
    for i in range(len(A)):
        next_pos = i
        while perm[next_pos] >= 0:
            if i == perm[next_pos]:
                perm[next_pos] -= len(perm)
                break
            A[next_pos], A[perm[next_pos]] = A[perm[next_pos]], A[next_pos]
            temp = perm[next_pos]
            perm[next_pos] -= len(perm)
            next_pos = temp
    perm[:] = [a + len(perm) for a in perm]

if __name__ == '__main__':
    A = ['a','b','c','d','e']
    perm = [4,1,0,3,2]
    apply_permutation(perm,A)
    print(A)
