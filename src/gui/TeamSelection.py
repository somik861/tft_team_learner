from PySide6.QtWidgets import QWidget

from src.gui.ui_TeamSelection import Ui_TeamSelection


class TeamSelection(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._ui = Ui_TeamSelection()
        self._ui.setupUi(self)
