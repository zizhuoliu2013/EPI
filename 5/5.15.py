import random

def random_subset(n,k):
    changed_elements = {}
    for i in range(k):
        rand_idx = random.randint(i,n-1)
        rand_idx_mapped = changed_elements.get(rand_idx,rand_idx)
        i_mapped = changed_elements.get(i,i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
    return [changed_elements[i] for i in range(k)]

if __name__ == '__main__':
    print(random_subset(100,10))
