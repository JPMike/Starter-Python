import urllib.request
import urllib.parse
import urllib.error
import tempfile
import shutil
import socket

timeout = 10
socket.setdefaulttimeout(timeout)

proxy_handler = urllib.request.ProxyHandler({})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

test_url = "http://python.org"
fake_url = "http://www.pretend_server.org"
not_found_url = "http://www.python.org/fish.html"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 " \
             "Safari/537.36"


def urlopen_test1():
    with urllib.request.urlopen(test_url) as resp:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(resp, tmp_file)

    with open(tmp_file.name) as html:
        pass


def urlopen_test2():
    req = urllib.request.Request(test_url)
    with urllib.request.urlopen(req) as resp:
        page = resp.read()


def urlopen_test3():
    values = {
        "key": "val"
    }
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(test_url, data)
    with urllib.request.urlopen(req) as resp:
        page = resp.read()


def urlopen_test4():
    values = {
        "key": "val"
    }
    url_values = urllib.parse.urlencode(values)
    url = test_url + '?' + url_values
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        page = resp.read()


def urlopen_test5():
    values = {
        "key": "val"
    }
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    headers = {
        "User-Agent": user_agent
    }
    req = urllib.request.Request(test_url, data, headers)
    with urllib.request.urlopen(req) as resp:
        page = resp.read()


def url_error_test():
    req = urllib.request.Request(fake_url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)


def http_error_test():
    req = urllib.request.Request(not_found_url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())


if __name__ == '__main__':
    # urlopen_test1()
    # urlopen_test2()
    # urlopen_test3()
    # urlopen_test4()
    # urlopen_test5()
    # url_error_test()
    # http_error_test()
    pass
