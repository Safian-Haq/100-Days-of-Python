import time


def speed_calc_decorator(benchmark_function):

    def benchmark():
        print(f'Starting {benchmark_function.__name__} inside wrapper')
        start_time = time.time()
        benchmark_function()
        run_time = time.time() - start_time
        print(f'Benchmark: {run_time}')
        print(f'Ending {benchmark_function.__name__} inside wrapper\n\n')

    return benchmark

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


if __name__ == '__main__':
    print('Start**\n')
    fast_function()
    slow_function()
