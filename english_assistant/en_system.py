import sys
from PyQt5.QtWidgets import QApplication, QWidget
import class_name


class english_system(QWidget, class_name.Ui_Form_search):
    def __init__(self, parent=None):
        super(english_system, self).__init__(parent)
        wnd = self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    w = english_system()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
