#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tax = meal_cost * tax_percent/100
    tip = meal_cost * tip_percent/100
    totalCost = meal_cost + tax + tip
    return totalCost

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(round(solve(meal_cost, tip_percent, tax_percent)))