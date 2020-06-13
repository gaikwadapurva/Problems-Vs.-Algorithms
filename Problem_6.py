def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    
    if len(ints) == 1:
        return (ints[0], ints[0])

    min = ints[0]
    max = ints[0]

    for number in ints:
        if min > number:
            min = number
        if max < number:
            max = number
    
    return (min, max)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if (None == get_min_max([])) else "Fail")
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")
print ("Pass" if ((1, 13) == get_min_max([3, 6, 1, 13, 8])) else "Fail")