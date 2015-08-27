#!/usr/bin/python
import random;
def judge():
    for i in range(10):
        x = random.randint(1,1000);
        y = random.randint(1,1000);
        print('time: %d----> x:%d\t y:%d'%(i,x,y));
        if x > y:
            print(' %d is bigger than %d'%(x,y));
        else:
            print(' %d is smaller than %d'%(x,y));
author='Yu Dong Wei';
