### Analysis

The input array here is a rotated sorted array, the solution to finding whether the given number exists in the array or not involves the usage of binary search algorithm.

Time complexity: The time complexity is O(log n) because given the initial problem of size n (to search in a rotated sorted array), the size n is divided into sub-problem of size n/2 until we reach a problem of size 1.

Space complexity: The space complexity is O(1) because the algorithm maintains a constant extra space, regardless of input size.