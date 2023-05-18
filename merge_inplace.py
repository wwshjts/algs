from random import randint, shuffle
def merge(arr, l_i, l_end, r_i, r_end, buff_k):
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
    if end - start > 1:
        print(f'sorting{arr[start:end]}')
        #Выбираем границы так, чтобы размер buff
        #был не меньше чем сортируемая часть
        l_e = (start + end) // 2
        r_s = start + end - l_e 
        #Сортируем левую часть массива, используя правую как буфер
        sort(arr, start, l_e, r_s)
        q = r_s
        while q - start > 2:
            new_middle = (start + q) // 2 + (start + q) % 2
            print(f'sorting in  cycle{arr[new_middle:q]}')
            sort(arr, new_middle, q, start)
            merge(arr, start, start + q - new_middle, q, end, buff_k = new_middle)
            q = new_middle

        for i in range(q):
            for j in range(i, end - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]


def merge_sort(arr):
    meta_sort(arr, 0, len(arr))

arr = [x for x in range(1, 9)]
shuffle(arr)
#arr =[0,2,0,1,1,5]
merge_sort(arr)
print(arr)
