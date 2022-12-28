import math


def batch_generator(data_size: int, batch_size: int = 25):
    num_of_batches = math.ceil(data_size / batch_size)  # 11

    batch_combination = []
    for batch_no in range(num_of_batches):
        batch_start = batch_no * batch_size
        batch_end = (batch_no + 1) * batch_size - 1
        if batch_no == num_of_batches - 1:
            batch_end = data_size - 1
        batch_combination.append((batch_start, batch_end))
    return batch_combination
