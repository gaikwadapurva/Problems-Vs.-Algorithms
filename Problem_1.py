def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None
    
    if (number == 0 or number == 1):
        return number
    
    left = 0
    right = number
    
    while left <= right:
        mid = (left + right) // 2
        result = mid * mid

        if result <= number:
            left = mid + 1
        
        else:
            right = mid - 1
        
    return left - 1


print ("Pass" if  (-1 == sqrt(4)) else "Fail")
print ("Pass" if  (None == sqrt(-10)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (17 == sqrt(300)) else "Fail")