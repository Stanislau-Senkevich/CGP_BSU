import os

from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    os.environ['QT_QPA_PLATFORM'] = 'wayland'  # Set the platform
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())