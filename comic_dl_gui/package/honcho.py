#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""This python module decides which URL should be assigned to which other module from the site package.
"""

from package.gui import Ui_MainWindow
from sites.gomanga import GomangaClass
from PyQt4 import QtCore, QtGui
#from downloader import universal, cookies_required
import urllib2


class Honcho(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Honcho, self).__init__(parent)
        self.setupUi(self)

    def url_checker(self, input_url, current_directory):
        self.textArea.textCursor().insertHtml(str(input_url))
        domain = urllib2.urlparse.urlparse(input_url).netloc

        if domain in ['mangafox.me']:
            #mangafox_Url_Check(input_url, current_directory)
            pass
        elif domain in ['yomanga.co']:
            #yomanga_Url_Check(input_url, current_directory)
            pass
        elif domain in ['gomanga.co']:
            GomangaClass().gomanga_Url_Check(input_url, current_directory)
            pass
        elif domain in ['bato.to']:
            # batoto_Url_Check(
            #     input_url,
            #     current_directory,
            #     User_Name,
            #     User_Password)
            pass
        elif domain in ['kissmanga.com']:
            #kissmanga_Url_Check(input_url, current_directory)
            pass
        elif domain in ['comic.naver.com']:
            #comic_naver_Url_Check(input_url, current_directory)
            pass
        elif domain in ['']:
            print 'You need to specify at least 1 URL. Please run : comic-dl -h'
        else:
            print "%s is unsupported at the moment. Please request on Github repository." % (domain)