
def binary_search_vanilla(data_list, search_value):
    """
        This is the implementation I came up with in the first go.
        Its not the optimized one, so refer to the binary_search method below.
        :param data_list: The list of data elements having unique and sorted values
        :param search_value: The value to be searched in the data list
        :returns The index of search_value if it is found, else returns -1
    """
    start_index = 0
    end_index = len(data_list)
    midpoint = int((start_index + end_index)/2)
    while start_index <= midpoint <= end_index:
        if search_value == data_list[midpoint]:
            return midpoint
        elif search_value < data_list[midpoint]:
            end_index = midpoint
            midpoint = int((start_index + end_index) / 2)
        else:
            start_index = midpoint
            midpoint = int((start_index + end_index) / 2)
        if midpoint == 0 or midpoint == len(data_list)-1:
            if search_value == data_list[midpoint]:
                return midpoint
            else:
                return -1
    else:
        return -1


def binary_search(data_list, search_value):
    """
        This is the optimized implementation.
        :param data_list: The list of data elements having unique and sorted values
        :param search_value: The value to be searched in the data list
        :returns The index of search_value if it is found, else returns -1
    """
    start_index = 0
    end_index = len(data_list) - 1
    midpoint = (start_index + end_index) // 2
    while start_index <= end_index:
        if search_value == data_list[midpoint]:
            return midpoint
        elif search_value < data_list[midpoint]:
            end_index = midpoint - 1  # The subtraction of 1 ensures the loop termination
            midpoint = int((start_index + end_index) // 2)
        else:
            start_index = midpoint + 1  # The addition of 1 ensures the loop termination
            midpoint = int((start_index + end_index) // 2)
    return -1


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    assert binary_search(list1, 3) == 2
    assert binary_search(list1, 0) == -1
    assert binary_search(list1, -5) == -1
    assert binary_search(list1, 10) == -1

    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search(list2, 3) == 2
    assert binary_search(list2, 4) == 3
    assert binary_search(list2, 8) == 7
    assert binary_search(list2, 9) == 8
    assert binary_search(list2, -5) == -1
    assert binary_search(list2, 10) == -1


if __name__ == '__main__':
    main()
