from dataclasses import dataclass

from PySide6.QtGui import QPixmap


@dataclass(frozen=True, eq=True, order=True)
class Champion:
    name: str
    cost: int
    icon: QPixmap
