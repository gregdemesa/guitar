#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        # TO-DO: implement this
        self.MAX_CAP = capacity
        self.buffer = [None]*capacity    
        self.size_ = 0 # number of elements currently in buffer     
        self._front = 0 # Index of oldest item
        self._rear = 0 #index of one beyond most recent item

    def size(self) -> int:
        return self.size_

    def is_empty(self) -> bool:
        return self.size_ == 0

    def is_full(self) -> bool:
        return self.size_== self.MAX_CAP

    def enqueue(self, x: float):
        if self.is_full():
            raise RingBufferFull("Cannot enqueue into a full buffer")
        self.buffer[self._rear] = x
        self._rear = (self._rear + 1) % self.MAX_CAP
        self.size_ += 1
        
    def dequeue(self) -> float:
        if self.is_empty():
            raise RingBufferEmpty("Cannot dequeue from an empty buffer")
        item = self.buffer[self._front]
        self._front = (self._front + 1) % self.MAX_CAP
        self.size_ -= 1
        return item
  

    def peek(self) -> float:
        if self.is_empty():
            raise RingBufferEmpty("Cannot peek into an empty buffer")
        return self.buffer[self._front]
        # TO-DO: implement this


class RingBufferFull(Exception):
    pass

class RingBufferEmpty(Exception):
    pass
