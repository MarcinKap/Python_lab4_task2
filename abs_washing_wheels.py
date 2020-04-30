from abc import ABC, abstractmethod


class AbstractWashingWheels(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def washing_wheels(self, washing):
        pass


class RisingWheelsWithWater(AbstractWashingWheels):
    def __init__(self):
        super().__init__()

    def washing_wheels(self, washing):
        pass


class CleaningWheelsWithAChemical(AbstractWashingWheels):
    def __init__(self):
        super().__init__()

    def washing_wheels(self, washing):
        pass


class WashingWheelsProgramForm(AbstractWashingWheels):
    def __init__(self, program_name):
        super().__init__()
        self.program_name = program_name

    def washing_wheels(self):
        print('Właśnie wykonałeś program o nazwie: ' + self.program_name)