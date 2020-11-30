import itertools

def get_result(gifts):
    valid_sets = []
    total_weight = 0
    for gift in gifts:
        total_weight += gift
    
    target_weight = int(total_weight / 3)
    for com_length in range(2,len(gifts) - 1):
        for com in itertools.combinations(gifts,com_length):
            if sum(com) == target_weight:
                #print('{} {} {} {}'.format(type(com),com[0], com[1], com))

                valid_sets.append(set(com))
                print(com)
    
    #print(valid_sets)

    gifts = set(gifts)
    #print(valid_sets)

    results = []
    for valid_set in valid_sets:
        remaining_gifts = set(gifts - valid_set)
        for v2 in valid_sets:
            if (remaining_gifts - v2) in valid_sets:
                results.append([valid_set, v2, (remaining_gifts - v2)])
                [r.sort(key=len) for r in results]


    #print(results)

    final = set()
    for result in results:
        count = 0
        qe = 1
        for element in result[0]:
            count += 1
            qe *= element
        final.add((count,qe))
    
    final = list(final)
    final.sort()
    print(final)
        
                #print('{} {} {}'.format(valid_set, v2, (remaining_gifts - v2)))
                #results.append
        #if third in gifts:
        #print('{} {}'.format(valid_set, remaining_gifts))
        #print(gifts - valid_set)

        #print('{} {}'.format(valid_set, valid_sets - valid_set))



    '''
    gifts = set(gifts)
    for valid_set in valid_sets:
        valid_set = set(valid_set)
        remaining_gifts = gifts - valid_set
        #print('{} {}'.format(valid_set, remaining_gifts))
        for remaining_set in (valid_sets - valid_set):
            remaining_set = set(remaining_set)
            #print('{} {}'.format(valid_set,remaining_set))
            #if (remaining_gifts - remaining_set) in valid_sets:
             #   print('{} {} {}'.format(valid_set, remaining_set, remaining_gifts - remaining_set))
    '''

    '''
    remaining_gifts = gifts.difference(valid_set)
    remaining_sets = valid_sets.difference(valid_set)
    for remaining_set in remaining_sets:
        if len(remaining_gifts - set(remaining_set)):
            print('{} {} {}'.format(valid_set, remaining_set, remaining_gifts))
    '''

    #print(valid_sets)
    #print(len(valid_sets))

get_result(set([1,2,3,4,5,7,8,9,10,11]))

with open('./input.txt') as f:
    lines = f.readlines()
    input = [int(element) for element in lines]
    get_result(input)

'''
def get_valid_states(gifts):
    results  = set()
    total_weight = 0
    for gift in gifts:
        total_weight += gift
    
    target_weight = int(total_weight / 3)

    print('total {} target weight {}'.format(total_weight, target_weight))

    kill = 0
    for candidate in itertools.combinations(gifts, 5):
        print(candidate)
        #if kill == 10000:
        #    break
        
        kill += 1
        #candidate = list(candidate)
        #candidate.reverse()
        #print(candidate)
        #for f in get_sublists(list(candidate), target_weight):
        #   inner_set.add(f)

        count,qe = get_sublists(list(candidate), target_weight)
        if count and qe:
            results.add((count,qe))
           #print('{} {}'.format(count,qe))
    
    results = list(results)
    results.sort()
    print(results)

# Start at the end of the list and see if the items add up to the target weight

# Iterate through the list, return the index at which the 

def get_sublists(gifts, target_weight):
    sublist_1 = get_sublist(gifts, target_weight)
    if sublist_1:
        sublist_2 = get_sublist(gifts, target_weight)
        if sublist_2:
            sublist_3 = get_sublist(gifts, target_weight)
            if sublist_3:
                # An arrangement exists. Return the number of items in the first group and the QE state.
                count = 0
                qe = 1
                for element in sublist_1:
                    count += 1
                    qe *= element
                print('state {} {}'.format(count, qe))    
                return (count, qe)
                #return sublists_to_string(sublist_1,sublist_2,sublist_3)
                #s[key] = value
                #return ','.join([subset_to_string(sublist_1.sort()), subset_to_string(sublist_2.sort()),subset_to_string(sublist_3.sort())])
            #print(set(sublist_1), set(sublist_2), set(sublist_3))
            #a = frozenset()
            # return (frozenset(sublist_1), frozenset(sublist_2), frozenset(sublist_3))
    return (None,None)

def sublists_to_string(s1,s2,s3):
    key = '|'.join([sublist_to_string(s1),sublist_to_string(s2), sublist_to_string(s3)])
    #print(key)
    return(key, (s1,s2,s3))
    #if subset:
    #    return '[' + ','.join([str(item) for item in subset]) + ']'
    
    return ''

def sublist_to_string(sublist):
    return ''.join([str(element) for element in sublist])

def get_sublist(gifts, target_weight):
    sublist = []
    sublist_weight = 0
    while sublist_weight < target_weight:
        element = gifts.pop()
        sublist_weight += element
        sublist.append(element)
    
    if sublist_weight == target_weight:
        sublist.sort()
        return sublist
    
    return []



test_input = [1,2,3,4,5,7,8,9,10,11]

get_valid_states(test_input)

with open('./input.txt') as f:
    lines = f.readlines()
    input = [int(element) for element in lines]
    get_valid_states(input)
'''


