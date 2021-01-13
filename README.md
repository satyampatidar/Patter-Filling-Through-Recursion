# Patter-Filling-Through-Recursion
Recursive function which goes through a pre-filled matrix which has many levels of inner matrices with varying depths, that have been initialized with three alphabets each, in a sequence.
The program needs to check whether the given matrix follows the rule or not, if it does not follow, recursion should terminate the check and return the list object that
violates the rule.

• The rules to be followed are the following:
1. Assume ‘a’ to ‘k’, if the number of chars encountered exceeds ‘k’, it should wrap
around again from ‘a’. Note: The string used, needs to be configurable manually.
2. You are free to follow my implementation discussed in the Session 13 or your own as
the starting point, but it needs to use inner functions with recursion.
3. If there are no entries in a matrix, or less or more number of elements in any list or
items not following the order prescribed, need to be flashed as an error and terminate.
4. Returns a tuple, with (Boolean result, matrix as a list object).
5. If the result is True, the entire Matrix object is passed. If the result is False, the first
matrix that has error is passed back.
