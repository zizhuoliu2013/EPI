import random

def random_sampling(k,A):
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A[:k]

if __name__ == "__main__":
    A = list(range(100))
    print(random_sampling(10,A))
