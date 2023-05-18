from random import randint
def merge(arr, l_i, l_end, r_i, r_end, buff_k):
    #print(l_i, l_end, r_i, r_end, buff_k)
    #print(f'l:{arr[l_i:l_end]} r:{arr[r_i:r_end]}')
    while l_i < l_end and r_i < r_end:
        if arr[l_i] <= arr[r_i]:
            arr[l_i], arr[buff_k] = arr[buff_k], arr[l_i]
            l_i += 1
        else:
            arr[r_i], arr[buff_k] = arr[buff_k], arr[r_i]
            r_i += 1
        buff_k += 1
    while l_i < l_end:
        arr[l_i], arr[buff_k] = arr[buff_k], arr[l_i]
        l_i += 1
        buff_k += 1
    while r_i < r_end:
        arr[r_i], arr[buff_k] = arr[buff_k], arr[r_i]
        r_i += 1
        buff_k += 1

def sort(arr, start, end, buff_k):
    if end - start == 1:
        arr[start], arr[buff_k] = arr[buff_k], arr[start]
    else:
        #Иначе разбиваем массив на левую и правую часть
        middle = (start + end) // 2
        #Сортируем левую часть при помощи sort, используя правую как буффер
        #print(f'in sort{arr[start:end]} to {arr[buff_k]}')
        meta_sort(arr, start, middle)
        meta_sort(arr, middle, end)
        merge(arr, start, middle, middle, end, buff_k)

def meta_sort(arr, start, end):
    if end - start > 2:
        print(f'sorting{arr[start:end]}')
        #Выбираем границы так, чтобы размер buff
        #был не меньше чем сортируемая часть
        l_e = (start + end) // 2
        r_s = start + end - l_e 
        print(f'call sort on {arr[start:l_e]} to {arr[r_s]}')
        sort(arr, start, l_e, r_s)
        print(f'after sorting {arr}')

        #После этого все эл-ты начиная с r_s отсортированы
        #Теперь отсортируем середину в левую часть
        middle = (start + r_s) // 2 + (start + r_s) % 2
        print(f'sorting 1/4 {arr[middle:r_s]} to {arr[start]}')
        sort(arr, middle, r_s, buff_k = start)
        print(f'after sorting 1/4 {arr}')

        #Мерджим отсортированные части
        print(f'merge {arr[start:middle]} and {arr[r_s:end]}')
        merge(arr, start, start + r_s - middle, r_s, end, buff_k = middle)
        print(f'after merge {arr}')

        print(f'now meta sort{arr[start: middle]}')
        meta_sort(arr, start, middle)
    elif end - start == 2:
        if arr[start] > arr[end - 1]:
            arr[start], arr[end - 1] = arr[end - 1], arr[start]

def merge_sort(arr):
    meta_sort(arr, 0, len(arr))

arr = [randint(0, 10) for i in range(5)]
merge_sort(arr)
print(arr)
