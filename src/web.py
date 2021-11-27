import requests


def fun1():
    url = "https://www.baidu.com"
    res = requests.post(url)
    print(res.headers)
