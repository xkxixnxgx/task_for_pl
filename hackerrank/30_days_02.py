import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_p = meal_cost*tip_percent/100
    tax_p = meal_cost*tax_percent/100
    sum_cost = round(meal_cost + tip_p + tax_p)
    print(sum_cost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)