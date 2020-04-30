import sys

from abs_washing_car import CarWaxing, WashingCarProgramForm
from washing_car import WashingCar, washing_car_menu
from washing_wheels import washing_wheels_menu


def main():

    new_washing_car_program_list = []
    new_washing_wheels_program_list = []
    while True:

        print("Opcje myjni samochodowej\n"
              "1 - Mycie samochodu\n"
              "2 - Mycie kół\n"
              "3 - exit\n"
              "\nWybierz: ", end='')

        code = input()

        if code == '1':
            print('\nWchodzimy w opcje mycia samochodu...')
            washing_car_menu(new_washing_car_program_list)

            continue
        if code == '2':
            print('\nWchodzimy w opcje mycia kół...')
            washing_wheels_menu(new_washing_wheels_program_list)
            continue

        elif code == '3':
            sys.exit()

        else:
            print("Error - zła wartość ")





if __name__ == "__main__":
    main()
