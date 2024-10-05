import threading
import time

def worker_thread():
    while not event.is_set():
        print("worker thread is running.......")
    time.sleep(1)
    print("worker thread finished the work")

if __name__ == "__main__":
    event=threading.Event()
    threads=[]
    num_threads=5
    for i in range(num_threads):
        thread=threading.Thread(target=worker_thread)
        threads.append(thread)
        thread.start()
        
    time.sleep(5)
    event.set()
    for thread in threads:
        thread.join()
    print("All Threads has stopped!")
        