from collections import deque
from time import time
import numpy as np
import sys

# result:
# (faster) collection.deque.popleft > numpy.delete > list.pop (slower)
class Queue:
    def __init__(self, data):
        self.data = data
    def remove_first(self):
        raise NotImplementedError
class ListQueue(Queue):
    def __init__(self, data):
        super().__init__(data)
    def remove_first(self):
        return self.data.pop(0)
class Deque(Queue):
    def __init__(self, data):
        super().__init__(data)
    def remove_first(self):
        return self.data.popleft()
class NumpyQueue(Queue):
    def __init__(self, data):
        super().__init__(data)
    def remove_first(self):
        first = self.data[0]
        self.data = np.delete(self.data, 0)
        return first
class IterQueue(Queue):
    def __init__(self, data):
        super().__init__(data)
    def remove_first(self):
        return self.data.__next__()

# deque と list で deque の方が高速か？
# イテレータは？numpyは？
ls  = ListQueue(list(range(1000**2*100)))
deq = Deque(deque(range(1000**2)))
npq = NumpyQueue(np.array(range(1000**2)))
itr = NumpyQueue(range(1000**2))

def trial(queue):
    start = time()
    num = queue.remove_first()
    print(time()-start)
    return num

trial(ls)
trial(deq)
trial(npq)
trial(itr)

q = deque(range(1000**2))
sys.getsizeof(q)

sys.getsizeof(range(1000**2))