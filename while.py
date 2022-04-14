#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This program uses a while loop


def main():
    # this function uses a while loop
    counter = 1
    sum_number = 1

    # input
    number_as_string = input("Enter a positive integer: ")
    # process & output
    print("")
    try:
        number_as_int = int(number_as_string)
        if number_as_int == 0:
            print("The sum is 1")
        elif number_as_int < 0:
            print("Not a positive integer")
        else:
            while counter <= number_as_int:
                sum_number = sum_number * counter
                counter = counter + 1
            print("The sum is {0}".format(sum_number))
    except Exception:
        print("¯\_(ツ)_/¯ sorry fam not an integer.")
    print("\nDone.")


if __name__ == "__main__":
    main()
