import numpy as np


def filter_data(data, threshold):
    threshold = np.float(threshold)
    return [i for i in data if np.greater(i[2], threshold)]


def sort_data(data):
    sorted_data = sorted(data, key=lambda tup: float(tup[2]), reverse=True)
    return sorted_data[:5]


def print_data(abstract, data):
    for i in range(len(data)):
        print(data[i][2])
