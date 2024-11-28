from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from src.gui.ui_MainFrame import Ui_MainFrame


class MainFrame(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._ui = Ui_MainFrame()
        self._ui.setupUi(self)

        self._ui.verticalLayout.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
