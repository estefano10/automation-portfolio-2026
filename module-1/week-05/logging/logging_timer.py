import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logging.debug(f"{func.__name__} tardó {end - start:.4f}s")
        return result
    return wrapper

@timer
def apply_iva(subtotal: float) -> float:
    rate = 0.21
    return round(subtotal + subtotal * rate, 2)

print(apply_iva(1000))