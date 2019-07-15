from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit,
                             QInputDialog, QFileDialog, QMessageBox,
                             QGridLayout, QLabel, QPushButton, QFrame)

class AddTabDialog(QDialog):
    def __init__(self):
        super(AddTabDialog,self).__init__()

        name = QLabel("The name os the song:")
        self.name_le = QLineEdit();
        url = QLabel("The url of the tab page:")
        self.url_le = QLineEdit();

        okButton = QPushButton("OK")
        okButton.clicked.connect(self.OnOk)
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.OnCancel)

        mainLayout = QGridLayout()
        mainLayout.addWidget(name,          0, 0)
        mainLayout.addWidget(self.name_le,  0, 1)
        mainLayout.addWidget(okButton,      2, 1)
        mainLayout.addWidget(self.url_le,1, 1)
        mainLayout.addWidget(cancelButton,    2, 2)
        mainLayout.addWidget(url,          1, 0)
        mainLayout.setRowMinimumHeight(2, 40)
        mainLayout.addWidget(QLabel(), 3, 0)

        mainLayout.setSpacing(5)

        self.setLayout(mainLayout)

    def OnOk(self):
      self.result = self.name_le.text(), self.url_le.text()
      with open("tabs.txt", "a") as f:
        text = "{},{}".format(self.name_le.text(),self.url_le.text()) + "\n"
        f.write(text)

      self.close()    

    def OnCancel(self):
      self.close()