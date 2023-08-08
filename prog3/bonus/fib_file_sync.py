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


def synchronous_fib(num):

    for j in range(num):
        file_path = os.path.join("fib_file_sync_text", f'filename_{j+1}.txt')
        with open(file_path, 'w') as filehandle: 
            filehandle.write(str(fib(j+1)))


    
