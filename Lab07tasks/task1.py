import argparse
from math import exp

def create_lambda_with_globals(s):
    return eval(s)

parser = argparse.ArgumentParser()

help_f= "The Syntax is  lambda x: f(x), where f(x) is the function in python language"
help_x="x coordinate for start point"
help_y="y coordinate for start point"
help_step="how many steps method should preform - default 3"
help_prec="how precise result should be"
parser.add_argument("-f",dest="f", type=create_lambda_with_globals, help=help_f, required=True)
parser.add_argument("-x", type=float, help=help_x, required=True)
parser.add_argument("-y", type=float, help=help_y, required=True)
parser.add_argument("-step", type=float, help=help_step)
parser.add_argument("-precision", type=float, help=help_prec)
params = parser.parse_args()
print(params.x)
print(params.y)
print(params.step if params.step is not None else "empty")
print(params.precision if params.precision is not None else "empty")
print("labda result: ",params.f(2))  # run the lambda with an input of 2
