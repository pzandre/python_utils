#!/usr/bin/python3
from argparse import ArgumentParser
from re import sub

"""
Validate if a given CPF number is valid.
This obviously can't tell if the CPF is already registered, or retrieve any sensible information of it.

Command line arguments: int - 11 numbers representing the CPF.

Returns - Boolean
"""

msg = "This program returns if the informed number is a valid CPF."
 
parser = ArgumentParser(description=msg)
parser.add_argument("-n", "--number", help="Input target CPF Number")

args = parser.parse_args()


def validate_cpf(number):
    # Removes non-digits values from number input
    cleaned_number = sub(r"[^0-9]", "", number)
    if len(cleaned_number) == 11:
        # Last 2 digits are validation digits, cannot enter in the initial calculation
        fixed_numbers = cleaned_number[:9]
        first_sum = 0
        for index, num in enumerate(fixed_numbers):
            first_sum += int(num) * (10 - index)
        first_remainder = first_sum % 11
        first_validator = 0
        if first_remainder > 1:
            first_validator = 11 - first_remainder
        primary_validated = f"{fixed_numbers}{first_validator}"
        second_sum = 0
        for index, num in enumerate(primary_validated):
            second_sum += int(num) * (11 - index)
        second_remainder = second_sum % 11
        second_validator = 0
        if second_remainder > 1:
            second_validator = 11 - second_remainder
        fully_validated = f"{primary_validated}{second_validator}"
        return number == fully_validated
        

if args.number:
    print(validate_cpf(args.number))
