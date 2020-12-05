# Get the value for any row/column on the simple 'increment by 1' paper
# Use this to find out how many times to apply the 'get next value' operation
def get_value(row, col):
    # Get the value at the row in the first column
    value = 1 
    for i in range(1, row):
        value = value + i
        i = i + 1
    
    # Use the value in the first colmn to get the value in the nth column
    col_increment = row + 1
    for j in range(1, col):
        value = value + col_increment
        col_increment += 1

    return value

def apply_operation(number_of_times):
    code_value = 20151125
    for i in range(1, number_of_times):
        code_value *= 252533
        code_value = code_value % 33554393
    return code_value

print('Problem 1 : {}'.format(apply_operation(get_value(2981,3075))))
