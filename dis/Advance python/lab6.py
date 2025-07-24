import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        print(f"Elapsed: {self.end - self.start:.4f} seconds")

with Timer():
    sum([i ** 2 for i in range(10_000_000)])
