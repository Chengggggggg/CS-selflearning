def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE *** -- version 1"
    from operator import mul
    from functools import reduce
    while k == 0:
        return print(1)
    
    return reduce(mul, range(n, n-k, -1))
    
    # result, i = 1, 0
    # while True:
    #     result = result * n
    #     n -= 1
    #     i += 1
    #     if k == 0:
    #         return print(1)
    #     if i == k:
    #         return print(result)
    #

    # result, i = 1, 1
    # while i <= k:
    #     result = result * n
    #     n -= 1
    #     i += 1
    # return print(result)







         
         
   



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    result = 0
    while y >= 10:
        summ, y = y % 10, y // 10
        result += summ
    return result + y

    "better version" "thinking about stop at y == 0"
    # ans = 0
    # while y:
    #     ans += y % 10
    #     y //= 10
    # return ans
        
        
        



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n:
        if n % 100 == 88:
            count += 1
        n //= 10
    return bool(count)




