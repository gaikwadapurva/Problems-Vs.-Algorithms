def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    
    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len (right):
        if left[left_index] < right[right_index]:
            merged_list.append(right[right_index])
            right_index += 1
        else:
            merged_list.append(left[left_index])
            left_index += 1
        
    merged_list += left[left_index:]
    merged_list += right[right_index:]

    return merged_list


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = merge_sort(input_list)

    num1 = 0
    num2 = 0

    for index in range(0, len(input_list), 2):
        num1 = (num1 * 10) + input_list[index]
    
    for index in range(1, len(input_list), 2):
        num2 = (num2 * 10) + input_list[index]

    return [num1, num2]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[],[0,0]])
test_function([[3],[0,3]])
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])