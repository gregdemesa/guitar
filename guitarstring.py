#!/usr/bin/env python3
from ringbuffer import *
import random
from math import ceil

class GuitarString:
    def __init__(self, frequency: float):
      
        self.capacity = int(ceil(44100/frequency)) # TO-DO: compute the max capacity of the ring buffer based on the frequency
        self.buffer =  RingBuffer(self.capacity)  # TO-DO: construct the ring buffer object
        # for _ in range(self.capacity):
        #     self.buffer.enqueue(0.0)
        self.tick_count = 0
    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        # Set the buffer to white noise by replacing its contents with random values
        while not self.buffer.is_empty():
            self.buffer.dequeue()
        for _ in range(self.capacity):
            self.buffer.enqueue(random.uniform(-0.5, 0.5))
        # TO-DO: implement this

    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        if not self.buffer.is_empty():
            front = self.buffer.dequeue()
            next_sample = 0.996*0.5* (front + self.buffer.peek())
            self.buffer.enqueue(next_sample)
            # TO-DO: implement this
            self.tick_count += 1

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        return self.buffer.peek()
        # TO-DO: implement this

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        return self.tick_count
        # TO-DO: implement this
