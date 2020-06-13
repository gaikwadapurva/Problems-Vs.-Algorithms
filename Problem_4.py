def sort_012(input_list):
    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_index = 0

    while front_index <= next_pos_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:           
            input_list[front_index] = input_list[next_pos_2] 
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1
    
    return input_list


def test_function(input_list):
    sorted_array = sort_012(input_list)
    print(sorted_array)
    if sorted_array == sorted(input_list):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 1, 0])
test_function([0, 0, 0, 0, 0])
test_function([])