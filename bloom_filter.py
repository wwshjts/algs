from math import log, e
from random import shuffle, randint
class BitSet:
    def __init__(self, size_bits = 8):
        self.size = size_bits // 8 + 1
        self.bit_array = [0] * self.size

    def __getitem__(self, index):
        block = index // 8
        mask = 1 << (index % 8)
        return 1 if self.bit_array[block] & mask else 0

    def __setitem__(self, index, val):
        block = index // 8 
        mask = 255 - (1 << (index % 8))
        self.bit_array[block] = self.bit_array[block] & mask
        mask = val << (index % 8)
        self.bit_array[block] += mask
    
    @property
    def print(self):
        for i in range(self.size):
            mask = 1
            x = self.bit_array[i]
            for i in range(8):
                print(1 if (x & mask) else 0, end = '')
                mask = mask << 1
        print()

class BloomFilter:
    def __init__(self, eps = 0.1, s = 10):
        #Погрешность
        self.eps = eps
        #Количество обращений
        self.s = s
        self.b = int(log(eps, 0.5) / log(2)) + 1
        self.k = int(log(2) * self.b) + 1
        self.n = self.s * self.b
        self.arr = BitSet(self.n)
        self.func = []
        for i in range(self.k):
            self.func.append([randint(0,self.n - 1) for i in range(4)])
    

    def call_func(self, index, x):
        return sum(self.func[index][i] * x[i] for i in range(4)) % self.n

    def insert(self, ip):
        for i in range(self.k):
            ind = self.call_func(i, ip)
            self.arr[ind] = 1
    
    def lookup(self, ip):
        flag = True
        for i in range(self.k):
            ind = self.call_func(i, ip)
            flag = flag and self.arr[ind]
        return flag
        
eps = float(input('eps> '))
calls  = int(input('calls> '))
cor = set()
s = BloomFilter(eps=eps, s=calls)

for i in range(calls):
    ip = tuple((randint(0,255) for _ in range(4)))
    cor.add(ip)
    s.insert(ip)
print(s.b)
print(s.k)
print(s.n)
cnt = 0
for i in range(calls):
    ip = tuple((randint(0, 255) for _ in range(4)))
    while ip in cor:
        ip = tuple((randint(0, 255) for _ in range(4)))
    if s.lookup(ip):
        cnt += 1
print(cnt)

    