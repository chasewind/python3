import os
import traceback
import sys
from test.fork_wait import _thread
fs = dir(__builtins__)
for item in fs:
    print(item)
try:
    aNum = int('123456A')
except ValueError as e:
    print(e)
#   os._exit(0)
print('-'*30)
try:
    aNum = int('12345A')
except (ValueError,Exception ) :
    print(ValueError,':',Exception)
print('-'*30)
try:
    aNum = int('12345A')
except:
    f = open('log.txt', 'a')
    traceback.print_exc(file=f)
    traceback.print_exc()
print('-'*30)
try:
    aNum = int('12345A')
except:
    info = sys.exc_info()
    print(info)
    print(len(info))
    print(info[0])
    print(info[1])
    print(info[2])
print('-'*30)
