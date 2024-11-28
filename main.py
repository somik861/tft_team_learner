import sys

from PySide6.QtWidgets import QApplication

from src.gui.MainFrame import MainFrame


def main() -> int:
    app = QApplication()
    mf = MainFrame()
    mf.show()
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
