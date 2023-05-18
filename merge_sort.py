from random import randint
def merge(l, r, buff):
    len_l = len(l)
    len_r = len(r)
    len_buff = len(buff)
    i = j = k = 0
    while i < len_l and j < len_r:
        if l[i] <= r[j]:
            buff[k] = l[i]
            i += 1
        else:
            buff[k] = r[j]
            j += 1
        k += 1
    while i < len_l:
        buff[k] = l[i]
        k += 1
        i += 1
    while j < len_r:
        buff[k] = r[j]
        k += 1
        j += 1

def merge_sort_impl(a, buffer):
    if len(a) == 1:
        return 

    middle = len(a) // 2
    R = a[:middle]
    L = a[middle:]
    merge_sort_impl(R, buffer)
    merge_sort_impl(L, buffer)
    assert len(a) <= len(buffer)
    merge(L, R, buffer)
    for i in range(len(a)):
        a[i] = buffer[i]
        i += 1

def merge_sort(a):
    bf = [0] * (len(a)) 
    merge_sort_impl(a, bf)

arr = [randint(1, 30) for i in range(10)]
print(arr)
merge_sort(arr)
print(arr)