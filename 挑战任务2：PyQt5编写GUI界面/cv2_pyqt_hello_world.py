# ex2tron's blog:
# http://ex2tron.wang

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Hello World!')
    window.show()

    sys.exit(app.exec_())
