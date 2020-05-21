'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

import collections


def sliding_window_max(nums, k):
    deque, result = collections.deque(), []

    for index, num in enumerate(nums):
        while deque and deque[0][1] <= index - k:
            deque.popleft()
        while deque and num > deque[-1][0]:
            deque.pop()
        deque.append([num, index])

        if index >= k - 1:
            result.append(deque[0][0])

    return result

    # old way much slower 
    # Your code here
    # final_array = []
    # array_max = None
    # for index, i in enumerate(nums):
    #     window = nums[index:index + k]
    #     if len(window) < k:
    #         pass
    #     else:
    #         array_max = max(window)
    #         final_array.append(array_max)
    #
    # return final_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
