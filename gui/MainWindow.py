from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Widget(object):
    def setupUi(self, Widget):
        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Get root directory
        root_directory = os.path.dirname(current_directory)

        # Define main widget
        Widget.setObjectName("Widget")
        Widget.resize(1080, 720)
        Widget.setWindowTitle('YTDL App')
        Widget.setMinimumSize(QtCore.QSize(1080, 720))
        Widget.setMaximumSize(QtCore.QSize(1080, 720))
        font = QtGui.QFont()
        font.setPointSize(12)
        Widget.setFont(font)
        
        # Define Label for url input
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(190, 210, 91, 16))
        self.label.setObjectName("label")
        self.label.setText('Video URL')
        
        # Define input line box for video url
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 240, 721, 41))
        self.lineEdit.setMinimumSize(QtCore.QSize(700, 0))
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setPlaceholderText("e.g. https://www.youtube.com/watch?=abcde")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        
        # Define download button
        self.downloadButton = QtWidgets.QPushButton(Widget)
        self.downloadButton.setGeometry(QtCore.QRect(970, 610, 75, 75))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(root_directory, 'assets', 'download.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon)
        self.downloadButton.setIconSize(QtCore.QSize(50, 50))
        self.downloadButton.setObjectName("downloadButton")

        # Define checkbox
        self.audioCheckBox = QtWidgets.QCheckBox(Widget)
        self.audioCheckBox.setGeometry(QtCore.QRect(190, 310, 121, 22))
        self.audioCheckBox.setObjectName("audioCheckBox")
        self.audioCheckBox.setText('Audio Only?')

        # Define progress bar
        self.progressBar = QtWidgets.QProgressBar(Widget)
        self.progressBar.setGeometry(QtCore.QRect(190, 440, 721, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()

        QtCore.QMetaObject.connectSlotsByName(Widget)

    
        