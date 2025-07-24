import threading
import time

class WorkerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"Thread {self.name} starting")
        time.sleep(2)
        print(f"Thread {self.name} done")

t1 = WorkerThread("A")
t2 = WorkerThread("B")
t1.start()
t2.start()
t1.join()
t2.join()
sum([i ** 2 for i in range(10_000_000)])
print("All threads completed")
