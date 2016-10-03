def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    result = []
    for i in aList:
        if isinstance(i,list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
# test = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# print(flatten(test))