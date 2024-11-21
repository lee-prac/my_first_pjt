class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f'{self.year} {self.make} {self.year}'

    def stop_engine(self):
        return f'{self.year} {self.make} {self.year}'


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def open_trunk(self):
        print('open trunk')
        return f'{self.year} {self.make} {self.year} {self.num_doors}'