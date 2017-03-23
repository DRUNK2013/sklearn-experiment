#!/usr/bin/python3
#coding=utf-8

#Createe by cane on 17-2-22

class Widget:
    def __init__(self, size = (40, 40)):
        self._size = size
    def getSize(self):
        return self._size
    def resize(self, width, height):
        self._size = (width, height)
    def dispose(self):
        pass
