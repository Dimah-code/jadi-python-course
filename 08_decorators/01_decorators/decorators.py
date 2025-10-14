import functools
import time


def timer_decorator(print_result=False):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()

            result = func(*args, **kwargs)

            end_time = time.perf_counter()
            execution_time = end_time - start_time

            print(f"'{func.__name__}': {execution_time:.6f} seconds")

            if print_result and len(str(result)) < 100:
                print(f"Result: {result}")

            return result

        return wrapper

    return decorator


@timer_decorator(print_result=True)
def create_list(n):

    return list(range(1, n + 1))


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    result = create_list(n)

    if n > 20:
        print(f"List: {result[:5]} ... {result[-5:]}")
    else:
        print(f"List: {len(result)}")
