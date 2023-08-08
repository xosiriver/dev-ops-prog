import threading
import concurrent.futures
import os
import numpy as np

def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    base_matrix = np.array([[1, 1], [1, 0]])
    
    def matrix_power(matrix, k):
        if k == 1:
            return matrix
        if k % 2 == 0:
            half_power = matrix_power(matrix, k // 2)
            return np.dot(half_power, half_power)
        else:
            half_power = matrix_power(matrix, (k - 1) // 2)
            return np.dot(matrix, np.dot(half_power, half_power))
    
    powered_matrix = matrix_power(base_matrix, n - 1)
    return powered_matrix[0][0]


def flcreate(num, semaphore):

        file_path = os.path.join(os.getcwd(),"fib_file_async_text", f'filename_{num+1}.txt')
        with open(file_path, 'w') as filehandle: 
            filehandle.write(str(fib(num+1)))

def threading_fib(N):
    load_size = N // 10
    num_chunks = N // load_size
    threads = []
    max_threads = 20  # Adjust this value based on your system's limitations
    semaphore = threading.Semaphore(max_threads)
    
    for i in range(num_chunks):
        start = i * load_size
        end = (i + 1) * load_size
        thread = threading.Thread(target=lambda: [flcreate(num, semaphore) for num in range(start, end)])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

