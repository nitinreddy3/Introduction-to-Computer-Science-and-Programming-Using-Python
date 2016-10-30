def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    length = len(L)

    def poly(x):
        result = 0
        for i in range(length):
            result += L[i] * pow(x, length - i - 1)
        return result
    return poly


# print(general_poly([1, 2, 3, 4])(10))
