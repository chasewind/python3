import urllib.request
import urllib.parse
import http.cookiejar
import html.parser
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
#print(html)
print('-'*30)


'''
http://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''
#print(table)
begin = html.find('<table class="fzTab nbt">')
end = html.find('</table>')
table =html[begin:(end+len('</table>'))]
#print(table)

#print(table2)
pattern = re.compile('tr ([\s]+) onmouseout', re.IGNORECASE)
print(pattern)
re.sub(pattern, 'tr onmouseout',html)
print(html)





