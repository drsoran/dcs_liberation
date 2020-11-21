"""Combo box for selecting a departure airfield."""
from typing import Iterable

from PySide2.QtWidgets import QComboBox
from dcs.unittype import FlyingType

from game import db
from game.theater.controlpoint import ControlPoint


class QArrivalAirfieldSelector(QComboBox):
    """A combo box for selecting a flight's arrival or divert airfield.

    The combo box will automatically be populated with all airfields the given
    aircraft type is able to land at.
    """

    def __init__(self, destinations: Iterable[ControlPoint],
                 aircraft: FlyingType, optional_text: str) -> None:
        super().__init__()
        self.destinations = list(destinations)
        self.aircraft = aircraft
        self.optional_text = optional_text
        self.rebuild_selector()
        self.setCurrentIndex(0)

    def change_aircraft(self, aircraft: FlyingType) -> None:
        if self.aircraft == aircraft:
            return
        self.aircraft = aircraft
        self.rebuild_selector()

    def rebuild_selector(self) -> None:
        self.clear()
        for destination in self.destinations:
            if destination.can_land(self.aircraft):
                self.addItem(destination.name, destination)
        self.model().sort(0)
        self.insertItem(0, self.optional_text, None)
        self.update()
