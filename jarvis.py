from latest_garvis3 import Ui_jarvis_gui
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import sys
from contextlib import redirect_stdout
import io


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        import main
        main.task()
        Gui_Start.starttask()


startExe = MainThread()


class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_jarvis_gui()
        self.gui.setupUi(self)

        self.gui.Start_pushbutton.clicked.connect(self.starttask)
        self.gui.Quit_pushbutton.clicked.connect(self.closeTask)

        self.console_output = io.StringIO()
        sys.stdout = self.console_output
        sys.stderr = self.console_output

    def starttask(self):
        self.gui.movie1 = QtGui.QMovie(".\\design\\BG\\Iron_Template_1.gif")
        self.gui.gif_1.setMovie(self.gui.movie1)
        self.gui.movie1.start()

        self.gui.movie2 = QtGui.QMovie(".\\design\\extra gui\\live.gif")
        self.gui.gif_2.setMovie(self.gui.movie2)
        self.gui.movie2.start()

        self.gui.movie3 = QtGui.QMovie(".\\design\\extra gui\\__1.gif")
        self.gui.gif_3.setMovie(self.gui.movie3)
        self.gui.movie3.start()

        self.gui.movie4 = QtGui.QMovie(".\\design\\extra gui\\Earth_Template.gif")
        self.gui.gif_4.setMovie(self.gui.movie4)
        self.gui.movie4.start()

        self.gui.movie5 = QtGui.QMovie(".\\design\\extra gui\\initial.gif")
        self.gui.gif_5.setMovie(self.gui.movie5)
        self.gui.movie5.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(999)

        startExe.start()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_console)
        self.timer.start(100)

    def update_console(self):
        console_output = self.console_output.getvalue()

        if console_output != self.gui.textBrowser.toPlainText():
            self.gui.textBrowser.setPlainText(console_output)
            self.gui.textBrowser.moveCursor(QTextCursor.End)

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        lable_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate)
        self.gui.dis_time.setText(lable_time)
        self.gui.dis_date.setText(lable_date)



    def closeTask(self):
        self.close()


GuiApp = QApplication(sys.argv)
jarvisGui = Gui_Start()
jarvisGui.show()
sys.exit(GuiApp.exec())
