import urllib.request
import urllib.parse
import http.cookiejar
import html.parser
import codecs
import re
def getHtml(url):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),('Cookie','4564564564564564565646540')]
    urllib.request.install_opener(opener)
    html_bytes=urllib.request.urlopen(url).read()
    html_string = html_bytes.decode('utf-8')
    return html_string
html = getHtml("http://zst.aicai.com/ssq/openInfo/")
'''
#http://blog.csdn.net/zm2714/article/details/8012474
f =codecs.open('a.html','w','utf-8')
f.write(html)
f.close()
'''
#print(html)
print ('-'*30)
match = re.match(r'(.*)<html(.*)>(.*?)html>(.*)',html,re.M|re.I)
if match:
    print(match.group())
print ('-'*30)
line = "Cats are smarter than dogs"
match = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if match:
    print(match.group())
