from utils import functions as func

# Getting the information from the user
try:
    value = float(input('Please, enter the value: '))   # possible error if user enters strings
except:
    print('Wrong value entered')
    quit()

input_unit = input('Enter the input unit [C, F or K]: ').upper()
output_unit = input('Enter the desired output unit [C, F or K]: ').upper()

# Run function
print(func.convertor(value=value, param1=input_unit, param2=output_unit))
