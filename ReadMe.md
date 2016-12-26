# Comic-dl GUI

Comic-dl GUI is a Graphical User Interface for my [comic-dl project (CLI)](https://github.com/Xonshiz/comic-dl). Since I just started learning about classes and GUI for Python, this project has loads of tons of problems and hence, it is partially broken.

## The problem :

This script right here works, it downloads the comics from currently supported gomanga.co website and downloads a single chapter. However, it doesn't print out anything on the screen of the GUI iteself, rather it goes down and shows the info in the CLI of this program and I kinda got stuck at it and I need help sorting this out. So, anyone who knows how to get rid of the problem, please pull and fix and TEACH ME!

I went on and asked on [StackOverflow to get a head start and this gentleman ekhumoro pointed me a direction](http://stackoverflow.com/a/41269933/2408212). And I followed him and it sort of worked, but... I got stuck at certain thing. Read below to understand.

So, a little summary of what ACTUALLY is going down here is below :

So, I created the GUI using the `Qt Designer` (gui.py has the code) and am inheriting the main UI created by that in the `app.py` file in the `package` directory, as mentioned in the answer (Directory structure actually makes sense). Below is explanation of which directory has what.

**[`downloader`]() :** Contians 2 py files which serve as a downloader. You send the file name, directory address, cookies and stuff in these and they'll download from the source link.

**[`package`]() :** Contians all the files related to UI (generated by Qt Designer), and app module, which inherits the main gui.py file. `honcho.py` file is the file that selects which url belong to which website and sends it to the corresponding site's class. For now, we only have gomanga.co (1 at a time people, 1 at a time).

**[`package\gui_images`]() :** Currently an empty folder. In future, it'll contain the images that'll be eventually visible in the UI itslef.

**[`sites`]() :** The very very important directory. It contains all the site's code. I mean, this directory contains all the classes for seperate sites to download from them.

This ends the quest for directory structure. And you need to start the `main.py` to start the application. Now, let's talk what is actuall happening here and where the problem is occurring.

So, we start the `main.py` file and it calls the `app.py` from the [package]() directory. We enter the **[`URL`](http://gomanga.co/reader/read/free-draw/en/0/9/)** in the QLineEdit and click on that extra wide download button.

As soon as we click the button, we trigger an action in the `app.py` and it calls the `download_click` method ([line 12 in the app.py](https://github.com/Xonshiz/comic-dl-GUI/blob/master/comic_dl_gui/package/app.py#L12)). Now, the URL that the app got is sent to a method `url_checker` of the `honcho.py` file. This method evaluates the URL and send it to `gomanga.py` file's `gomanga_Url_Check` method (which is in the [sites]() directory).  Now, this is working, because the URL is being passed to this level and the URL is visited and evaluated by the script. Now, to download the images from the Direct Links grabbed by the script, we will call the `main` method of `cookies_required` from the [downloader]() directory on [line 79](https://github.com/Xonshiz/comic-dl-GUI/blob/master/comic_dl_gui/sites/gomanga.py#L79). Even this is working just fine.

Now, skip to the [line 38 of the cookies_required.py file](https://github.com/Xonshiz/comic-dl-GUI/blob/master/comic_dl_gui/downloader/cookies_required.py#L38). Here, we're calling the `[file_skipping_print](https://github.com/Xonshiz/comic-dl-GUI/blob/master/comic_dl_gui/downloader/cookies_required.py#L38)` method or `[file_download_print](https://github.com/Xonshiz/comic-dl-GUI/blob/master/comic_dl_gui/downloader/cookies_required.py#L46)` of `MainWindow` class from the `[app.py]`(https://github.com/Xonshiz/comic-dl-GUI/blob/master/comic_dl_gui/package/app.py). I've added comment after each and every line of code in these areas to see it on my command line. But, this all is working perfectly fine.

Now, we're sending the data along with this to be printed on the QTextBrowser of the GUI. Check the [line 20 of app.py](https://github.com/Xonshiz/comic-dl-GUI/blob/master/comic_dl_gui/package/app.py#L20). Now, this all should work just fine. I mean, it is downloading the images, it is doing it all in a loop, so the line should show up on the QTextBrowser. But, it is not happening.

This IS ery complex and I hope the explanation somewhat helped. I am not sure what's happening and what's not. Need help fixing this issue.