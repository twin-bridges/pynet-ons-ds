from concurrent.futures import ProcessPoolExecutor, as_completed
import math
import random


AMOUNT_OF_MATHS = 8


def do_maths():
    for i in range(random.randint(10000000, 30000000)):
        final_sqrt = math.sqrt(i)
    return final_sqrt


def main():
    pool = ProcessPoolExecutor()
    procs = []
    for _ in range(AMOUNT_OF_MATHS):
        procs.append(pool.submit(do_maths))
    for proc in as_completed(procs):
        print(proc.result())


if __name__ == "__main__":
    main()
