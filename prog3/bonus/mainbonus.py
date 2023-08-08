import fib_file_sync, fib_file_multi, fib_file_async
import time
N = 50

def timetrack(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        print(f"Function ~ {func.__name__} ~ took {time.time() - before} seconds")
        
    return wrapper

'''
timed_sync = timetrack(fib_file_sync.synchronous_fib)
timed_multi = timetrack(fib_file_multi.multiprocess_fib)
timed_async = timetrack(fib_file_async.threading_fib)
if __name__ == "__main__": #needed to run multiprocessing in python
    timed_multi(N)
    timed_sync(N)
    timed_async(N)
'''
st = time.time()
fib_file_sync.synchronous_fib(N)
print(f"Synchronous processing took {time.time() - st} seconds")

st = time.time()
fib_file_multi.multiprocess_fib(N)
print(f"multiprocessing took {time.time() - st} seconds")

st = time.time()
fib_file_async.threading_fib(N)
print(f"Asynchronous processing took {time.time() - st} seconds")