def reverse_array(arr):
    return arr[::-1]

def reverse_array_manual(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_array([1, 2, 3, 4, 5]))
print(reverse_array_manual([1, 2, 3, 4, 5]))
