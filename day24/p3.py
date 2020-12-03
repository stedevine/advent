import itertools

# "Quantum Entanglement Factor" (product of the values in the group)
def get_qe_factor(group):
    qe = 1
    for item in group:
        qe *= item
    return qe

# Recursive function that determines if a given group can be split into smaller groups
def split_group(group, num_of_groups):

    if num_of_groups == 1:
        return True
    
    target_weight = int(sum(group) / num_of_groups)
    
    for group_size in range(2, len(group) - (num_of_groups -1)):
        print('Checking group {}'.format(group_size))
        valid_subgroups = []
        for candidate_group in itertools.combinations(group, group_size):
            #print('{} {} {}'.format(candidate_group, sum(candidate_group), target_weight))
            if (sum(candidate_group) == target_weight):
                valid_subgroups.append(candidate_group)
        
        valid_subgroups.sort(key=lambda x: get_qe_factor(x))

        for valid_subgroup in valid_subgroups:
            print('Checking valid group {}'.format(valid_subgroup))
            if split_group(list(set(group)-set(valid_subgroup)), num_of_groups - 1):
                print('found valid group {} {}'.format(valid_subgroup, get_qe_factor(valid_subgroup)))
                return True
                
    return False

test_input = [1,2,3,4,5,7,8,9,10,11]
split_group(test_input,3)
split_group(test_input,4)

with open('./input.txt') as f:
    lines = f.readlines()
    problem_input = [int(element) for element in lines]
    split_group(problem_input,3)
    split_group(problem_input,4)