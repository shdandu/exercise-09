"""File to define River class."""

from __future__ import annotations

__author__ = "730705811"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

        return None

    def bears_eating(self):
        """Removes fish for eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Removes bears with negative hunger score."""
        for bear in self.bears:
            if bear.hunger_score < 0:
                self.bears.remove(bear)
        return None

    def check_ages(self):
        """Removes old fish and bears."""
        for fish in self.fish:
            if fish.age > 3:
                self.fish.remove(fish)
        for bear in self.bears:
            if bear.age > 5:
                self.bears.remove(bear)
        return None

    def repopulate_fish(self):
        """Reproduction of fish."""
        start: int = 0
        new_fish: int = int(len(self.fish) / 2) * 4
        while start < new_fish:
            self.fish.append(Fish())
            start += 1
        return None

    def repopulate_bears(self):
        """Reproduction of bears."""
        start: int = 0
        new_bears: int = int(len(self.bears) / 2)
        while start < new_bears:
            self.bears.append(Bear())
            start += 1
        return None

    def remove_fish(self, amount: int):
        "Death of fish."
        start: int = 0
        while start < amount:
            self.fish.pop(0)
            start += 1

        return None

    def __str__(self) -> str:
        """Returns inputs."""
        return f"""~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}"""

    def __add__(self, other_riv: River) -> River:
        """Adds together populations."""
        total_fish = len(self.fish) + len(other_riv.fish)
        total_bears = len(self.bears) + len(other_riv.bears)
        return River(total_fish, total_bears)

    def __mul__(self, factor: int) -> River:
        """Multiplies populations."""
        total_fish = len(self.fish) * factor
        total_bears = len(self.bears) * factor
        return River(total_fish, total_bears)

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        """Simulate 7 days of life in the river."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
