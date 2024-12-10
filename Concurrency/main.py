# Created on iPad (Timur).
import _thread
import time
def hello(threadName, delay, lock):
    while 1:
        lock.acquire()
        print(f"{threadName}: Hello,world")
        lock.release()
        time.sleep(delay)

def main():
    lock = _thread.allocate_lock()
    try:
        _thread.start_new_thread(hello,("Tima",1, lock))
        _thread.start_new_thread(hello,("Rusya",1, lock))
    except:
        print("Error")
    while 1:
        pass

if __name__ == "__main__":
    main()