from pathlib import Path

from PySide6.QtGui import QPixmap

from src.common.structs import Champion


def load_champions(directory: Path) -> list[Champion]:
    out: list[Champion] = []
    for cost in directory.iterdir():
        if not cost.name.isdecimal():
            continue
        for champ in cost.iterdir():
            if not champ.is_file():
                continue
            logo = QPixmap(str(champ))
            if logo.isNull():
                continue
            out.append(Champion(name=champ.stem,
                       icon=logo, cost=int(cost.name)))

    return out
