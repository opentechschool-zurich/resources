# Write a function to flatten the nesting in an arbitrary list of values.
# [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []] should become
# [1, 2, 3, 4, 5, 6, 7, 8]

sample_input = [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]
expected_output = [1, 2, 3, 4, 5, 6, 7, 8]

def flatten(input_list):
    result = []
    for item in input_list:
        if type(item) == list:
            for sub_item in flatten(item):
                result.append(sub_item)
        else:
            result.append(item)    
        # print(item)
    return result

print(flatten(sample_input))
