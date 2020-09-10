from IPublisher import IPublisher
from ISubscriber import ISubsrciber

import inspect

class UpdateManager(IPublisher):
    ## There are no constructors in python
    ## The init is the function that is first called when the object is created
    def __init__(self):
        self.__subscribers__ = []
        self.__baudRate__ = 0
        self.__aspectRatio__ = 0
        self.__volumeLevel__ = 0

    def registerObserver(self, subscriber):
        if not subscriber in self.__subscribers__:
            self.__subscribers__.append(subscriber)

    def unregisterObserver(self, subscriber):
        print (inspect.stack()[0][3])
        if subscriber in self.__subscribers__:
            self.__subscribers__.remove(subscriber)

    def setBaudRate(self, newBaudRate):
        self.__baudRate__ = newBaudRate
        self._notifyObserver()

    def setAspectRatio(self, newAspectRatio):
         self.__aspectRatio__ = newAspectRatio
         self._notifyObserver()

    def setVolumeLevel(self, newVolume):
        print (inspect.stack()[0][3])
        self.__volumeLevel__ = newVolume;
        self._notifyObserver()


     # Protected _notifyObserver
    def _notifyObserver(self):
       for subsriber in self.__subscribers__ :
        subsriber.update( self.__baudRate__, self.__aspectRatio__,self.__volumeLevel__)

