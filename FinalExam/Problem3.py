trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
         '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    if len(us_num) < 2 or us_num == '10':
        result = trans[us_num]
    elif us_num[1] == '0':
        result = trans[us_num[0]] + ' ' + trans['10']
    elif us_num[0] == '1':
        result = trans['10'] + ' ' + trans[us_num[1]]
    else:
        result = trans[us_num[0]] + ' ' + trans['10'] + ' ' + trans[us_num[1]]
    return result

print(convert_to_mandarin('20'))

