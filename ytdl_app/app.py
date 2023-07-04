import sys
import yt_dlp
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_Widget
from time import sleep

class DownloadThread(QThread):
    finished = pyqtSignal()

    def __init__(self, url, ytdl_options):
        super(DownloadThread, self).__init__()
        self.url = url
        self.ytdl_options = ytdl_options

    def run(self):
        try:
            with yt_dlp.YoutubeDL(self.ytdl_options) as ydl:
                ydl.download([self.url])
        except Exception as e:
            print(e)

        self.finished.emit()


class MainWindow(QMainWindow, Ui_Widget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
    @QtCore.pyqtSlot()
    def on_downloadButton_clicked(self):
        """
        Handler for download operation
        """
        url = self.lineEdit.text()
        audioOnly = self.audioCheckBox.isChecked()
        try:
            if audioOnly:
                ytdl_options = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192'
                    }],
                }
            else:
                ytdl_options = {
                    'format': 'best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4'
                    }],
                }

            ytdl_options['external_downloader_args'] = ['-o', 'pipe:', '--limit-rate', 'None']
            ytdl_options['progress_hooks'] = [self.p_hook]

            # Initializes a thread to perform the download to avoid freezing the ui
            self.download_thread = DownloadThread(url, ytdl_options)
            self.progressBar.show()
            self.change_input_state(True)
            self.download_thread.start()

        except Exception as e:
            print(e)
            

    def change_input_state(self, lock):
        """
        Changes all the input state to disabled to avoid additional operations by user
        """
        self.downloadButton.setDisabled(lock)
        self.lineEdit.setDisabled(lock)
        self.audioCheckBox.setDisabled(lock)
        

    def p_hook(self, d):
        """
        Tracks the download progress and updates the progress bar accordingly
        """
        download_percentage = (d['downloaded_bytes']/d['total_bytes']) *100
        self.progressBar.setProperty("value", download_percentage)
        if d['status'] == 'finished':
            sleep(3)
            self.change_input_state(False)
            self.lineEdit.clear()
            self.progressBar.hide()
            

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()