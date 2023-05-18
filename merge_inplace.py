from random import randint, shuffle
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
    if end - start > 1:
        print(f'sorting{arr[start:end]}')
        #Выбираем границы так, чтобы размер buff
        #был не меньше чем сортируемая часть
        l_e = (start + end) // 2
        r_s = start + end - l_e 
        print(f'call sort on {arr[start:l_e]} to {arr[r_s]}')
        #Сортируем левую часть массива, используя правую как буфер
        sort(arr, start, l_e, r_s)
        print(f'after sorting {arr}')

        #После этого все эл-ты начиная с r_s отсортированы
        #Теперь отсортируем середину в левую часть
        middle = (start + r_s) // 2 + (start + r_s) % 2
        

        print(f'sorting 1/4 {arr[middle:r_s]} to {arr[start]}')
        sort(arr, middle, r_s, buff_k = start)
        print(f'after sorting 1/4 {arr}')

        #Мерджим отсортированные части
        print(f'merge {arr[start:start + r_s - middle]} and {arr[r_s:end]}')
        merge(arr, start, start + r_s - middle, r_s, end, buff_k = middle)
        print(f'after merge {arr}')
        #В данный момент отстортирована часть начиная с middle
        
        #разбить на пополам [start, middle)
        #[start, new_middle) [new_middle, middle)
        #отсотрировать sort(arr, new_middle, middle, start) 
        #merge
        #и так далее
        #Указатель на остортированную часть
        q = middle
        #print(q - start)
        while q - start > 2:
            new_middle = (start + q) // 2 + (start + q) % 2
            print(f'sorting like normal {arr[new_middle:q]}')
            sort(arr, new_middle, q, start)
            print(f'after sorting like normak{arr}')
            #после этого отсортированная часть
            merge(arr, start, start + r_s - new_middle, q, end, buff_k = new_middle)
            q = new_middle
        for i in range(start, q-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
#        print(f'res {arr}')

def merge_sort(arr):
    meta_sort(arr, 0, len(arr))

arr = [x for x in range(1, 9)]
shuffle(arr)
merge_sort(arr)
print(arr)
