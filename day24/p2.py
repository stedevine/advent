import itertools

# return all of the groups (with the fewest members) whose combinations sum to the target
def get_smallest_groups(data):
    target_weight = int(sum(data) / 3)
    smallest_groups = []
    print('target weight {}'.format(target_weight))
    for group_size in range(1, 7):
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
                    return
                #print('{} {}'.format(a, get_qe_factor(a)))
            #return smallest_groups

def get_qe_factor(group):
    qe = 1
    for item in group:
        qe *= item
    return qe

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
# Test this small group against the rest of the data
# We need to find two other valid groups into which the
# remaining data must be sorted
def get_next_smallest_group(data, small_group):
    target_weight = int(sum(data) / 3)
    print('Testing {}'.format(small_group))
    remaining = list(set(data)-set(small_group))
    #print(remaining)
    next_smallest_groups = []
    for group_size in range(len(small_group), len(data) -3 ):
        print('Searching remaining for group size {}'.format(group_size))
        for candidate_group in itertools.combinations(remaining, group_size):
            if (sum(candidate_group) == target_weight) and (sum(set(remaining) - set(candidate_group)) == target_weight):
                print('found')
                print(candidate_group)
                print(list(set(remaining) - set(candidate_group)))
                return True
                #next_smallest_groups.append(list(candidate_group))
        #if len(next_smallest_groups) > 0:
            #return next_smallest_groups

'''
def get_final_group(data, small_group, next_group):
    target_weight = int(sum(data) / 3)
    testing('{} and {}', small_group, next_group)
    remaining = list(set(data) - set(small_group) - set(next_group))
    
    for group_size in range(len(small_group)+len(ne), len(data) -3 ):
        print('Searching remaining for group size {}'.format(group_size))
        for candidate_group in itertools.combinations(remaining, group_size):
            if (sum(candidate_group) == target_weight):
                next_smallest_groups.append(list(candidate_group))
        if len(next_smallest_groups) > 0:
            return next_smallest_groups
'''
test_input = [1,2,3,4,5,7,8,9,10,11]
print(get_smallest_groups(test_input))
get_next_smallest_group(test_input,[9,11])
'''
for next_group in get_next_smallest_group(test_input, [9,11])):
    print(get_final_group(data, [9,11], next_group))
    '''

with open('./input.txt') as f:
    lines = f.readlines()
    input = [int(element) for element in lines]
    print(get_smallest_groups(input))