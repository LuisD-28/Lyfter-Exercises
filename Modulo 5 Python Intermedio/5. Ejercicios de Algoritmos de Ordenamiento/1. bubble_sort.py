def bubble_sort(lst):
    if not isinstance(lst, list):
        raise TypeError("El argumento debe ser una lista.")
    
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst



lst = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lst)
sorted_list = bubble_sort(lst)
print("Lista ordenada:", sorted_list) 


# Ejercicio 2: Modificar el bubble sort para que ordene de derecha a izquierda.
def bubble_sort_right_to_left(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst



lst = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lst)
sorted_list = bubble_sort_right_to_left(lst)
print("Lista ordenada de derecha a izquierda:", sorted_list)