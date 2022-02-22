import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QMessageBox
from coredumputilframe  import Ui_coreDumpUtilFrame
from coredumpHelper  import FileDirHelper
from coredumpHelper import LabelHelper
from  coreDumpWindow import TabbedTerminal

class CoreDumpAttrib:
      __arch = 'MIPS'
      __sysRoot = 'NONE'
      __applicationExe = 'NONE'
      __coreFile = 'NONE'
      

      ''' get the Architecture type - by default, it is MIPS '''  
      def getArchName(self):
          return self. _arch
      '''  sets the Architecture type '''''''''

      def setArchName(self, archName):
          self.__arch = archName

      '''   get the SysRoot Path - it is directory path -- remember  '''
      def getSysRoot(self):
          return self.__sysRoot

      '''  sets the Sysroot Path '''
      def setSysRoot(self, sysRootPath):
           self.__sysRoot = sysRootPath


      '''  get the Application Exe  path and name ------'''
      def getApplicationExe(self):
          return self.__applicationExe

      '''  sets the Application Exe path and name -------'''
      def setApplicationExe(self, AppExe):
          self.__applicationExe = AppExe
    
      '''  get the core file name and path -----'''
      def getCoreFile(self):
          return self.__coreFile

      '''   set the core file name and path -----'''
      def setCoreFile(self, coreFile):   
         self. __coreFile = coreFile

      def validateGdbEnviron(self):

         if self.__sysRoot is 'NONE':
             msgBox = QMessageBox()
             msgBox.setText('SysRoot PATH Missing..')
             msgBox.setStandardButtons(QMessageBox.Ok)
             ret = msgBox.exec_();
             return False

         if self.__applicationExe is 'NONE':
             msgBox = QMessageBox()
             msgBox.setText('Set the Application -binary Path..')
             msgBox.setStandardButtons(QMessageBox.Ok)
             ret = msgBox.exec_();
             return False

         if self.__coreFile is 'NONE':
             msgBox = QMessageBox()
             msgBox.setText('Set the Core File  Path..')
             msgBox.setStandardButtons(QMessageBox.Ok)
             ret = msgBox.exec_();
             return False

         return True



   
def dbgLog(msg):
    # while making the actual product, comment the below line and uncomment pass
    print msg
    #pass 


class Main(QtGui.QMainWindow, Ui_coreDumpUtilFrame):
    def __init__(self):
       QtGui.QMainWindow.__init__(self)
       self.ui= Ui_coreDumpUtilFrame()
       self.ui.setupUi(self)
       self.coreAttrib = CoreDumpAttrib()
       ## added this line to do event driven -- function to be called when the button is clicked 
       self.ui.bSysRootBrowse.clicked.connect(self.ButtonbrowseSysRoot)
       self.ui.bApplicationBrowser.clicked.connect(self.browseApplicationExe)
       self.ui.lCoreFileBrowser.clicked.connect(self.browseCoreFile)
       self.ui.bgetBackTrace.clicked.connect(self.getbt)
  
 ## browse button event installer ########
  
    def ButtonbrowseSysRoot(self):
        dbgLog('browseSys Root pressed')
        fileHelper = FileDirHelper()
        sysRootDir = fileHelper.getDirPath("SysRootPath")
        self.coreAttrib.setSysRoot(sysRootDir)
        dbgLog (self.coreAttrib.getSysRoot())
        labelHandle = self.ui.lSysRootFilePath
        labelHelper = LabelHelper()
        ## This is to check if the string is empty or not
        if sysRootDir:
           labelHelper.setLabel(labelHandle,sysRootDir)
  
    def browseApplicationExe(self):
        dbgLog('browse Application Exe')
        fileHelper = FileDirHelper()
        appPathName = fileHelper.getFilePath("Select the Executable")
        self.coreAttrib.setApplicationExe(appPathName)
        dbgLog (self.coreAttrib.getApplicationExe())
        labelHandle = self.ui.lApplicationFilePath
        labelHelper = LabelHelper()
        ## This is to check if the string is empty or not
        if appPathName:
           labelHelper.setLabel(labelHandle,appPathName)
  

    def browseCoreFile(self):
       dbgLog('browse core file')
       fileHelper = FileDirHelper()
       corePathName = fileHelper.getFilePath("Select the CoreFile")
       self.coreAttrib.setCoreFile(corePathName)
       dbgLog (self.coreAttrib.getCoreFile())
       labelHandle = self.ui.lCorefileBrowser
       labelHelper = LabelHelper()
       ## This is to check if the string is empty or not
       if  corePathName:
           labelHelper.setLabel(labelHandle,corePathName)

   
    def getbt(self):
        dbgLog('get bt')
        if  self.coreAttrib.validateGdbEnviron() is True:
            coredumpParams = []
            coredumpParams.append(self.coreAttrib.getSysRoot())
            coredumpParams.append(self.coreAttrib.getApplicationExe())
            coredumpParams.append(self.coreAttrib.getCoreFile())
            self.win = TabbedTerminal(coredumpParams)
            self.win.show()

 #### browse button event installer completed ###########  


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
