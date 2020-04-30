from abc import ABC, abstractmethod


class AbstractWashingCar(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def washing_car(self):
        pass


class RisingCarWithWater(AbstractWashingCar):
    def __init__(self):
        super().__init__()

    def washing_car(self):
        print('zwykle mycie woda')


class CleaningTheCarWithAChemical(AbstractWashingCar):
    def __init__(self):
        super().__init__()

    def washing_car(self):
        print('mycie srodkiem chemicznym')


class CarWaxing(AbstractWashingCar):
    def __init__(self):
        super().__init__()

    def washing_car(self):
        print('woskowanie auta')

class WashingCarProgramForm(AbstractWashingCar):
    def __init__(self, program_name):
        super().__init__()
        self.program_name = program_name

    def washing_car(self):
        print('Właśnie wykonałeś program o nazwie: ' + self.program_name)
