import time
from contextlib import contextmanager

@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"time: {(end_time - start_time)//0.001/1000}")

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print(f"time: {(end_time - self.start_time)//0.001/1000}")


if __name__ == "__main__":
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)
        