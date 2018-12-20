import os
from multiprocessing import Process
import time
import random
from multiprocessing import Pool

# 多进程、多线程、协程和分布式进程
# 多进程实现：
# os 模块中的 fork 方法，适用于 Unix/Linux 操作系统。
# multiprocessing 模块，跨平台的实现。
'''
1.使用 os 模块中的 fork 方式实现多进程
fork 方法来自于 Unix/Linux 操作系统中提供的一个 fork 系统调用，
fork 方法是调用一次，返回两次，原因在于操作系统将当前进程（父进程）复制出一份进程（子进程），这两个进程几乎完全相同，
fork 方法分别在父进程和子进程中返回。子进程中永远返回0，父进程中返回的是子进程的ID。
'''
# os 模块中的 getpid 方法用于获取当前进程的 ID，getppid 方法用于获取父进程的 ID
'''
     import os
     if __name__ == '__main__':
        print 'current Process (%s) start ...'%(os.getpid())
        pid = os.fork()
        if pid < 0:
                print 'error in fork'
        elif pid == 0:
                print 'I am child process(%s) and my parent process is (%s)',(os.getpid(),
                os.getppid())
        else:
                print 'I(%s) created a chlid process (%s).',(os.getpid(),pid)
'''


# 2.使用 multiprocessing 模块创建多进程
# multiprocessing 模块提供了一个 Process 类来描述一个进程对象。
# 创建子进程时，只需要传入一个执行函数和函数的参数，即可完成一个 Process 实例的创建，
# 用 start（）方法启动进程，
# 用 join（）方法实现进程间的同步。


# 子进程要执行的代码
def run_process(name):
    print('Child process %s (%s) Running...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_process, args=(str(i),))
        print('Process will start.')
        p.start()
    p.join()
    print('Process end.')

# 启动大量的子进程，使用进程池批量创建子进程
# 3.multiprocessing 模块提供了一个 Pool 类来代表进程池对象
# Pool 可以提供指定数量的进程供用户调用，默认大小是 CPU 的核数


def run_task(name):
    print('Task %s (pid = %s) is running...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)


if __name__ == '__main__':
    print('Current process %s.' % os.getpid())
    # 创建容量为3的进程池
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')





