from ISubscriber import ISubsrciber
from UpdateManager import UpdateManager
import inspect

class UpdateReceiver(ISubsrciber):
    # Static variable
    updateReceiverTracker = 0
    def __init__(self,updateManager):
        self.__m_baudRate__ = 0
        self.__m_volumeLevel__ = 0
        self.__m_receiverNumber__ = 0
        self.__m_updateManager__ = updateManager

        self.__m_updateManager__.registerObserver(self)
        self.__m_receiverNumber__ = UpdateReceiver.updateReceiverTracker
        ## Unary operator is different in Python
        UpdateReceiver.updateReceiverTracker += 1

    def update(self, baudRate,AspectRatio, VolumeLevel):
         __m_baudRate__ = baudRate
         __m_volumeLevel__ = AspectRatio
         __m_receiverNumber__ = VolumeLevel
         print (inspect.stack()[0][3])
         print ("The following client number : " + str(self.__m_receiverNumber__) + " got the update ")
         print ("The baudRate is " + str(baudRate))
         print ("The AspectRatio is " + str(AspectRatio))
         print ("The VolumeLevel is "+ str(VolumeLevel))
