from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QWidget

from src.common.structs import Champion
from src.gui.ui_ChampionSlot import Ui_ChamionSlot


class ChampionSlot(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._ui = Ui_ChamionSlot()
        self._ui.setupUi(self)

    def resizeEvent(self, event: QResizeEvent) -> None:
        # force to always be a square
        new_size = min(event.size().height(), event.size().width())
        self.resize(new_size, new_size)
        event.accept()
        super().resizeEvent(event)

    def set_champion(self, champion: Champion) -> None:
        pass
