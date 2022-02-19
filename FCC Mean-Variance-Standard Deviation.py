import numpy as np


def calculate(digits):
    for i in digits:
        if type(i) != int:
            return 'Incorrect input'
    if len(digits) != 9:
        raise ValueError('List should contain nine numbers')
    a = digits[:3]
    b = digits[3:6]
    c = digits[6:]
    arr = np.array([a, b, c])
    print(np.mean(arr, axis=0))
    results = \
        {
            'mean': [[*np.mean(arr, axis=0)], [*np.mean(arr, axis=1)], np.mean(arr.flatten())],
            'variance': [[*np.var(arr, axis=0)], [*np.var(arr, axis=1)], np.var(arr.flatten())],
            'standard deviation': [[*np.std(arr, axis=0)], [*np.std(arr, axis=1)], np.std(arr.flatten())],
            'max': [[*np.max(arr, axis=0)], [*np.max(arr, axis=1)], np.max(arr.flatten())],
            'min': [[*np.min(arr, axis=0)], [*np.min(arr, axis=1)], np.min(arr.flatten())],
            'sum': [[*np.sum(arr, axis=0)], [*np.sum(arr, axis=1)], np.sum(arr.flatten())]
        }
    return results

print(calculate([1,2,3,4,5,6,7,8,9]))