import time
import sys


def bar(percent):
    count = 40
    filled_count = int(percent * count)
    print '\r', 'Some text:', '[' + filled_count * '#' + (count - filled_count) * ' ' + ']', int(percent * 100), '%',
    sys.stdout.flush()

print
for i in range(10):
    percent = (i + 1) / (10 * 1.0)
    bar(percent)
    time.sleep(.1)
