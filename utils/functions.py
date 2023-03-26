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
                return f'{1.8 * value + 32} F'
            elif param2 == 'K':
                return f'{value + 273.15} K'
            else:
                return f'{value} C'
        elif param1 == 'F':
            if param2 == 'C':
                return f'{0.55 * (value - 32)} C'
            elif param2 == 'K':
                return f'{(0.55 * (value - 32)) + 273.15} K'
            else:
                return f'{value} F'
        elif param1 == 'K':
            if param2 == 'C':
                return f'{value - 273.15} C'
            elif param2 == 'F':
                return f'{1.8 * (value - 273.15) + 32} F'
            else:
                return f'{value} K'
