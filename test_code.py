# test code

import numpy as np
import datetime as dt


def mkdate(text):
    return dt.datetime.strptime(text, '%Y-%m-%d')

database = np.genfromtxt('City_Zhvi_Summary_AllHomes.csv', delimiter=',', names=True, usecols=(0, 1), dtype=None, converters={'Date': mkdate})
print database


# http://stackoverflow.com/questions/7500864/python-array-of-datetime-objects-from-numpy-ndarray
