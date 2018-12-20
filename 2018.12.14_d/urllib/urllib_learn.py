from urllib import request
from urllib import parse
import urllib
print('Python3Urllib库的基本使用')
'''一、什么是Urllib
Urllib库是Python自带的一个http请求库，包含以下几个模块：
urllib.request　　　 请求模块
urllib.error　　   　异常处理模块
urllib.parse　　  　 url解析模块
urllib.robotparser 　robots.txt解析模块
其中前三个模块比较常用，第四个仅作了解。
'''
'''二、Urllib方法介绍
将结合Urllib的官方文档进行说明。
首先是urllib.request模块：
urllib.request.urlopen(url, data=None, [timeout, ] *, cafile=None, capath=None, cadefault=False, context=None)'''
# 示例代码1：
print('import urllib.request')
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
'''这里用到了方法的第一个参数，即为URL地址，这种请求方式为GET请求，因为没有附加任何的参数。read()
方法从返回中读取响应体的内容，读取完是二进制字节流，因此需要调用decode()
方法通过utf8编码方式转换成我们所能读懂的网页代码。'''

# 示例代码2：

print('import urllib.parse,'
      'import urllib.request')
d = bytes(urllib.parse.urlencode({'name': 'zhangsan'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=d)
print(response.read().decode('utf-8'))
# res
'''{
    "args": {},
    "data": "",
    "files": {},
    "form": {
        "name": "zhangsan"
    },
    "headers": {
        "Accept-Encoding": "identity",
        "Connection": "close",
        "Content-Length": "13",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "httpbin.org",
        "User-Agent": "Python-urllib/3.7"
    },
    "json": null,
    "origin": "183.209.153.56",
    "url": "http://httpbin.org/post"
}'''
'''这里用到了第二个参数data，这次相当于一次post请求，该url是http测试网址。因为urlopen方法的data要求传入的参数形式是二进制，所以我们需要对字典进行二进制转码。

　　示例代码3：



# 设置请求的超时时间
import socket
import urllib.request

try:
    response = urllib.request.urlopen('http://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time Out')


　　这里使用了timeout参数，设置了一个极短的时间以至于不会在时间内返回。所以程序会抛出异常。通过判断异常的类型去打印异常信息是常用的手段，因此，当异常为timeout时，将打印‘Time
Out’。

　　示例代码4：



1  # response有用的方法或参数
2
import urllib.request

3
4
response = urllib.request.urlopen('http://www.python.org')
5
print(response.status)
6
print(response.getHeaders())  # 元祖列表
7
print(response.getHeader('Server'))


　　status为状态码，getHeaders()
返回响应头的信息。但是当我们想传递request
headers的时候，urlopen就无法支持了，因此这里需要一个新的方法。

urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
　　示例代码1：



1
from urllib import request, parse

2
3
url = 'http://httpbin.org/post'
4
headers = {
    5
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36',
6
'Host': 'httpbin.org'
7}
8
dict = {
    9
'name': 'zhangsan'
10}
11
12
data = bytes(parse.urlencode(dict), encoding='utf8')
13
req = request.Request(url=url, data=data, headers=headers, method=post)
14
response = request.urlopen(req)
15
print(response.read().decode('utf-8'))


　　用Request方法进行post请求并加入了请求头。

urllib.request.build_opener([handler, ...])
　　Handler是urllib中十分好用的一个工具，当我们进行IP代理访问或者爬虫过程保持对话（cookie）时，可以用相应的handler进行操作。以处理cookie的handler为例。

　　代码示例2：



1
import http.cookiejar, urllib.request

2
3
cookie = http.cookiejar.CookieJar()
4
handler = urllib.request.HttpCookieProcessor(cookie)
5
opener = urllib.request.build_opener(handler)
6
response = opener.open('http://www.baidu.com')
7
8
for item in cookie:
    9
    print(item.name, item.value)


　　通过CookieJar()
来构造一个cookie对象，然后调用urllib.request.HttpCookieProcesser()
创建一个关于cookie的handler对象，通过这个handler构造opener，然后就可以进行http请求了。返回的response包含cookie信息，这个handler就可以拿到该cookie信息并保存到cookie对象中。cookie的作用在于，如果爬虫过程中需要维持会话，那可以将cookie加入到Request中。

　　示例代码3：



1
import http.cookiejar, urllib.request

2
3
filename = 'cookie.txt'
4
cookie = http.cookiejar.MozillaCookieJar(filename)
5
handler = urllib.request.HttpCookieProcessor(cookie)
6
opener = urllib.request.build_opener(handler)
7
response = opener.open('http://www.baidu.com')
8
cookie.save(ignore_discard=True, ignore_expires=True)


　　MozillaCookieJar是CookieJar的子类，可以将cookie写入本地文件。

　　示例代码4：

1
import http.cookiejar, urllib.request

2
3
cookie = http.cookiejar.MozillaCookieJar()
4
cookie.load('cookie.txt', Ignore_discard=True, Ignore_expires=True)
5
handler = urllib.request.HttpCookieProcessor(cookie)
6
opener = urllib.request.build_opener(handler)
7
response = opener.open('http://www.baidu.com')
8
print(response.read().decode('utf-8'))


　　通过cookie对象的load()
方法可以从本地文件读取cookie内容，然后可以在request中维持会话状态。

　　其次是urllib.error模块。

urllib.error

　　示例代码1：



1
from urllib import request, error

2
3
try:
    4
    response = request.urlopen('http://bucunzai.com/index.html')
5 except error.HTTPError as e:
6
print(e.reason, e.code.e.header, sep='\n')
7 except error.URLError as e:
8
print(e.reason)
9 else:
10
print('Request Successfully')


　　通过官方文档可以看出，httperror是URLerror的子类，所以需要先捕捉子类异常。实例证明HTTPError被捕获。文档中可以看出，HTTPError有三个参数，分别是reason，code和header。通过实例可以得到code为404。下面将说明一种常见的用法，显示异常时哪一类异常的方法。

　　示例代码2：



1
from urllib import request, error

2
import socket

3
4
try:
    5
    response = request.urlopen('http://www.baidu.com', timeout=0.01)
6 except error.URLError as e:
7
if isinstance(e.reason, socket.timeout):
    8
    print('Time Out')


　　最后看一下urllib.parse中提供的常用方法。

urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
　　示例代码1：



1
from urllib.parse import urlparse

2
3
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
4
print(result)
5  # ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')


　　最后一行为输出结果。urlparse方法分析传入的url结构，并且拆分成相应的元组。scheme参数的作用是提供一个默认值，当url没有协议信息时，分析结果的scheme为默认值，如果有则默认值被覆盖。

　　示例代码2：



1
from urllib.parse import urlparse

2
3
result = urlparse('http://www.baidu.com/index.html;user#comment', allow_fragments=False)
4
print(result)
5  # ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html',params='user#comment', query='', fragment='')


　　可以看到，当fragment参数被设置为false的时候，url中的fragment会被添加到前面有数据的那一项中。如果不清楚URL各部分的含义，可参考本篇备注。

urllib.parse.urlunparse(parts)
　　进行url各部分的拼接，参数形式是一个列表类型。

　　示例代码1：



1
from urllib.parse import urlunparse

2
3
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
4
print(urlunparse(data))
5
6  # http://www.baidu.com/index.html;user?a=6#comment

urllib.parse.urljoin(base, url, allow_fragments=True)
　　示例代码1：



1
from urllib.parse import urljoin

2
3
print(urljoin('http://www.baidu.com', 'index.html'))
4
print(urljoin('http://www.baidu.com#comment', '?username="zhangsan"'))
5
print(urljoin('http://www.baidu.com', 'www.sohu.com'))
6
7  # http://www.baidu.com/index.html
8  # http://www.baidu.com?username="zhangsan"
9  # http://www.baidu.com/www.sohu.com


　　这种拼接需要注意其规则，如果第二个参数是第一个参数中没有的url组成部分，那将进行添加，否则进行覆盖。第二个print则是一种需要避免的现象，这种join方式会覆盖掉低级别的参数。这里的第三个print是一个反例，很多人认为解析是从域名开始的，实际上是从‘ // ’开始解析的，官方文档给出了很明确的解释：If
url is an
absolute
URL(that is, starting
with // or scheme://), the
url‘s
host
name and / or scheme
will
be
present in the
result。所以再次建议，官方文档是最好的学习工具。

urllib.parse.urlencode()
　　urlencode()
方法将字典转换成url的query参数形式的字符串 。

　　示例代码1：



1
from urllib.parse import urlencode

2
3
params = {
    4
'name': 'zhangsan',
5
'age': 22
6}
7
8
base_url = 'http://www.baidu.com?'
9
url = base_url + urlencode(params)
10
print(url)
11
12  # 'http://www.baidu.com?name=zhangsan&age=22's'''