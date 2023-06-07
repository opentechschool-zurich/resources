def decimal_to_roman(decimal):
    roman_signs = 'IVXLCDM'
    roman = '' # the roman number, built in reverse order
    step = 0
    while decimal > 0:
        if step == len(roman_signs) - 1: # add as many Ms as needed
            roman += decimal * roman_signs[-1]
            break

        remainder = decimal % 10

        if remainder < 4: # 1 2 3
            roman += remainder * roman_signs[step]
        elif remainder == 4:
            roman += roman_signs[step + 1] + roman_signs[step] 
        elif remainder < 9: # 5 6 7 8
            roman += roman_signs[step] * (remainder - 5) + roman_signs[step + 1]
        elif remainder == 9:
            roman += roman_signs[step + 2] + roman_signs[step]

        decimal //= 10
        step += 2
    return roman[::-1]

assert(decimal_to_roman(1) == 'I')
assert(decimal_to_roman(2) == 'II')
assert(decimal_to_roman(3) == 'III')
assert(decimal_to_roman(4) == 'IV')
assert(decimal_to_roman(5) == 'V')
assert(decimal_to_roman(6) == 'VI')
assert(decimal_to_roman(7) == 'VII')
assert(decimal_to_roman(8) == 'VIII')
assert(decimal_to_roman(9) == 'IX')
assert(decimal_to_roman(10) == 'X')
assert(decimal_to_roman(11) == 'XI')
assert(decimal_to_roman(12) == 'XII')
assert(decimal_to_roman(13) == 'XIII')
assert(decimal_to_roman(14) == 'XIV')
assert(decimal_to_roman(15) == 'XV')
assert(decimal_to_roman(16) == 'XVI')
assert(decimal_to_roman(17) == 'XVII')
assert(decimal_to_roman(18) == 'XVIII')
assert(decimal_to_roman(19) == 'XIX')
assert(decimal_to_roman(20) == 'XX')
assert(decimal_to_roman(21) == 'XXI')
assert(decimal_to_roman(50) == 'L')
assert(decimal_to_roman(99) == 'XCIX')
assert(decimal_to_roman(100) == 'C')
assert(decimal_to_roman(101) == 'CI')
assert(decimal_to_roman(790) == 'DCCXC')
assert(decimal_to_roman(990) == 'CMXC')
assert(decimal_to_roman(1990) == 'MCMXC')
assert(decimal_to_roman(1999) == 'MCMXCIX')
assert(decimal_to_roman(9999) == 'MMMMMMMMMCMXCIX')
