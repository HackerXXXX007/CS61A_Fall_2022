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
    "*** YOUR CODE HERE ***"
    result_total=1                                   #Prepare two variables for receiving data after two for loops
    result_part=1                                    
    if(k==0):                                        #if k==0  return 1
        return 1
    for i in range(1, n + 1):                        #factorial of n
        result_total *= i
    for j in range(1, n-k + 1):                      #factorial of n-k
        result_part *= j
    return (result_total)//(result_part)

# The code from openAI:
#    def falling(n, k):
#     """Compute the falling factorial of n to depth k."""
#     result = 1
#     for i in range(n, n - k, -1):
#         result *= i
#     return result


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
    digits=[]                                         #Define an array to accept each bit of the split
    sum=0
    while y>0:                                        #The resulting numbers are placed in reverse order
        digit=y%10
        digits.insert(0,digit)
        y=y//10
    for digit in digits:
        sum+=digit
    return sum

# # Method 2:                                         #Convert a number to a string, convert it back to a single number and sum it
# # def sum_digits(y):
#     sum=0
#     digits = [int(digit) for digit in str(y)]
#     for digit in digits:
#         sum += digit
#     return sum


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
    if(n<88):
        return False
    digits=[]                                                           #Define an array to accept each bit of the split
    while n>0:                                                          #The resulting numbers are placed in reverse order
        digit=n%10
        digits.insert(0,digit)
        n=n//10
    length = len(digits)
    for i in range(0,length-1):                                         #Determine whether there are two adjacent numbers 8
        if((digits[i]==digits[i+1]) and (digits[i]==8)):
            return True
    return False