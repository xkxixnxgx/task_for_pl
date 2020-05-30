#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    list_620 = range(6, 21)
    if N % 2 == 0:
        if N in list_620:
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('Weird')