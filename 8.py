import threading
def thread_1():
    print("Thread 1 is my function")
thread=threading.Thread(target=thread_1)
thread.start()
thread.join()

print()

shared_variable = 0
lock=threading.Lock()
def increment_shared_variables():
    shared_variable
    with lock:
        shared_variable += 1