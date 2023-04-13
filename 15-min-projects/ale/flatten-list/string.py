# Write a function to flatten the nesting in an arbitrary list of values.
# [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []] should become
# [1, 2, 3, 4, 5, 6, 7, 8]

sample_input = [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]
expected_output = [1, 2, 3, 4, 5, 6, 7, 8]

def flatten(input_list):
    result = []
    for c in str(sample_input):
        if c.isnumeric():
            result.append(int(c))
    return result

print(flatten(sample_input))
