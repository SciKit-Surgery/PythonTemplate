# coding=utf-8

"""Hello world demo module"""
from {{ cookiecutter.pkg_name }}.algorithms import addition, multiplication

def run_demo(input_x, input_y, multiply, verbose):
    """ Run the application """

    if multiply:
        result = multiplication.multiply_two_numbers(input_x, input_y)

    else:
        result = addition.add_two_numbers(input_x, input_y)


    if verbose:
        if multiply:
            print(f"Calculating {input_x} * {input_y}")

        else:
            print(f"Calculating {input_x} + {input_y}")

    print(f"Result is {result}")

    return result
