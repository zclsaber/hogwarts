import threading
import time


# 定义一个线程执行的任务
def task():
    for i in range(10):
        print(f"线程 {threading.current_thread().name} 执行第 {i+1} 次任务")

# 创建两个线程
t1 = threading.Thread(target=task, name='Thread-1')
t2 = threading.Thread(target=task, name='Thread-2')

# 启动两个线程，开始执行任务
t1.start()

for i in range(1, 11):
    time.sleep(1)
    print("first sleep " + str(i) + " seconds")

t2.start()


# 等待两个线程执行完成
t1.join()

for i in range(1, 11):
    time.sleep(1)
    print("sleep " + str(i) + " seconds")

t2.join()



# 任务执行完成
print('任务执行完成')