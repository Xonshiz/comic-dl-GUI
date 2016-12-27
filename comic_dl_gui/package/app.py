import sys
import os
from PyQt4 import QtCore, QtGui
from package.gui import Ui_MainWindow
from package.honcho import Honcho
import webbrowser


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.downloadButton.clicked.connect(self.download_click)
        self.actionReport_Issue.triggered.connect(self.report_issue)
        self.actionReport_Issue_2.triggered.connect(self.report_issue)

    def report_issue(self):
        webbrowser.open('https://github.com/Xonshiz/comic-dl-GUI/issues/new')

    def download_click(self):
        # self.textArea.textCursor().insertHtml('Hello World!')
        url = str(self.urlInputField.text())
        current_directory = os.getcwd()
        Honcho().url_checker(url, current_directory)

    def file_skipping_print(self, filename):
        print "At : ",filename
        self.textArea.textCursor().insertHtml('[Comic-dl] File Exist! Skipping %s' % filename)
        print 'Definitely I did not'

    def file_download_print(self, filename):
        self.textArea.textCursor().insertHtml('[Comic-dl] Downloading : %s' % filename)

    def info_printer(self, series_name, chapter_number):
        main_info = ('{:^80}'.format('%s - %s') % (series_name, chapter_number))
        deco = ('{:^80}'.format('=====================================================================\n'))
        self.textArea.textCursor().insertHtml('\n%s\n%s\n' % (main_info, deco))


def run():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec_()

if __name__ == "__main__":
    import sys
    run()
