import itertools

# "Quantum Entanglement Factor" (product of the values in the group)
def get_qe_factor(group):
    qe = 1
    for item in group:
        qe *= item
    return qe

# Recursive function that determines if a given group (of numbers) can be split into smaller groups 
# that sum to the same number. If so it returns a tuple containing the group and the qe factor
def split_group(group, num_of_groups):

    # base case - only one group
    if num_of_groups == 1:
        return (True,group, get_qe_factor(group))
    
    target_weight = int(sum(group) / num_of_groups)
    
    # To find a group  of size n whose values sum to the target weight
    # take each combination n values from the group and test their sum

    # Problem definition tells us to find the arrangement of groups
    # that contains a group with the fewest numbers, so start looking for the smallest possible group
    for group_size in range(2, len(group) - (num_of_groups -1)):

        # There may be more than one group of this size whose values fit
        valid_subgroups = []
        for candidate_group in itertools.combinations(group, group_size):
            if (sum(candidate_group) == target_weight):
                valid_subgroups.append(candidate_group)
        
        # The problem also tells us that, as a tie breaker, we should consider the 'qe factor'
        # sort the list of valid group in ascending qe factors.
        valid_subgroups.sort(key=lambda x: get_qe_factor(x))

        # Now recursively call this function on the sub group
        for valid_subgroup in valid_subgroups:
            #print('Checking valid group {}'.format(valid_subgroup))
            # The new input group is the input group with the values from the subgroup removed and the size is n-1
            if split_group(list(set(group)-set(valid_subgroup)), num_of_groups - 1)[0]:
                #print('found valid group {} {}'.format(valid_subgroup, get_qe_factor(valid_subgroup)))
                return (True, valid_subgroup, get_qe_factor(valid_subgroup))
                
    return (False, None, None)

test_input = [1,2,3,4,5,7,8,9,10,11]
print('test 1 {}'.format(split_group(test_input,3)[2]))
print('test 2 {}'.format(split_group(test_input,4)[2]))


with open('./input.txt') as f:
    lines = f.readlines()
    problem_input = [int(element) for element in lines]
    print('problem 1 {}'.format(split_group(problem_input,3)[2]))
    print('problem 2 {}'.format(split_group(problem_input,4)[2]))
