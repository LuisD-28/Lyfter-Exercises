def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list



list = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", list)
sorted_list = bubble_sort(list)
print("Lista ordenada:", sorted_list) 


# Ejercicio 2: Modificar el bubble sort para que ordene de derecha a izquierda.
def bubble_sort_right_to_left(list):
    n = len(list)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
    return list



list = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", list)
sorted_list = bubble_sort_right_to_left(list)
print("Lista ordenada de derecha a izquierda:", sorted_list)