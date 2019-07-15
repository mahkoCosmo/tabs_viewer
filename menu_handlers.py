from tkinter import messagebox
from add_tab_dialog import *
import webbrowser

def OnExit():
  exit()

def OnViewTabs():
  file = open("tabs.txt", "r") 
  for line in file: 
    name, url = line.split(',')
    webbrowser.open_new_tab(url)


def OnAddTab(parent):
  res = AddTabDialog(parent);
  print(res.result)