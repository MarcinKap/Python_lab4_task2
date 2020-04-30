import sys
import time

from numpy.ma.bench import timer

from abs_washing_car import CarWaxing, CleaningTheCarWithAChemical, RisingCarWithWater, WashingCarProgramForm


class WashingCar:
    def __init__(self, washing_strategy):
        self.__washing_strategy = washing_strategy

    def __call__(self):
        # time.sleep(1)
        self.__washing_strategy.washing_car()
        # time.sleep(2)
        print("samochod umyty\n\n")
        # time.sleep(2)


def washing_car_menu(new_washing_car_program_list):
    while True:
        counter = 3
        print("\nOpcje mycia samochodu:\n"
              "1 - Mycie wodą\n"
              "2 - Mycie środkiem chemicznym\n"
              "3 - Woskowanie auta\n", end='')
        for i in new_washing_car_program_list:
            counter = counter + 1
            print(counter, "- Program stworzony przez użytkownika o nazwie: ", end='')
            print(f'{i.program_name}')

        print(counter + 1, "- Tworzenie nowego programu")
        print(counter + 2, "- Wycofaj")
        print(counter + 3, "- exit\n")
        print("\nWybierz: ", end='')

        counter = 3
        code = int(input())

        if code == 1:
            print('\nUwaga za moment zacznie się mycie samochodu wodą...')
            washing = WashingCar(RisingCarWithWater())
            washing()
            continue
        elif code == 2:
            print('\nUwaga za moment zacznie się mycie samochodu środkiem chemicznym...')
            washing = WashingCar(CleaningTheCarWithAChemical())
            washing()
            continue
        elif code == 3:
            print('\nUwaga za moment zacznie się woskowanie samochodu...')
            washing = WashingCar(CarWaxing())
            washing()
            continue

        elif len(new_washing_car_program_list) > 0 and 3 < code <= 3 + len(new_washing_car_program_list):
            for i in new_washing_car_program_list:
                counter = counter + 1
                if code == counter:
                    print('\nUwaga za moment zacznie się program stworzony przez użytkownika o nazwie: ', end='')
                    print(f'{i.program_name}')
                    washing = WashingCar(i)
                    washing()
                    break
        elif code == len(new_washing_car_program_list) + 4:
            print('\nStwórz nowy program')
            new_washing_program_name = input()
            new_washing_car_program_list.append(WashingCarProgramForm(new_washing_program_name))
            continue
        elif code == len(new_washing_car_program_list) + 5:
            break
        elif code == len(new_washing_car_program_list) + 6:
            sys.exit()

        else:
            print("Error - zła wartość ")
