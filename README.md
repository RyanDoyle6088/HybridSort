![](images/sorting_complexities.png)

A **sorting algorithm** is an algorithm that puts elements in a certain order. This is commonly seen when we need to
organize an array or list in numerical or lexicographical order. 

There are various sorting algorithms - each with their own benefits in terms of efficiency. This project will be 
focussing on the *Insertion Sort Algorithm* and the *Merge Sort Algorithm*. 

####Insertion Sort

![](images/insertion_sort.png)

Insertion sort is an in place comparison based sorting algorithm. It builds a final sorted array by comparing one
element at a time and inserting it into it's appropriate location. 

The worst case runtime is O(n^2).
The best case runtime is O(n) - in the case that the array is already sorted. 
The space complexity is O(1) for in place implementation.

####Merge Sort

![](images/merge_sort.png)

Merge sort is one of the most efficient sorting algorithms. It works on the principle of Divide and Conquer. 
Merge sort repeatedly breaks down a list into several sublists until each sublist consists of a single element and 
merging those sublists in a manner that results into a sorted list.

The worst case runtime is O(nlog(n)).
The best case runtime is O(nlog(n)). 
The space complexity is O(N) - as new arrays are created everytime you divide.

####Hybrid Sort

While Merge Sort has a faster average runtime than Insertion Sort, there are instances that an Insertion Sort is more 
efficient. Due to the overhead of recursively splitting containers with a Merge Sort, Insertion Sort can have a faster 
performance with small sets of data.

## Project Details
### Overview
You will be implementing the Insertion Sort Algorithm and the Merge Sort Algorithm. You will develop your Merge Sort 
such that it can be used as a Hybrid Sort when given a threshold value. The Hybrid Sort will rely on Merge Sort until 
the partitioned lists are less than or equal to a given threshold, at which point you will switch to Insertion Sort.

In addition to these sorting algorithms, you will be implementing an algorithm to determine the *inversion count* of 
a list of elements. This algorithm will be integrated into your merge_sort function. You will only calculate the inversion 
count when your function is not being used as a Hybrid Sort, that is, the threshold is 0.

The inversion count is how far away a list of elements is from being sorted. The inversion count of a sorted array is 0.
You can think of the number of inversions as the number of pairs of elements that are out of order.

Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

##### Examples:

**data = [3,2,9,0]**
- data has 4 inversions:
   - (3, 2): 3 > 2 but 3 comes before 2
   - (3, 0): 3 > 0 but 3 comes before 0
   - (2, 0): 2 > 0 but 2 comes before 0
   - (9, 0): 9 > 0 but 9 comes before 0
    

**data = [1, 2, 3, 4, 5]**
- data has 0 inversions

Note: Although you can swap the elements of the inversions to form a sorted array, the inversion count is not the same 
as the minimum number of swaps to sort the array.

For instance, data = [10, 1, 2, 0]. 

You could sort this in 1 *swap* (10, 0), but there are 5 *inversions* (10, 1), (10, 2), (10, 0), (1, 0), (2, 0).

### Assignment Specs
You are given one file, HybridSort.py. You must complete and implement the following functions. 
Take note of the specified return values and input parameters. *Do not change the function signatures*.

You must adhere to the required time & space complexities.


**HybridSort.py:**

- **insertion_sort(data)**
    - Given a list of values, perform an insertion sort to sort the list.
    - data: List of str or int to be sorted.
    - return: None
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
- **merge_sort(data, threshold = 0)**
    - Given a list of values, perform a merge sort to sort the list and calculate the inversion count. When a threshold 
    is provided, use a merge sort algorithm until the partitioned lists are smaller than or equal to the threshold - 
    then use insertion sort.
    - data: List of str or int to be sorted.
    - threshold: int representing the size of the data at which insertion sort should be used. Defaults to 0.
    - return: int representing inversion count. 0 if threshold > 0.
    - **NOTE**: The inversion count will be calculated when only a merge_sort algorithm is used! (when threshold is 0) 
    return 0 otherwise.
    - **NOTE**: This must be done recursively
    - Time Complexity: O(n*log(n))
    - Space Complexity: O(n)
    
- **hybrid_sort(data, threshold)**
    - Wrapper function to use merge_sort() as a Hybrid Sorting Algorithm. Should call merge_sort() with provided 
    threshold.
    - data: List of str or int to be sorted.
    - threshold: int representing the size of the data at which insertion sort should be used.
    - return: None
    - Time Complexity: O(n*log(n))
    - Space Complexity: O(n)
   
- **inversion_count(data)**
    - Wrapper function to use merge_sort() to retrieve the inversion count. Should call merge_sort() with *no threshold.*
    - data: List of str or int to be sorted.
    - return: int representing inversion count.
    - Time Complexity: O(n*log(n))
    - Space Complexity: O(n)
    
####Application

You will be designing a simple recommendation engine for SELF.FIND(LOVE), a popular dating app for programmers. 

Given a user's ranking of interests, and the candidate interest rankings, you will need to find the candidate 
who most closely relates to them, that is, their rankings are **closest to being in the same order** of the user's.

#####Examples
Suppose the Zosha has ranked their interests in this order: 

1. Dogs
2. Indie Music
3. House Plants
4. Peanut Butter
5. Thrift Stores

These are the potential candidates and their ranking of these interests:
- Daniel
    - [Dogs, Indie Music, Thrift Stores, House Plants, Peanut Butter]
- Sabrein
    - [Thrift Stores, Peanut Butter, House Plants, Indie Music, Dogs]
    
Here is how the candidates compare to Zosha:
![](images/application_example.png)

Daniel would be their ideal match because they have the *least number of interests in a different order* than Zosha.

Sabrein has 10 interests out of order where Daniel has 2.