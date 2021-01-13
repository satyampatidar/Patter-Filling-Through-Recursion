# -*- coding: utf-8 -*-
"""
#Win Cartell
@author: Satyam Patidar

"""
# function for sequence check
def seq_check(a):
    # to check if the letters in the list
    # are properly arranged or not
    s = 'abcdefghijkab'
    if ''.join(a) in s:
        return(True)
    else:
        return(False)


# function to get the deepest list
def get_deepest(a):
    if type(a[0]) == type('s'):
        return a
    else:
        return get_deepest(a[0])

# head function for checking list
def check(a):
    if type(a[0]) == type(''):
        if len(a) == 3 and seq_check(a):
            return(True,a)
        else:
            return(False,a)
    for element in a:
        if len(element)==0:
            return(False,element)
        deepest = get_deepest(element)
        if len(deepest) == 3 and seq_check(deepest):
            pass
        else:
            return(False,deepest)
    return(True,a)

myMatrix0 = ['a', 'b', 'c']
myMatrix1 = ['a', 'b']
myMatrix2 = [ ['a', 'b', 'c'] ]
myMatrix3 = [ ['a', 'b', 'c'], ['d', 'e', 'f'] ]
myMatrix4 = [[[['a', 'b', 'c']]], ['d', 'e', 'f'] ] 
myMatrix5 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']]], 
             ['g', 'h', 'i'], ['j', 'k', 'z'] ] 
myMatrix6 = [[[['a', 'b', 'c']]], 
             [[['d', 'z', 'f']]], 
             ['g', 'h', 'i'], ['j', 'k', 'a'] ]
myMatrix7 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']]], 
             ['g', 'z', 'i'], ['j', 'k', 'a'] ] 
myMatrix8 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']], ['g', 'h', 'i']], 
             ['j', 'k', 'a'], ['b', 'c', 'd']]
myMatrix9 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']], ['g', 'h', 'i']], 
             ['j', 'k', 'a'], ['b', 'c', 'd'],
             []]
myMatrix10 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']], ['g', 'h', 'i']], 
             ['j', 'k', 'a'], ['b', 'c', 'd'],
             ['e', 'g', 'h', 'i']]
myMatrix11 = [[[['a', 'b', 'c']]], 
             [[['d', 'e', 'f']], [[[[[[[[['g', 'h', 'i']]]]]]]]],
             ['j', 'k', 'a']], 
             ['b', 'c', 'd'], ['e', 'f', 'g'],
             ['h', 'i', 'j']]

temp=0    
while(temp<12):
    em='myMatrix'
    em += str(temp)   
    bool_val,array1 = check(eval(em))
    print('The result of chcking the matrix: {}'.format(bool_val))
    print('The returned matrix is: {} \n'.format(array1))
    temp += 1  
