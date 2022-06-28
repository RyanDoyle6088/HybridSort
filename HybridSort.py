"""
Name: Ryan Doyle
Hybrid Sorting - Starter Code
"""
from typing import List, Any, Dict


def hybrid_sort(data: List[Any], threshold: int) -> None:
    """
    performs merge sort as a hybrid sorting algorithm.
    it calls merge_sort() function with provided threshold.
    """
    count = merge_sort(data, threshold)


def inversions_count(data: List[Any]) -> int:
    """
    returns the inversion count of the list provided.
    """
    return merge_sort(data)


def merge_sort(data: List[Any], threshold: int = 0) -> int:
    """
    sorts the list provided using merge sort and returns inversion count

    merge sort is performed to sort the list and inversion count is calculated.
    when a threshold is provided, this function uses merge sort algorithm until
    the lists are smaller than or equal to the threshold, then uses insertion sort.
    """
    # If size of data is less than threshold
    if len(data) <= threshold:
        insertion_sort(data)
        return 0
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0]*(len(data))
    return merge_sort_util(data, temp_arr, 0, len(data)-1, threshold)


def merge_sort_util(data: List[Any], temp_arr: List[Any], left: int, right: int, threshold: int) -> int:
    """
    Utility function for merge sort and returns inversion count.
    """
    # store inversion counts in each recursive call
    inv_count = 0
    # if size of data is less than threshold
    if (right-left+1) <= threshold:
        data1 = [x for x in data[left:right+1]]
        insertion_sort(data1)
        j = 0
        for i in range(left, right+1):
            data[i] = data1[j]
            j += 1
        return inv_count
    # will make a recursive call if and only if
    # we have more than one elements
    if left < right:
        # mid is calculated to divide the array into two sub arrays
        mid = (left + right)//2
        # calculate inversion counts in the left subarray
        inv_count += merge_sort_util(data, temp_arr, left, mid, threshold)
        # calculate inversion counts in right subarray
        inv_count += merge_sort_util(data, temp_arr, mid + 1, right, threshold)
        # merge two sub arrays in a sorted sub array
        inv_count += merge_util(data, temp_arr, left, mid, right)
    return inv_count


def merge_util(data: List[Any], temp_arr: List[Any], left: int, mid: int, right: int) -> int:
    """
    Utility function will merge two sorted list into single list.
    """
    i = left     # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0
    while i <= mid and j <= right:
        if data[i] <= data[j]:
            temp_arr[k] = data[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = data[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = data[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = data[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        data[loop_var] = temp_arr[loop_var]
    return inv_count


def insertion_sort(data: List[Any]) -> None:
    """
    This function performs insertion sort to sort the list of values.
    """
    # Traverse through 1 to len(data)
    for i in range(1, len(data)):
        k = data[i]
        j = i - 1
        while j >= 0 and k < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = k


def find_match(user_interests: List[str], candidate_interests: Dict[str, List]) -> str:
    """
    Returns the name of the candidate whose interest ranking
    match most closely to the user's.
    """
    # Rank of the user interest
    map_count = 1
    mapping = {}
    for i in user_interests:
        mapping[i] = map_count
        map_count = map_count + 1
    u_least = -1  # user with least inversion count
    u_match = ""
    for num, i in candidate_interests.items():
        i_map = [mapping[x] for x in i]  # mapping according to the user interests
        cnt = inversions_count(i_map)  # inversion count
        # Updating the user with least inversion count
        if u_least == -1:
            u_least = cnt
            u_match = num
        else:
            if u_least > cnt:
                u_least = cnt
                u_match = num
    return u_match
