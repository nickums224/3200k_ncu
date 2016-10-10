

def sa_cuboid (l, b, h):
    """returns the surface area of cuboid

    >>> sa_cuboid(1, 1, 1)
    6

    >>> sa_cuboid(2, 2, 2)
    24
    
    """
    
    return 2 * (l*b + b*h + h*1)


def super_state_adder(x, y):
    """returns sum of both are int
    >>> super_safe_adder(2, 3)
    5

    >>> super_safe_adder('tacos', 3)
    0

    """

    if isinstance(x, int) and isinstance (y, int) :
        return x + y
    else:
        return 0
        

            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
