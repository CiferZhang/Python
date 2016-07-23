# encoding:utf8
""" Simulate a user login to Sina Weibo with cookie.
You can use this method to visit any page that requires login.
"""
import urllib.request
import re


cookie = 'your-cookie'  # get your cookie from Chrome or Firefox
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
    'cookie': your cookie
}


def visit():
    url = 'http://weibo.com'
    req = urllib.request.Request(url, headers=headers)
    text = urllib.request.urlopen(req).read()
    text = text.decode('utf8')
    # print the title, check if you login to weibo sucessfully
    pat_title = re.compile('<title>(.+?)</title>')
    r = pat_title.search(text)
    if r:
        print (r.group(1))


if __name__ == '__main__':
    visit()