#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 21:13:49/03/02/19
# Author  : Hugh Sun
# File    : distributed_system.py
# Software: distributed_system.py
'''
distributed system ---master
'''
import random, time, queue
from multiprocessing.managers import BaseManager


#send task queue
task_queue = queue.Queue()

#receive task queue
result_queue = queue.Queue()

#继承BaseManager
class QueueManager(BaseManager):
    pass
if __name__ == "__main__":
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register("get_result_queue",callable=lambda: result_queue)

    #bind port and set 验证码
    #ip = "127.0.0.1"
    #port = 5000
    manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')

    # 启动Queue:
    manager.start()
    print('The task is in queue')
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去:
    for i in range(10):
        n = random.randint(10,10000)
        print('Put task %d' %n)
        task.put(n)

    # 从result队列读取结果:
    print('Try get result')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result %s' %r)

    # 关闭
    manager.shutdown()
    print('Exit')



