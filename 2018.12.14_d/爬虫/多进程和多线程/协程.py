from gevent import monkey
from gevent.pool import Pool
import gevent
import urllib
from urllib import request
monkey.patch_all()
'''协程（coroutine），又称微线程，纤程，是一种用户级的轻量级线程。
协程拥有自己的寄存器上下文和栈。
协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈。
因此协程能保留上一次调用时的状态，每次过程重入时，就相当于进入上一次调用的状态。'''
# 在并发编程中，协程与线程类似，每个协程表示一个执行单元，有自己的本地数据，与其他协程共享全局数据和其他资源。
'''
协程需要用户自己来编写调度逻辑，对于 CPU 来说，协程其实是单线程，所以 CPU 不用去考虑怎么调度、切换上下文，这就省去了 CPU 的切换开销，所以协程在一定程度上又好于多线程。
实现协程
Python 通过 yield 提供了对协程的基本支持，但是不完全，而使用第三方 gevent 库是更好的选择，gevent 提供了比较完善的协程支持。
gevent 是一个基于协程的 Python 网络函数库，使用 greenlet 在 libev 事件循环顶部提供了一个有高级别并发性的 API。
主要特性有以下几点：
基于 libev 的快速事件循环，Linux 上是 epoll 机制。
基于 greenlet 的轻量级执行单元。
API 复用了 Python 标准库里的内容。
支持 SSL 的协作式 sockets。
可通过线程池或 c-ares 实现 DNS 查询。
通过 monkey patching 功能使得第三方模块变成协作式。
gevent 对协程的支持，本质上是 greenlet 在实现切换工作。
greenlet 工作流程如下：
假如进行访问网络的 IO 操作时，出现阻塞，greenlet 就显式切换到另一段没有被阻塞的代码段执行，直到原先的阻塞状况消失以后，再自动切换回原来的代码段继续处理。
因此，greenlet 是一种合理安排的串行方式。
由于 IO 操作非常耗时，经常使程序处于等待状态，有了 gevent 为我们自动切换协程，就保证总有 greenlet 在运行，而不是等待 IO，
这就是协程一般比多线程效率高的原因。
由于切换是在 IO 操作时自动完成，所以 gevent 需要修改 Python 自带的一些标准库，将一些常见的阻塞，如 socket、select 等地方实现协程跳转，
这一过程在启动时通过 monkey patch 完成。下面通过一个的例子来演示 gevent 的使用流程，代码如下：
'''


def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        print('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)

# 以上程序主要用了 gevent 中的 spawn 方法和 joinall 方法。
# spawn 方法可以看做是用来形成协程，joinall 方法就是添加这些协程任务，并且启动运行。
# 从运行结果来看，3个网络操作是并发执行的，而且结束顺序不同，但其实只有一个线程。

'''gevent 中还提供了对池的支持。
当拥有动态数量的 greenlet 需要进行并发管理（限制并发数）时，
就可以使用池，
这在处理大量的网络和 IO 操作时是非常需要的。
接下来使用 gevent 中 pool 对象，对上面的例子进行改写，程序如下：'''

print('gevent 中还提供了对池的支持')


def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        print('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print(e)
    return 'url:%s --->finish' % url


if __name__ == '__main__':
    pool = Pool(2)
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    results = pool.map(run_task, urls)
    print(results)
# Pool 对象确实对协程的并发数量进行了管理，先访问了前两个网址，当其中一个任务完成时，才会执行第三个。
