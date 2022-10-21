import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self.capacity)

    def __len__(self):
        
        return self._n

    def __getitem__(self, k):
        
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        return self._A[k] # Retrieve from array

    def __append__(self, obj):
        if self._n == self.capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):

        return (c * ctypes.py_object)()

data = [1 , 2 , 3] 

print(data.__getitem__(1))
print(data.__len__())
