#!/usr/bin/python
#encoding utf-8
'''
urllib.request代替urllib2
created at:2015-08-27
author:yudongwei
'''
import  urllib.request;

file = urllib.request.urlopen('http://www.baidu.com');
print(file.read());
req = urllib.request.Request('http://www.baidu.com');

file2 = urllib.request.urlopen(req);
print(file2.read());
data = {'q':'中文','go':'提交'};
data = urllib.parse.urlencode(data);
print(data);