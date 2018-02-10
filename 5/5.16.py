import bisect
import random
import itertools

def nonuniform_random_number_generator(values, probabilities):
    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(prefix_sum_of_probabilities,random.random())
    return values[interval_idx]

if __name__ == '__main__':
    values = [3,5,7,11]
    probabilities = [9/18, 6/18, 2/18, 1/18]
    print(nonuniform_random_number_generator(values, probabilities))
