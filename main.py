#import os
#os.system('/bin/bash --rcfile /home/michel/Dev/python/tabsviewer/tabsViewer.sh')
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, qApp, QApplication, QVBoxLayout,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView , QWebEnginePage, QWebEngineSettings
from PyQt5.QtNetwork import *
from add_tab_dialog import *



class TabViewer(QMainWindow):
  currentIdx = 0
  def __init__(self):
      super().__init__()
      
      self.initUI()
      
  def OnViewTabs(self):
    self.webView = QWebEngineView(self)
    self.setCentralWidget(self.webView)

    self.webView.settings().setAttribute(QWebEngineSettings.WebGLEnabled, True)
    self.webView.settings().setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled, True)

    self.tabUrls = open("tabs.txt", "r").readlines()

    self.DisplayTab()
    self.currentIdx +=1

  def OnAddTab(self):
    addTab = AddTabDialog()
    result = addTab.exec_()

  def initUI(self):
    menubar = self.menuBar()
    fileMenu = menubar.addMenu('&File')
    exitAct = QAction(QIcon('exit.png'), '&Exit', self)        
    exitAct.setShortcut('Ctrl+Q')
    exitAct.setStatusTip('Exit application')
    exitAct.triggered.connect(qApp.quit)      
    fileMenu.addAction(exitAct)

    tabsMenu = menubar.addMenu('&Tabs')        
    viewTabsAct = QAction('View tabs', self)
    viewTabsAct.setShortcut('Ctrl+V')
    viewTabsAct.triggered.connect(self.OnViewTabs)
    tabsMenu.addAction(viewTabsAct)

    addTabAct = QAction('Add tab', self)
    addTabAct.setShortcut('Ctrl+A')
    addTabAct.triggered.connect(self.OnAddTab)
    tabsMenu.addAction(addTabAct)        

    self.statusBar().showMessage('Ready')
    
    self.setGeometry(600, 300, 900, 600)
    self.setWindowTitle('TabsViewer')    
    self.show()

  def DisplayTab(self):
    name, url = self.tabUrls[self.currentIdx].split(',')
    self.webView.load(QtCore.QUrl(url))
    self.webView.show()

  def keyPressEvent(self, e):
    if(e.modifiers() == QtCore.Qt.ControlModifier):
      if(e.key() == QtCore.Qt.Key_N):
        if self.currentIdx == len(self.tabUrls) :
          QMessageBox.warning(self, '', 'End list reached')
        else:
          self.next = False
          self.currentIdx += 1
          self.DisplayTab()          
      if(e.key() == QtCore.Qt.Key_P):
        if self.currentIdx == 0:
          QMessageBox.warning(self, '', 'Beginning list reached')
        else:
          self.currentIdx -= 1
          self.DisplayTab()         

if __name__ == '__main__':
  app = QApplication(sys.argv)
  tv = TabViewer()
  sys.exit(app.exec_())