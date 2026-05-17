from abc import \
    ABC, \
    abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget:int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def get_sponsors(self):
        pass

    @property
    @abstractmethod
    def get_expenses(self):
        pass

    def calculate_revenue_after_race(self,race_pos: int):
        revenue = 0
        sponsors = self.get_sponsors
        for sponsor in sponsors.values():
            for key, value in sponsor.items():
                if key >= race_pos:
                    revenue += value
                    break
        revenue -= self.get_expenses
        self.__budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget {self.budget}$"
