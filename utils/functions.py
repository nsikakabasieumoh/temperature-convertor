def convertor(value:float, param1, param2) -> float:
    """ Get input from the user

    :value: the value to be converted
    :param1: the input unit
    :param2: the output unit
    :return: returns the output value as float
    """

    if param1 not in ['C', 'F', 'K'] or param2 not in ['C', 'F', 'K']:
        return None
    else:
        return 0.00
