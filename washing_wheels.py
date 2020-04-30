import sys
import time

from numpy.ma.bench import timer

from abs_washing_wheels import RisingWheelsWithWater, CleaningWheelsWithAChemical, WashingWheelsProgramForm


class WashingWheels:
    def __init__(self, washing_strategy):
        self.__washing_strategy = washing_strategy

    def __call__(self):
        # time.sleep(1)
        self.__washing_strategy.washing_wheels()
        # time.sleep(2)
        print("koła umyte można jechać\n\n")
        # time.sleep(2)


def washing_wheels_menu(new_washing_wheels_program_list):
    while True:
        counter = 2
        print("\nOpcje mycia kół:\n"
              "1 - Mycie wodą\n"
              "2 - Mycie środkiem chemicznym\n", end='')
        for i in new_washing_wheels_program_list:
            counter = counter + 1
            print(counter, "- Program stworzony przez użytkownika o nazwie: ", end='')
            print(f'{i.program_name}')

        print(counter + 1, "- Tworzenie nowego programu")
        print(counter + 2, "- Wycofaj")
        print(counter + 3, "- exit\n")
        print("\nWybierz: ", end='')

        counter = 2
        code = int(input())

        if code == 1:
            print('\nUwaga za moment zacznie się mycie kół wodą...')
            washing = WashingWheels(RisingWheelsWithWater())
            washing()
            continue
        elif code == 2:
            print('\nUwaga za moment zacznie się mycie kół środkiem chemicznym...')
            washing = WashingWheels(CleaningWheelsWithAChemical())
            washing()
            continue

        elif len(new_washing_wheels_program_list) > 0 and 2 < code <= 2 + len(new_washing_wheels_program_list):
            for i in new_washing_wheels_program_list:
                counter = counter + 1
                if code == counter:
                    print('\nUwaga za moment zacznie się program stworzony przez użytkownika o nazwie: ', end='')
                    print(f'{i.program_name}')
                    washing = WashingWheels(i)
                    washing()
                    break
        elif code == len(new_washing_wheels_program_list) + 3:
            print('\nStwórz nowy program')
            new_washing_program_name = input()
            new_washing_wheels_program_list.append(WashingWheelsProgramForm(new_washing_program_name))
            continue
        elif code == len(new_washing_wheels_program_list) + 4:
            break
        elif code == len(new_washing_wheels_program_list) + 5:
            sys.exit()

        else:
            print("Error - zła wartość ")
