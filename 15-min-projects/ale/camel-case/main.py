def dash_to_camel_case(text):
    result = ''
    nextUpper = False
    for c in text:
        if c == '_':
            nextUpper = True
        else:
            if nextUpper:
                result += c.upper()
                nextUpper = False
            else:
                result += c
    return result


print(dash_to_camel_case('sum_of_digits'))
