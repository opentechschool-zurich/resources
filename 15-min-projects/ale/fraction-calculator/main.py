# 1/2 + 2/3 = 7/6
#
#
# 1*3 / 2*3 + 2+2 / 3*2 


# 1/3 + 1/3 = 6/9

def division(a_1, a_2, b_1, b_2):
    c_1 = a_1 * b_2 + a_2 * b_1
    c_2 = a_2 * b_2
    for i in range(2, min(c_1, c_2) // 2 + 1):
        if c_1 % i == 0 and c_2 % i == 0:
            c_1 = c_1 // i
            c_2 = c_2 // i
    return c_1, c_2


c_1, c_2 = division(1,2, 2,3)
print(c_1, c_2)
c_1, c_2 = division(1,3, 1,3)
print(c_1, c_2)
