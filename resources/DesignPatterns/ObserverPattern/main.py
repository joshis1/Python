# Create the Subsrcibers now

from UpdateManager import UpdateManager
from UpdateReceiver import UpdateReceiver


## if the name - special variable set by the python is __main__ then execute the remaining functions

if __name__ == "__main__":
    AV_UpdateMgr = UpdateManager()
    AV_UpdateReceiver = UpdateReceiver(AV_UpdateMgr)
    NW_UpdateReceiver = UpdateReceiver(AV_UpdateMgr)
    AV_UpdateMgr.setBaudRate(1000)
    AV_UpdateMgr.setAspectRatio(43)
    AV_UpdateMgr.setVolumeLevel(100)
    AV_UpdateMgr.unregisterObserver(AV_UpdateReceiver)
    AV_UpdateMgr.setVolumeLevel(20)



