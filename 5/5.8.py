def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse = i % 2)

if __name__ == '__main__':
    A = [2,4,12,5,1,43,53]
    rearrange(A)
    print(A)
