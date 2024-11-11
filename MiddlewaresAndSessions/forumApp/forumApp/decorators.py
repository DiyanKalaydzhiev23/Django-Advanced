import time
from functools import wraps


def measure_execution_time(view_func):
    @wraps(view_func)
    def _wrapper(request, *args, **kwargs):
        start_time = time.time()
        result = view_func(request, *args, **kwargs)
        end_time = time.time()

        print(f"The time it took for {view_func.__name__}: ", end_time - start_time, "seconds")

        return result

    return _wrapper
