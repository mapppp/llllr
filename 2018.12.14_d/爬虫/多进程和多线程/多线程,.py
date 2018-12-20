import threading
import time
import random
import os


# 1.用 threading 模块创建多线程
# 把一个函数传入并创建 Thread 实例，然后调用 start 方法开始执行；


def thread_run(urls):
    print('Current %s is running...' % threading.current_thread().name)
    for url in urls:
        print('%s ---->>> %s' % (threading.current_thread().name, url))
        time.sleep(random.random())
    print('%s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    print('%s is running...' % threading.current_thread().name)
    t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url_1', 'url_2', 'url_3'],))
    t2 = threading.Thread(target=thread_run, name='Thread_2', args=(['url_4', 'url_5', 'url_6'],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('%s ended.' % threading.current_thread().name)


# 直接从 threading.Thread 继承并创建线程类，然后重写__init__方法和 run 方法。
class MyThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print('Current %s is running...' % threading.current_thread().name)
        for url in self.urls:
            print('%s ---->>> %s' % (threading.current_thread().name, url))
            time.sleep(random.random())
        print('%s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    print('%s is running...' % threading.current_thread().name)
    t1 = MyThread(name='Thread_1', urls=['url_1', 'url_2', 'url_3'])
    t2 = MyThread(name='Thread_2', urls=['url_4', 'url_5', 'url_6'])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('%s ended.' % threading.current_thread().name)

'''如果多个线程共同对某个数据修改，则可能出现不可预料的结果，
使用 Thread 对象的 Lock 和 RLock 可以实现简单的线程同步，
这两个对象都有 acquire 方法和 release 方法，'''
# 每次只允许一个线程操作的数据，将其操作放到 acquire 和 release 方法之间。
'''对于 Lock 对象而言，如果一个线程连续两次进行 acquire 操作，
那么由于第一次 acquire 之后没有 release，第二次 acquire 将挂起线程。
这会导致 Lock 对象永远不会 release，使得线程死锁。
RLock 对象允许一个线程多次对其进行 acquire 操作，因为在其内部通过一个 counter 变量维护着线程 acquire 的次数。
而且每一次的 acquire 操作必须有一个 release 操作与之对应，
在所有的 release 操作完成之后，别的线程才能申请该 RLock 对象。'''

mylock = threading.RLock()
num = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print('%s locked, Number: %d' % (threading.current_thread().name, num))
            if num >= 4:
                mylock.release()
                print('%s released, Number: %d' % (threading.current_thread().name, num))
                break
            num += 1
            print('%s released, Number: %d' % (threading.current_thread().name, num))
            mylock.release()


if __name__ == '__main__':
    thread1 = myThread('Thread_1')
    thread2 = myThread('Thread_2')
    thread1.start()
    thread2.start()

'''3.全局解释器锁（GIL）
在 Python 的原始解释器 CPython 中存在着 GIL（Global Interpreter Lock，全局解释器锁），
因此在解释执行 Python 代码时，会产生互斥锁来限制线程对共享资源的访问，
直到解释器遇到 I/O 操作或者操作次数达到一定数目时才会释放 GIL。
由于全局解释器锁的存在，在进行多线程操作的时候，不能调用多个 CPU 内核，只能利用一个内核，
所以在进行 CPU 密集型操作的时候，不推荐使用多线程，更加倾向于多进程。
那么多线程适合什么样的应用场景呢？对于 IO 密集型操作，多线程可以明显提高效率，
例如 Python 爬虫的开发，绝大多数时间爬虫是在等待 socket 返回数据，网络 IO 的操作延时比 CPU 大得多。'''