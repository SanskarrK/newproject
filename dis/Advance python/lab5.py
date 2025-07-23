import threading, multiprocessing

def work():
    print("Working")

# Thread
t = threading.Thread(target=work)
t.start()

# Process
p = multiprocessing.Process(target=work)
p.start()
t.join()
p.join()
print("Thread and Process completed")

