def bubble_sort(data_list):
    """
    Runtime is O(n^2) since each loop takes n-1 iterations.
    :param data_list: The data list which needs to be sorted
    :return: The sorted list
    """
    outer_loop_count = 0
    end_index = len(data_list) - 1
    # n - 1 outer loops
    while outer_loop_count < len(data_list) - 1:
        index = 0
        # n - 1 comparisons
        while index < end_index:
            if data_list[index+1] < data_list[index]:
                # logic to swap two variables without using additional variable
                data_list[index] = data_list[index] + data_list[index+1]  # x = x + y
                data_list[index+1] = data_list[index] - data_list[index+1]  # y = x - y
                data_list[index] = data_list[index] - data_list[index+1]  # x = x - y
            index += 1
        outer_loop_count += 1
        end_index -= 1
    return data_list


def main():
    list1 = [1, 7, 2, 6, 3, 8, 9]
    print(bubble_sort(list1))
    list2 = [11, -5, 0, 1, 7, 2, 6, 3, 8, 9]
    print(bubble_sort(list2))

if __name__ == '__main__':
    main()
