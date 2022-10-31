class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):

        # 1  Return (But not remove) the element at the top of the stack
        # 2. Raise exception if the stack is empty

        if self.is_empty():
            raise Empty("is empty")
        return self._data[-1]             # Last item in the list


    def pop(self):

        # 1. Remove and return the element at the top of the stack
        # 2. Raise exception if its empty



        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

        
obj1 = ArrayStack()

obj1._data = [1 ,2 ,3, 4] 

print(obj1.is_empty())
print(obj1.__len__())
print(obj1.top())
print(obj1.pop())

