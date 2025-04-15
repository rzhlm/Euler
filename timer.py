import time
from statistics import median
from functools import wraps

def timer(iterations = 1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            split_values = []
            for i in range(iterations):
                print(f"timed iteration: #{i+1} of {iterations}")
                start = time.perf_counter()
                do = func(*args, **kwargs)
                split = time.perf_counter() - start
                total_time += time.perf_counter() - start
                split_values.append(split)
            
            avg_time = total_time / iterations
            
            print(f"{func.__name__} takes avg: {avg_time:.4f} sec")
            print(f"median: {median(split_values):.4f}")
            print(f"{split_values=}")
            #print(f"duration: {duration:.4f} s")
    
    
            return do
        return wrapper
    return decorator


def main():
    pass

if __name__ == "__main__":
    main()
