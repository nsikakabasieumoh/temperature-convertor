def convertor(value:float, param1, param2) -> float:
    """ Get input from the user

    :value: the value to be converted
    :param1: the input unit
    :param2: the output unit
    :return: returns the output value as float
    """

    unit_list = ['C', 'F', 'K']

    if param1 not in unit_list or param2 not in unit_list:
        return None
    else:
        if param1 == 'C':
            if param2 == 'F':
                return 1.8 * value + 32
            elif param2 == 'K':
                return value + 273.15
            else:
                return value
