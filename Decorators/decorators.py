import time
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def first_decorator(funk):
    def wrapper():
        print("falling asleep")
        funk()
        print("wake up")
    return wrapper

def second_decorator(funk):
    def wrapper():
        print("Second in")
        funk()
        print("Second out")
    return wrapper

def log_decorator(debug=False):
    def inner(func):
        def wrapper():
            start_time = time.time()
            if debug:
                logger.info(f"Execution started at {start_time}")
            func()
            end_time = time.time()
            if debug:
                logger.info(f"Execution ended at {end_time}")
                logger.info(f"Execution took {end_time - start_time}")
        return wrapper
    return inner
# @second_decorator
# @first_decorator
@log_decorator(debug=True)
def long_function():
    time.sleep(5)
    print("Inside the funktion")

# long_function = first_decorator(long_function)

if __name__ == "__main__":
    long_function()

