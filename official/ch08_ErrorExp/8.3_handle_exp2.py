#!/usr/bin/env python3

import os, sys
from os.path import dirname

file_path = dirname(os.path.abspath(__file__)) + '/workfile'

try:
    with open(file_path, 'r+') as f:
        s = f.readline()
        i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
    