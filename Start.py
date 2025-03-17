import sys
from PyQt5.QtWidgets import QApplication
from TPanel import TPanel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TPanel()
    window.show()
    sys.exit(app.exec_())
