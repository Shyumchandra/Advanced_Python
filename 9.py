import threading
import time

tickets = 10
semaphore=threading.Semaphore(2)

def buy_tickets():
    with semaphore:
        global tickets
        if tickets > 0:
            tickets-=1
            print(tickets)
        else:
            print("no tickets are available")

def ticket_simulation():
    threads=[]
    for i in range(10):
        thread=threading.Thread(target=buy_tickets)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    ticket_simulation()