#!/usr/bin/python
#encoding utf-8
'''
urllib.request代替urllib2
created at:2015-08-27
author:yudongwei
'''
import  urllib.request;

file = urllib.request.urlopen('http://www.baidu.com');
#print(file.read());
req = urllib.request.Request('http://www.baidu.com');

file2 = urllib.request.urlopen(req);
#print(file2.read());
data = {'q':'中文','go':'提交'};
data = urllib.parse.urlencode(data);
print(data);

file3 = urllib.request.urlopen("http://cn.bing.com/search?q=python");
#print(file3.read());


'''
[Errno 11001] getaddrinfo failed
'''
try:
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)';
    headers = { 'User-Agent' : user_agent };
    req = urllib.request.Request("http://cn.bingbing.com/search?q=python",None,headers);
    file4 = urllib.request.urlopen(req);
    print(file4.read());
except urllib.request.URLError as e:
    if hasattr(e, 'reason'):
        print('error reason:',e.reason);
    if hasattr(e, 'code'):
        print('error code:',e.code);



















