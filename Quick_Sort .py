

def partition(L, low, high):
    pivot = L[high]
    i = low - 1
    for j in range(low,high):
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]

    L[i+1], L[high] = L[high], L[i+1]
    return i+1

def quick_sort(L, low, high):
    if low >= high:
        return
    pivot_ind = partition(L, low, high)
    quick_sort(L, low, pivot_ind-1)
    quick_sort(L, pivot_ind+1, high)

numb_list = [1,5,6,8,4,2]
print("Unsorted list: ", numb_list)
quick_sort(numb_list, 0, len(numb_list)-1)
print("Sorted list: ", numb_list)
    












