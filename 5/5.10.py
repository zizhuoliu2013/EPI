def apply_permutation(perm, A):
    for i in range(len(A)):
        next = i
        while perm[next] >= 0 & next >= 0 :
            A[next], A[perm[next]] = A[perm[next]], A[next]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
            print(perm)
            print(A)
    perm[:] = [a + len(perm) for a in perm]

if __name__ == '__main__':
    perm = [3,1,4,0,2]
    A = [0,1,2,3,4]
    apply_permutation(perm,A)
    print(A)
