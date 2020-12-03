import itertools
import unittest

# "Quantum Entanglement Factor" (product of the values in the group)
def get_qe_factor(group):
    qe = 1
    for item in group:
        qe *= item
    return qe

# return all of the groups (with the fewest members) whose combinations sum to the target
def get_smallest_groups(data):
    target_weight = int(sum(data) / 3)
    smallest_groups = []
    print('target weight {}'.format(target_weight))
    for group_size in range(1, len(data) - 2):
        print('Searching for group size {}'.format(group_size))
        for candidate_group in itertools.combinations(data, group_size):
            if (sum(candidate_group) == target_weight):
                smallest_groups.append(list(candidate_group))

        if len(smallest_groups) > 0:
            print("There are {}  groups".format(len(smallest_groups)))
            # Sort them by QE factor
            smallest_groups.sort(key=lambda x: get_qe_factor(x))
            for small_group in smallest_groups:
                if is_group_valid(data, small_group):
                    return get_qe_factor(small_group)



def is_group_valid(data, small_group):
    # Group is valid if, when the values for the small group are removed from the big group
    # the remaining group can be split into two groups which are both the same size as the small group.
    remaining = list(set(data) - set(small_group))
    target_weight = sum(small_group)
    # Start searching for groups that are larger than the smallest group
    for group_size in range(len(small_group), len(data) - len(small_group) - 1):
        print('Testing {} ({}) searching group size {}'.format(small_group, get_qe_factor(small_group), group_size))
        for candidate_group in itertools.combinations(remaining, group_size):
            if (sum(candidate_group) == target_weight): 
                print("Done!")
                return True



test_input = [1,2,3,4,5,7,8,9,10,11]
tc = unittest.TestCase()
tc.assertEqual(99, get_smallest_groups(test_input))

with open('./input.txt') as f:
    lines = f.readlines()
    problem_input = [int(element) for element in lines]

    print(get_smallest_groups(problem_input))
    tc.assertEqual(10723906903, get_smallest_groups(problem_input))