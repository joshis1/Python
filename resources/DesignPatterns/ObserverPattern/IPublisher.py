## This import abc is to make this class as abstract -- a pure virtual methods kind off
from abc import ABCMeta, abstractmethod

## This is the class name - IPublisher
class IPublisher(object):
## The metaclass will make this class as an abstract class
    __metaclass__ = ABCMeta
#Public methods - they don't start with either single underscore or double underscore
    @abstractmethod
     ## Remember the identation should be correct for the program to compile
    def registerObserver(self, observer):
     ## pass is like an empty body
     pass
    def unregisterObserver(self, observer):
     pass
    def setBaudRate(self,newBaudRate):
     pass
    def setAspectRatio(self, newAspectRatio):
     pass
    def setVolumeLevel(self,newVolume):
     pass
    # Protected method starts with one underscore
    def _notifyObserver(self):
        pass



