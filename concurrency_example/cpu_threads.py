"""
Purpose of this example is to demonstrate multiple threads
(Python instances) being spawned -- in this case up to the
AMOUNT_OF_MATHS.

Use top or activity/system monitor to see a single instance
of Python being ran with very high CPU.
"""
from concurrent.futures import ThreadPoolExecutor, wait
import math
import random


AMOUNT_OF_MATHS = 8


def do_maths():
    for i in range(random.randint(10000000, 30000000)):
        final_sqrt = math.sqrt(i)
    return final_sqrt


def main():
    pool = ThreadPoolExecutor()
    threads = []
    for _ in range(AMOUNT_OF_MATHS):
        threads.append(pool.submit(do_maths))
    wait(threads)


if __name__ == "__main__":
    main()