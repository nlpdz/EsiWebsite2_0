from urllib2 import urlopen,Request
url = 'http://haoyun4.kagirl.cn/kphoto/submit_like.php?bookid=dD2nhG888UxJYasaj9p0eW_5flcPGLMCPVmwpJ5UxaM&wxid=haoyun&randnum=0.23495112137155028'
import random
import threading
endip = random.randint(10, 200)
ip = '61.103.192.'+str(endip)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'X-Forwarded-For': ip,
}


def click(c):
    for i in xrange(c):
        req = Request(url, headers=headers)
        urlopen(req, timeout=5)

threads = []
for i in xrange(10):
    threads.append(threading.Thread(target=click,args=(100,)))

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
