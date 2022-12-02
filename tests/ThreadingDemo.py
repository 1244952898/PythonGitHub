import _thread
import time


def print_time(tname: str, delay: int):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (tname, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ('T0', 2))
    _thread.start_new_thread(print_time, ('T1', 1))
except:
    print("Error: 无法启动线程")
while 1:
    pass
