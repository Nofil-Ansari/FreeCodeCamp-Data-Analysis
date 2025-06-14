import numpy as np
def calculate(param_list):
    arr = np.array(param_list).reshape(3, 3)
    matrix = np.matrix(arr)
    mean = np.mean(matrix, axis=0).tolist()[0]
    variance = np.var(matrix, axis=0).tolist()[0]
    std_dev = np.std(matrix, axis=0).tolist()[0]
    max_val = np.max(matrix, axis=0).tolist()[0]
    min_val = np.min(matrix, axis=0).tolist()[0]
    sum_val = np.sum(matrix, axis=0).tolist()[0]
    
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
print(calculate([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    

    