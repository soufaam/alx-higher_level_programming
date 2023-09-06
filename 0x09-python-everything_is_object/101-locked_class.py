#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

    def __init__(self, fn=None):
        self.first_name = fn
