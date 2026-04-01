def bubble_sort(list):
    n = len(list) #O(1)
    for i in range(n): #O(n)
        for j in range(0, n-i-1): #O(n^2)
            if list[j] > list[j+1]: #O(n)
                list[j], list[j+1] = list[j+1], list[j] #O(1)
    return list #O(1)



list = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", list)
sorted_list = bubble_sort(list)
print("Lista ordenada:", sorted_list) 