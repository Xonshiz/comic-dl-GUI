if __name__ == '__main__':

    import sys
    import os
    from package import app
    from package.app import MainWindow
    from package import honcho
    from sites import gomanga
    from downloader import cookies_required
    from downloader import universal
    #current_directory = os.getcwd()
    #mw = MainWindow()


    sys.exit(app.run())