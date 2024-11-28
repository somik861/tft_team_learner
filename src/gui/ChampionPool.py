from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from src.gui.ui_ChampionPool import Ui_ChampionPool


class ChampionPool(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._ui = Ui_ChampionPool()
        self._ui.setupUi(self)
