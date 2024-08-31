def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot,end):
    swapindex = pivot
    for i in range(pivot + 1, end+1):
        if my_list[i] < my_list[pivot]:
            swapindex += 1
            swap(my_list,i,swapindex)
    swap(my_list,pivot,swapindex)
    return swapindex

def quicksort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quicksort(my_list, left, pivot_index - 1)
        quicksort(my_list, pivot_index + 1, right)
    return my_list

my_list = [4,1,6,7,3,2,5]
print(quicksort(my_list, 0, 6))
