from math import log, e
from random import shuffle
import numpy as np
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
        #Погреность
        self.eps = eps
        #Количество обращений
        self.s = s
        self.b = int(log(eps, 0.5) / log(2))
        self.k = int(log(2) * self.b)
        self.n = self.s * self.b
        self.arr = BitSet(self.n)
        a = [x for x in range((self.k) * 4 + 1)]
        self.func = []
        for i in range(0, len(a) - 4, 4):
            self.func.append([a[i+j] for j in range(4)])
    def call_func(self, index, x):
        return sum(self.func[index][i] * x[i] for i in range(4)) % self.n
s = BloomFilter(eps = 0.02, s = 10)





'''
#Желаемая вероятность ошибки
eps = float(input('Input epsilon> '))
#Предполагаемое количество запросов
s = int(input('Amount of inserts> '))
#Бит на элемент
b = int(log(eps, 0.5) / log(2))
#Колиечество бит
n = b * s'''
