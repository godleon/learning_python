import os

print(os.getcwd())
#print(dir(os))
#print(help(os))

import shutil
shutil.copyfile('README.md', 'README.md.cp')


import glob
print(glob.glob('**/*.py', recursive=True))


import sys
print(sys.argv)

sys.stderr.write('Warning, log file not found starting a new one\n')


import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
print('tea for too'.replace('too', 'two'))


import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))


import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))


import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))


from datetime import date
now = date.today()
print(now)
birthday = date(1981, 12, 8)
age = now - birthday
print(age.days / 365)


import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
print(s)
t = zlib.compress(s)
print(len(t))
print(t)
print(zlib.decompress(t))
print(zlib.crc32(s))


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()


import unittest

class estStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 40]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()