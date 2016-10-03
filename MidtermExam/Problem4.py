def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    result = 0
    if num == 1:
        return 0
    while base ** result - num < 0:
        result += 1
    if base ** result - num < num - base ** (result - 1):
        return result
    else:
        return result - 1 
# print(closest_power(3,12))
# print(closest_power(4,12))
# print(closest_power(4,1))