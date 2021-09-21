"""
The task is to implement all function from current file.

1) decorate `csv_to_json` function with `print_time` and check call duration

2) decorate `factorial` function with `print_time` and check call (20 as input) duration
3) decorate `factorial` function with `print_time` and `cache` and check call (20 as input) duration.
4) decorate `factorial` function with `print_time` and `sized_cache(size=10)` and check call (20 as input) duration.
analyze results

5) check the following links:
  * https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-login-required-decorator
    example of decorator usage for authentication in Django framework
  * https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing
    example of decorator usage app routing in Flask framework
  * https://stackoverflow.com/questions/9416947/python-class-based-decorator-with-parameters-that-can-decorate-a-method-or-a-fun
    example of decorator implementation using class and __call__ method
"""


import csv
import json
from pathlib import Path
import time


def print_time(func):
    """
    decorator which print time of function call duration
    >>> @print_time
    >>> def some_func(*args, **kwargs): return "result"
    exampe:
    >>> some_func()
    >>> "start_time: {time here}, end_time: {time here}, duration: {time here}"
    >>> "result"
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        done = time.time()
        print(f"start_time: {start}, end_time: {done}, duration: {done - start}")
        return result

    return wrapper


def cache(func):
    """
    decorator which caches function result
    assuming that all items in args and kwargs are immutable types and can be converted to string (has __str__)
    >>> @cache
    >>> def some_func(*args, **kwargs): pass
    """
    storage = {}

    def wrapper(*args, **kwargs):
        key = str(*args, **kwargs)
        if storage.get(key):
            return storage[key]
        else:
            result = func(*args, **kwargs)
            storage[key] = result
            return result

    return wrapper


def sized_cache(size=10):
    """
    parametrized decorator(fabric of decorators) which caches function result
        but saves not more than size items in cache
    assuming that all items in args and kwargs are immutable types and can be converted to string (has __str__ method)
    >>> @sized_cache(size=5)
    >>> def some_func(*args, **kwargs): pass
    """
    def out_wrapper(func):

        storage = {}
        keys_queue = []

        def wrapper(*args, **kwargs):
            key = str(*args, **kwargs)
            if not storage.get(key):
                result = func(*args, **kwargs)
                storage[key] = result
                keys_queue.append(key)
                if len(keys_queue) > size:
                    del(storage[keys_queue.pop(0)])
            return storage[key]

        return wrapper

    return out_wrapper


@print_time
def csv_to_json(csv_file_path: str, json_file_path: str):
    """
    read csv file and generate json
    csv format: (last_name,first_name,second_name) - example.csv
    json format: check example.json

    >>> csv_to_json('example.csv', 'example_converted.json')

    """
    fieldnames = ('last_name', 'first_name', 'second_name')

    # read csv file
    try:
        with open(Path(csv_file_path)) as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames)
            csv_data = {num: row for num, row in enumerate(csv_reader, start=1)}
    except FileNotFoundError as err:
        raise CustomException() from err

    # generate json
    try:
        with open(Path(json_file_path), 'w') as json_file:
            json.dump(csv_data, json_file, indent=2)
    except OSError as err:
        raise CustomException() from err


@print_time
@cache
def factorial(n: int):
    """
    factorial(n) = 1 * 2 * 3 * ... * (n - 1) * n
    5! = 1 * 2 * 3 * 4 * 5 = 120

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120

    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
