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


def csv_to_json(csv_file_path: str, json_file_path: str):
    """
    read csv file and generate json
    csv format: (last_name,first_name,second_name) - example.csv
    json format: check example.json
    """

    raise NotImplementedError


def factorial(n: int):
    """
    factorial(n) = 1 * 2 * 3 * ... * (n - 1) * n
    5! = 1 * 2 * 3 * 4 * 5 = 120.
    """
    raise NotImplementedError


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
    pass


def cache(func):
    """
    decorator which caches function result
    assuming that all items in args and kwargs are immutable types and can be converted to string (has __str__)
    >>> @cache
    >>> def some_func(*args, **kwargs): pass
    """
    raise NotImplementedError


def sized_cache(size=10):
    """
    parametrized decorator(fabric of decorators) which caches function result
        but saves not more than size items in cache
    assuming that all items in args and kwargs are immutable types and can be converted to string (has __str__ method)
    >>> @sized_cache(size=5)
    >>> def some_func(*args, **kwargs): pass
    """
    raise NotImplementedError
