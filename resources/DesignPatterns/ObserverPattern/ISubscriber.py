# a metaclass is a blueprint for the creation of a class.

#http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

#https://pymotw.com/2/abc/

from abc import ABCMeta,abstractmethod
class ISubsrciber(object):
    __metaclass__ = ABCMeta

def update(baudRate,AspectRatio,VolumeLevel):
    pass
