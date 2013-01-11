import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.gui import Ui_Form
from ui.popup import Ui_Dialog
from lib.vklib import Vkontakte


class MyForm(QMainWindow):
    """Functions as a scope for the UI.
    """

    def __init__(self, parent=None):
        """Initialization of the main window.
        """

        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Setting signal connections
        self.ui.loginBtn.clicked.connect(self.login_dialog)
        self.ui.searchBtn.clicked.connect(self.search)
        self.ui.lineEdit.returnPressed.connect(self.search)
        self.ui.songList.itemActivated.connect(self.download_item)

        # Manage login status
        self.ui.statusLbl.setText("Not logged in")
        self.loggedIn = False

    def search(self):
        """Perform a search.
        """

        if self.loggedIn:
            self.ui.songList.clear()
            query = self.ui.lineEdit.text()             # Get search query
            search = self.vk.search(unicode(query))     # Perform search

            # Add search result to the QListWidget
            if search:
                for idx, x in enumerate(search):
                    s = " - "
                    listString = unicode(idx+1) + s + x['artist'] + s + x['title'] + s + x['duration']
                    dataString = x['artist'] + s + x['title'] + ".mp3"
                    item = QListWidgetItem(listString)

                    # Add download data to the list
                    data = [x['url'], dataString]
                    item.setData(Qt.UserRole, data)

                    # Add QWidgetListItems
                    self.ui.songList.addItem(item)
            else:
                pass

    def login_dialog(self):
        """Spawn the login modal.
        """

        self.dialog = QDialog()
        self.dialog.ui = Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.setAttribute(Qt.WA_DeleteOnClose)
        self.dialog.ui.login.clicked.connect(self.take_login)
        self.dialog.ui.password.setEchoMode(QLineEdit.Password)
        self.dialog.exec_()

    def take_login(self):
        """Performs a login on VK.com.
        """

        username = self.dialog.ui.username.text()
        password = self.dialog.ui.password.text()

        self.dialog.accept()    # Accept the form

        # Call the login function
        self.vk = Vkontakte(unicode(username), unicode(password))
        login = self.vk.login()

        if login:
            self.ui.statusLbl.setText("Logged in")
            self.loggedIn = True
        else:
            self.ui.statusLbl.setText("Wrong user/password")

    def download_item(self, item):
        """Download an mp3 from the list
        """

        url = item.data(Qt.UserRole).toPyObject()[0]
        name = item.data(Qt.UserRole).toPyObject()[1]

        # Initialize background download thread.
        self.workThread = WorkThread(url, name)
        self.connect(self.workThread, SIGNAL("download_status(QString)"), self.download_status)
        self.workThread.start()

    def download_status(self, status):
        """Handles signals from the download threads, and update the status.
        """
        self.ui.currentLbl.setText(status)


class WorkThread(QThread):
    """Downloader thread
    """

    def __init__(self, url, name):
        QThread.__init__(self)
        self.url = url
        self.name = name

    def run(self):
        self.emit(SIGNAL('download_status(QString)'), "Download Started...")

        myapp.vk.download(unicode(self.url), unicode(self.name))

        self.emit(SIGNAL('download_status(QString)'), "Download Finished")
        return

if __name__ == "__main__":
    directory = "downloads"        # Folder where the downloads will be stored
    if not os.path.exists(directory):
        os.makedirs(directory)

    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
