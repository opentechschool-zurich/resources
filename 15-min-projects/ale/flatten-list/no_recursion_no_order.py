# Write a function to flatten the nesting in an arbitrary list of values.
# [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []] should become
# [1, 2, 3, 4, 5, 6, 7, 8]

sample_input = [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]
expected_output = [1, 2, 3, 4, 5, 6, 7, 8]

def flatten_no_recursion(input_list):
    result = []
    process_list = input_list
    while len(process_list) != 0:
        item = process_list.pop(0)
        if type(item) == list:
            for sub_item in item:
                process_list.append(sub_item)
        else:
            result.append(item)

    return result

print(flatten_no_recursion(sample_input))
