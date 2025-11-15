import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        elapsed = end - start
        print(f"{func.__name__} executed in {elapsed} seconds")

        return result
    
    return wrapper