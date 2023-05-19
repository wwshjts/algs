def merge(l, r, buff):
    len_l = len(l)
    len_r = len(r)
    len_buff = len(buff)
    i = j = k = 0
    counter = 0
    while i < len_l and j < len_r:
        if l[i] <= r[j]:
            buff[k] = l[i]
            i += 1
        else:
            buff[k] = r[j]
            j += 1
            counter += len_l - i
        k += 1
    while i < len_l:
        buff[k] = l[i]
        k += 1
        i += 1
    while j < len_r:
        buff[k] = r[j]
        k += 1
        j += 1
    print(f'{l}, {r}, {counter}')
    return counter

def merge_sort(a):
    if len(a) == 1:
        return 0 

    middle = len(a) // 2
    L = a[:middle]
    R = a[middle:]
    left = merge_sort(L)
    right = merge_sort(R)
    buffer = [0] * len(a)
    split = merge(L, R, buffer)
    for i in range(len(a)):
        a[i] = buffer[i]
        i += 1
    return left + right + split

a = [1,0,2]
cnt = 0
for i in range(len(a) - 1):
    if a[i] > a[i+1]: cnt += 1

s = merge_sort(a)
print(a)
print(s, cnt)