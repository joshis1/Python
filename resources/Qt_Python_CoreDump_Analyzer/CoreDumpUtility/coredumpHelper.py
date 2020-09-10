import sys
import textwrap
from PyQt4 import QtGui
from coredumputilframe  import Ui_coreDumpUtilFrame


####### This is to get the Directory Path #############################


class FileDirHelper:
      
      def getDirPath(self, infoMsg):
          return QtGui.QFileDialog.getExistingDirectory(None,infoMsg)


      def getFilePath(self,infoMsg):
         return QtGui.QFileDialog.getOpenFileName(None,infoMsg)
  
class LabelHelper:
      def setLabel(self, lHandle, labelText):
          #print textwrap.fill(labelText,20)
          lHandle.setText(labelText[0:30])


          


