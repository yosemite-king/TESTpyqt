import sys
from PyQt5 import QtWidgets
from package.grid import GridExample


def run():
    app = QtWidgets.QApplication(sys.argv)
    grid = GridExample()
    return app.exec()