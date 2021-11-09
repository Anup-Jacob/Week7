# ---------------------------------

# File          : Experiment.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 09/11/2021
# Modified Date : 09/11/2021
# Description   : Experiment on Code Inspection
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

'''Static Type Checking example '''

def factorial(num):
    '''Factorial is where you have factors of a number
    3! == 3x2x1 == 6
    2! == 2x1 == 2
    1! == 1x1 == 1
    0! == 1 (defined)
    must be real number
    '''
    if num < 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num-1)



if __name__ == '''__main__''':
    print(factorial(3))
    #print(factorial(3.3))
    #print(factorial("a"))