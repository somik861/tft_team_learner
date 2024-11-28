from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from src.common.structs import Champion
from src.gui.CostPool import CostPool
from src.gui.ui_ChampionPool import Ui_ChampionPool


class ChampionPool(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._ui = Ui_ChampionPool()
        self._ui.setupUi(self)

        self._champions: list[Champion] = []

    def add_champion(self, champion: Champion) -> None:
        assert self._champions.count(champion) == 0

        self._champions.append(champion)

    def _refresh_champions(self) -> None:
        pools: dict[int, list[Champion]] = {}

        for champ in sorted(self._champions):
            if champ.cost not in pools:
                pools[champ.cost] = []

            pools[champ.cost].append(champ)

        for cost, champs in pools.items():
            pool = CostPool()
