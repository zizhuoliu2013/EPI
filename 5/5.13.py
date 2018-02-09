import random

def online_random_sample(it,k):
    sampling_results =it[:k]
    num_seen_so_far = k - 1
    for x in it[k:]:
        num_seen_so_far += 1
        idx_to_replace = random.randint(0,num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x
    return sampling_results

if __name__ == '__main__':
    it = [1,2,3,4,5,6]
    print(online_random_sample(it,2))
