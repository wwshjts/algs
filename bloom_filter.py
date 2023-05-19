from math import log, e
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





'''
#Желаемая вероятность ошибки
eps = float(input('Input epsilon> '))
#Предполагаемое количество запросов
s = int(input('Amount of inserts> '))
#Бит на элемент
b = int(log(eps, 0.5) / log(2))
#Колиечество бит
n = b * s'''

arr = BitSet(7)
arr[0] = 1
arr[3] = 1
arr[5] = 1
arr.print