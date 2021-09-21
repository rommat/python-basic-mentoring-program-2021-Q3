
"""

    2.	Context manager.

Реализуйте контекстный менеджер timer, используя __enter__ и __exit__

Check yourself:

with timer('doing some sleeps'):
    time.sleep(1)
    time.sleep(2)
    time.sleep(3)

Output:
timer: block 'doing some sleeps' executed in 6.013 sec

"""


from time import perf_counter, sleep


class Timer:
    def __init__(self, block_name):
        self.block_name = block_name
        self._start = 0.0

    def __enter__(self):
        self._start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = perf_counter()
        duration = round(end - self._start, 3)
        print(f"Block '{self.block_name}' executed in {duration} sec")


with Timer('doing some sleeps'):
    sleep(1)
    sleep(2)
    sleep(3)
