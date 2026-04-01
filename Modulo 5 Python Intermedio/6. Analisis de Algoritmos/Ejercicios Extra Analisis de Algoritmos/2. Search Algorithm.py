

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            print(f"Target {target} found in the list.")
            return True
        
    print(f"Target {target} not found in the list.")
    return False



def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            print(f"Target {target} found in the list.")
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    print(f"Target {target} not found in the list.")
    return False


if __name__ == "__main__":

    my_list = [10, 8, 6, 5, 9, 11, 13, 15, 17, 19]
    target = 5
    linear_search(my_list, target)
    binary_search(my_list, target)
