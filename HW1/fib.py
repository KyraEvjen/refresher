from functools import lru_cache
import matplotlib.pyplot as plt
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f" Finished in {total_time:.8f} seconds: f({args[0]}) -> {result}")
        y.append(total_time)
        x.append(args[0])
        return result

    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    x = []
    y = []
    fib(100)
    plt.plot(x, y)
    plt.show()
