from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE = __file__


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    resoult =1
    for i in range(1,n+1):
        resoult *= term(i)
    return resoult


def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    arr=[]
    for i in range(1,n+1):                                   #Numbers from 1 to n are processed by the term function and stored in an array
        arr.append(term(i))
    arr.insert(0,start)                                      #Add the "start" as the first element of the array
    def apply_operation(arr,merger):                         #Each element in the array is processed by the merge function
            result = arr[0]
            for num in arr[1:]:
                result = merger(result, num)
            return result
    return apply_operation(arr,merger)



def summation_using_accumulate(n, term):
    """Returns the sum: term(0) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    #"*** YOUR CODE HERE ***"                                #fuck
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    #"*** YOUR CODE HERE ***"
    return accumulate(mul, 1, n, term)

###Exam Practice
#1.Fall 2019 MT1 Q3: You Again [Higher Order Functions]
def again(f):
    """Return the smallest non-negative integer n such that f(n) == f(m) for some m < n.
    >>> again(parabola) # parabola(4) == parabola(5)
    5
    >>> again(vee) # vee(1) == vee(3)
    3
    """
    n=1
    while True:
        m=0
        while m<n:
            if f(n) == f(m):
                return n
            m=m+1
        n=n+1

#Test:
a=again(parabola)
b=again(vee)
print(a,b)







#2.Spring 2021 MT1 Q4: Domain on the Range [Higher Order Functions]
#(a) (4.0 points) restrict_domain
from math import sqrt,inf
def restrict_domain(f, low_d, high_d):
    """Returns a function that restricts the domain of F,
    a function that takes a single argument x.
    If x is not between LOW_D and HIGH_D (inclusive),
    it returns -Infinity, but otherwise returns F(x).
    >>> from math import sqrt
    >>> f = restrict_domain(sqrt, 1, 100)
    >>> f(25)
    5.0
    >>> f(-25)
    -inf
    >>> f(125)
    -inf
    >>> f(1)
    1.0
    >>> f(100)
    10.0
    """
    def wrapper_method_name(X):
    # (a)
        if low_d<=X<=high_d:
        # (b)
            return f(X)
            # (c)
        else:
            return -inf
        # (d)
    return wrapper_method_name
#Test: 
a=restrict_domain(sqrt, 1, 100)
print(a(25))
print(a(-25))
print(a(125))
print(a(1))
print(a(100))

#(b) (5.0 points) restrict_range
cube = lambda x: x * x * x
def restrict_range(f, low_r, high_r):
    """Returns a function that restricts the range of F, a function
    that takes a single argument X. If the return value of F(X)
    is not between LOW_R and HIGH_R (inclusive), it returns -Infinity,
    but otherwise returns F(X).
    >>> cube = lambda x: x * x * x
    >>> f = restrict_range(cube, 1, 1000)
    >>> f(1)
    1
    >>> f(-5)
    -inf
    >>> f(5)
    125
    >>> f(10)
    1000
    >>> f(11)
    -inf
    """
    def wrapper_method_name(X):  
    # (a)
        resoult = f(X)
        # (b)
        if low_r <= resoult <= high_r:
        # (c)
            return resoult
            # (d)
        return float('-inf')
        # (e)
    return wrapper_method_name
#Test:
b=restrict_range(cube, 1, 1000)
print(b(1))
print(b(-5))
print(b(5))
print(b(10))
print(b(11))

#(c) (1.0 points) restrict_both
diva = lambda x: (10000 // x) * 9
def restrict_both(f, low_d, high_d, low_r, high_r):
    """
    Returns a version of F with a domain restricted to (LOW_D, HIGH_D)
    and a range restricted to (LOW_R, HIGH_R).
    >>> diva = lambda x: (10000 // x) * 9
    >>> f = enforce_both(diva, 1, 1000, 100, 999)
    >>> f(0)
    -inf
    >>> f(10000)
    -inf
    >>> f(200)
    450
    >>> f(100)
    900
    >>> f(1000)
    -inf
    """
    def wrapper_method_name(X):
        if X==0:
            return float('-inf')
        else:
            result=f(X)
            if   low_r <= result <= high_r and low_d<=X<=high_d:
                 return result
            else:
                  return float('-inf')
    return wrapper_method_name
#Test
c=restrict_both(diva, 1, 1000, 100, 999)
print(c(0))
print(c(10000))
print(c(200))
print(c(100))
print(c(1000))



#3.Fall 2021 MT1 Q1b: tik [Functions and Expressions]
def tik(tok):
    """Returns a function that takes gram and prints tok and gram on a line.
    >>> tik(5)(6)
    5 6
    """
    def insta(gram):
        print(tok,gram) # The implementation of this function has been omitted.
    return insta
#Test:
tik(5)(6)