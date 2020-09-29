def func_m(x):
    """Вычисляет значение функции.

    >>> func_m(0)
    1.0

    >>> func_m(1)
    5.0

    """
    return float(x**4+4**x)

import doctest
doctest.testmod()


