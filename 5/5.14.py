import random

def compute_random_permutation(n):
    permutation = list(range(n))
    for i in range(n):
        r = random.randint(i,n-1)
        permutation[i], permutation[r] = permutation[r], permutation[i]
    return permutation

if __name__ == '__main__':
    print(compute_random_permutation(10))
