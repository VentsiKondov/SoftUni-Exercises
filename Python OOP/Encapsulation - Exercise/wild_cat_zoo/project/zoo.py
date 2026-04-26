class Zoo:
    def __init__(self, name:str ,budget: int, animal_capacity:int, worker_capacity:int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if  self.__budget - price < 0:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"
    def fire_worker(self, worker_name):
        try:
            current_worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(current_worker)
        return f"{worker_name} fired successfully"
    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)
        if salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
    def tend_animals(self):
        total_money_for_care = sum([a.money_for_care for a in self.animals])
        if total_money_for_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self,amount:int):
        self.__budget += amount
    def animals_status(self):
        info = {"Cheetah": [], "Tiger": [], "Lion": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.animals]
        output = [f"You have {len(info['Cheetah']) + len(info['Tiger']) + len(info['Lion'])} animals",
                  f"----- {len(info['Lion'])} Lions:", *info['Lion'],
                  f"----- {len(info['Tiger'])} Tigers:", *info['Tiger'],
                 f"----- {len(info['Cheetah'])} Cheetahs:", *info['Cheetah']]
        return "\n".join(output)
    def workers_status(self):
        info = {"Vet": [], "Keeper": [], "Caretaker": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]
        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:", *info["Keeper"],
            f'----- {len(info["Caretaker"])} Caretakers:',*info["Caretaker"],
            f'----- {len(info["Vet"])} Vets:',*info["Vet"],
        ]
        return "\n".join(result)



