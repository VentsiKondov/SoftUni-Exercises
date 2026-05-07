from project.computer_types import \
    computer
from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import \
    DesktopComputer
from project.computer_types.laptop import Laptop

class ComputerStoreApp:
    VALID_COMPUTERS = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}
    def __init__(self):
        self.warehouse:list = []
        self.profits:int = 0


    def build_computer(self,type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTERS:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        comp = self.VALID_COMPUTERS[type_computer](manufacturer,model)
        self.warehouse.append(comp)
        return comp.configure_computer(processor, ram)

    def sell_computer(self,client_budget: int, wanted_processor: str, wanted_ram: int):
        wanted_computer = next((c for c in self.warehouse if c.processor == wanted_processor and c.price <= client_budget and c.ram >= wanted_ram), None)
        if wanted_computer is None:
            raise Exception(f"Sorry, we don't have a computer for you.")
        self.profits += abs(wanted_computer.price - client_budget)
        self.warehouse.remove(wanted_computer)
        return f"{repr(wanted_computer)} sold for {client_budget}$."

computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
