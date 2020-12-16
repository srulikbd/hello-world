import copy
import time
import functools

# from classes.Logger import log_info

"""
This file contains useful decorators.
"""



def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        return_value = func(*args, **kwargs)
        run_time = time.time() - start_time
        log_info(
            f"Finished {func.__name__!r} in {int(run_time)} secs, {run_time / 60:.1f} min, {run_time / 60 / 60:.2f} hours")
        return return_value

    return wrapper_timer