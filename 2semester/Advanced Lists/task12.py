import numpy as np

def cumulative_sum(input_list):
    np_list = np.array(input_list)
    cum_sum = np.cumsum(np_list)
    return cum_sum.tolist()

input_list = [4, 10, 15, 18, 20]
output_list = cumulative_sum(input_list)
print("Output:", output_list)
