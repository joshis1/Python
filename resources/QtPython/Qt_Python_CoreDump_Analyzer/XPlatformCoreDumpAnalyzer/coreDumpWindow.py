#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from PyQt4.QtGui import QMessageBox

from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QApplication, QTabWidget, QPushButton

from pyqterm import TerminalWidget
from pyqterm.procinfo import ProcessInfo
from subprocess import call


class TabbedTerminal(QTabWidget):

    def __init__(self,params, parent=None):
        super(TabbedTerminal, self).__init__(parent)
        self.proc_info = ProcessInfo()
        self.gdbparams = params
        self.setTabPosition(QTabWidget.South)
        self._new_button = QPushButton(self)
        self._new_button.setText("New")
        self._new_button.clicked.connect(self.new_terminal)
        self.setCornerWidget(self._new_button)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setWindowTitle("Terminal")
        self.resize(800, 600)
        self._terms = []
        self.tabCloseRequested[int].connect(self._on_close_request)
        self.currentChanged[int].connect(self._on_current_changed)
        QTimer.singleShot(0, self.new_terminal)  # create lazy on idle
        self.startTimer(1000)

    def _on_close_request(self, idx):
        term = self.widget(idx)
        term.stop()

    def _on_current_changed(self, idx):
        term = self.widget(idx)
        self.term = term
        self._update_title(term)

    def new_terminal(self):
        term = TerminalWidget(self)
        term.session_closed.connect(self._on_session_closed)
        self.addTab(term, "Terminal")
        self._terms.append(term)
        self.setCurrentWidget(term)
        term.setFocus()
        self.terminal = term
        filename = str(self.gdbparams[2])
        print filename
        extension = os.path.splitext(filename)[1]
        print extension
        if extension == ".lzo":
           print "the core is lzo"
           call(["lzop", "-fd", filename, "-o","test.core"])
       
        
        term.send("rm -f bt.txt \n")
        gdbpath = str("/usr/bin/mips-csr3.0-gdb -x bt.txt") + str(" \n")  
        #gdbpath = str(self.gdbparams[0]) + "/usr/bin/gdb "
        print gdbpath
        #cmd = str(gdbpath + str(self.gdbparams[1]) + " test.core \n")
        #print cmd
        ## start gdb 
        term.send(gdbpath)
        term.send("set logging on bt.txt \n")
        solibpathcmd = str("set solib-absolute-prefix ") + str(self.gdbparams[0]) + str(" \n")
        term.send(solibpathcmd)
        sysrootpathcmd = str("set sysroot ") + str(self.gdbparams[0]) + str(" \n")
        term.send(sysrootpathcmd)
        filepathcmd = str("file ") + str(self.gdbparams[1]) + str(" \n")
        term.send(filepathcmd)
        corefilecmd = str("core-file ") + "test.core" + str(" \n")
        term.send(corefilecmd)
        #term.send(cmd)
        term.send("bt full  \n")
        msgBox = QMessageBox()
        workingDir = os.getcwd() 
        btMsg = str("Check the backtrace stored in bt.txt at ") + str(workingDir) 
        msgBox.setText(btMsg)
        msgBox.setStandardButtons(QMessageBox.Ok)
        ret = msgBox.exec_();
        #self.term.send("ls -l ")
        #print (self.gdbparams[1])
        #term.send(self.gdbparams[0])
        #term.send(self.gdbparams[1])

    def timerEvent(self, event):
        self._update_title(self.currentWidget())

    def _update_title(self, term):
        if term is None:
            self.setWindowTitle("Terminal")
            return
        idx = self.indexOf(term)
        pid = term.pid()
        self.proc_info.update()
        child_pids = [pid] + self.proc_info.all_children(pid)
        for pid in reversed(child_pids):
            cwd = self.proc_info.cwd(pid)
            if cwd:
                break
        try:
            cmd = self.proc_info.commands[pid]
            title = "%s: %s" % (os.path.basename(cwd), cmd)
        except:
            title = "Terminal"
        self.setTabText(idx, title)
        self.setWindowTitle(title)

    def _on_session_closed(self):
        term = self.sender()
        try:
            self._terms.remove(term)
        except:
            pass
        self.removeTab(self.indexOf(term))
        widget = self.currentWidget()
        if widget:
            widget.setFocus()
        if self.count() == 0:
            self.new_terminal()

'''
if __name__ == "__main__":
    templist = []
    templist.append("ls -l \n")
    templist.append("date \n")
    app = QApplication(sys.argv)
    win = TabbedTerminal(templist)
    win.show()
    app.exec_()
'''
