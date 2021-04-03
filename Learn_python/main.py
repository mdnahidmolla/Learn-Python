# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(100, 50, 621, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.thoughts_2 = QtWidgets.QLabel(self.tab)
        self.thoughts_2.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.thoughts_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(24, 255, 116);\n"
"color: rgb(255, 0, 0);")
        self.thoughts_2.setObjectName("thoughts_2")
        self.thoughts = QtWidgets.QLineEdit(self.tab)
        self.thoughts.setGeometry(QtCore.QRect(10, 60, 591, 41))
        self.thoughts.setObjectName("thoughts")
        self.addb = QtWidgets.QPushButton(self.tab)
        self.addb.setGeometry(QtCore.QRect(20, 110, 581, 41))
        self.addb.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.addb.setObjectName("addb")
        self.allthoughts = QtWidgets.QLabel(self.tab)
        self.allthoughts.setGeometry(QtCore.QRect(30, 180, 141, 41))
        self.allthoughts.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.allthoughts.setObjectName("allthoughts")
        self.all = QtWidgets.QListWidget(self.tab)
        self.all.setGeometry(QtCore.QRect(-10, 230, 621, 221))
        self.all.setObjectName("all")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 61, 21))
        self.label_4.setObjectName("label_4")
        self.myname = QtWidgets.QLineEdit(self.tab_2)
        self.myname.setGeometry(QtCore.QRect(120, 30, 371, 41))
        self.myname.setObjectName("myname")
        self.mycontact = QtWidgets.QLineEdit(self.tab_2)
        self.mycontact.setGeometry(QtCore.QRect(130, 150, 371, 41))
        self.mycontact.setObjectName("mycontact")
        self.mypassword = QtWidgets.QLineEdit(self.tab_2)
        self.mypassword.setGeometry(QtCore.QRect(130, 90, 371, 41))
        self.mypassword.setObjectName("mypassword")
        self.myemail = QtWidgets.QLineEdit(self.tab_2)
        self.myemail.setGeometry(QtCore.QRect(130, 200, 371, 41))
        self.myemail.setObjectName("myemail")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.thoughts_2.setText(_translate("MainWindow", "thought"))
        self.addb.setText(_translate("MainWindow", "add thought"))
        self.allthoughts.setText(_translate("MainWindow", "all thoughts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "welcome"))
        self.label.setText(_translate("MainWindow", "My namel"))
        self.label_2.setText(_translate("MainWindow", "My password"))
        self.label_3.setText(_translate("MainWindow", "contact"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "my profile"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
