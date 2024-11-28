from itertools import batched

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QWidget

from src.common.structs import Champion
from src.gui.ChampionSlot import ChampionSlot
from src.gui.ui_CostPool import Ui_CostPool


class CostPool(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._ui = Ui_CostPool()
        self._ui.setupUi(self)

        self._slots: list[ChampionSlot] = []
        self._hboxes: list[QHBoxLayout] = []

    def set_cost(self, value: int) -> None:
        self._ui.costLabel.setText(f'{value}')

    def set_champions(self, champions: list[Champion]) -> None:
        # TODO: delete previous widgets

        for row_champs in batched(champions, n=5):
            hbox = QHBoxLayout()
            for champ in row_champs:
                slot = ChampionSlot()
                slot.set_champion(champ)
                hbox.addWidget(slot)
                self._slots.append(slot)
            self._hboxes.append(hbox)
            self._ui.verticalLayout.addLayout(hbox)
