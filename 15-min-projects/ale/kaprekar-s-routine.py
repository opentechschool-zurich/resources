# https://en.wikipedia.org/wiki/Kaprekar%27s_routine
#
# - pick a four digit integer number with at least two distinct digits
# - sort the digits in descedning order
# - substract the digits in ascending order
# - within seven iterations you will get to 6174
#
# for other number lengths, a cycle is generated: try to detect the cycle

def digits_descreasing(n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n = n // 10
    digits.sort(reverse=True)
    return digits

def list_to_int(digits):
    n = 0
    power_10 = 10 ** (len(digits) - 1)
    for d in digits:
        n += d * power_10
        power_10 //= 10
    return n

def next_kaprekar(n):
    digits = digits_descreasing(n)
    result = list_to_int(digits)
    digits.reverse()
    result -= list_to_int(digits)
    return result

def kaprekar(n):
    while True:
        next_n = next_kaprekar(n)
        if n == next_n:
            break
        n = next_n
    return n

def test_next_kaprekar():
    assert next_kaprekar(9981) == 8082
    assert next_kaprekar(8082) == 8532
    assert next_kaprekar(8532) == 6174
    assert next_kaprekar(6174) == 6174
    
def test_kaprekar():
    assert kaprekar(9981) == 6174


def main():
    n = 8082
    print(kaprekar(n))

if __name__ == "__main__":
    test_next_kaprekar() 
    test_kaprekar()

    main()
