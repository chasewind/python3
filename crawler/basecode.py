#!/usr/bin/python
#filename:base knowledge for python
'''
created at:2015-08-27
author:yudongwei
'''
import sys;
import statements;
import data;
print('good begin for python learning ......');
if __name__ =='__main__':
    print(' in main module ......');
else:
    print('sub module......');
statements.judge();
print('moduleName:%s,and module author:%s'%(statements.__name__,statements.author));
sysinfo = dir(sys);
print('sys module info are below:');
for info in sysinfo:
    print(info,end=',');
print('*'*30);
data.dataStruct();
