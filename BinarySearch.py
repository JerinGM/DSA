# input_list = [8, 8, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 1]
# input_list = [9, 8, 6, 5, 4, 3, 2, 1, 0]
# input_list = [5, 4, 3, 2, 1]
input_list = [10, 8, 8, 7, 7, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 1, 0, -1, -1, -1, -4, -5, -10]

query = -1


def binary_search_function(input_list, query):
    found = False
    high = len(input_list) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        # print(f"Low is {low}\nHigh is {high}\n Mid is {mid}")
        if input_list[mid] == query and (mid == 0 or input_list[mid-1] != query):
            print(f"Found at index {mid}")
            found = True
            break
        elif input_list[mid] == query and input_list[mid-1] == query and mid-1 >= 0:
            high = mid - 1
        elif input_list[mid] > query:
            low = mid + 1
        elif input_list[mid] < query:
            high = mid - 1
    if not found:
        print("No such item")


binary_search_function(input_list, query)
