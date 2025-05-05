#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: May 5, 2025
# Program that asks the user for a temperature value in degrees Celsius.
# It then displays the equivalent value in degrees Fahrenheit


# DEFINE fahrenheit()
def fahrenheit():
    # Get the user's input as a string
    # \u00b0 is the unicode sequence for the degree symbol
    user_input = input("Enter the temperature (\u00b0C): ")

    try:
        # Convert the user's input to a float
        degrees_celsius = float(user_input)

        # CONVERT FROM CELSIUS TO FAHRENHEIT
        degrees_fahrenheit = (9 / 5) * degrees_celsius + 32

        # Display the result
        # \u00b0 is the unicode sequence for the degree symbol
        # Values are rounded to 2 decimal places
        print(f"{degrees_celsius:.2f}\u00b0C is equal to ", end="")
        print(f"{degrees_fahrenheit:.2f}\u00b0F")

    except ValueError:
        # Tell the user that their input wasn't a number
        print(f"{user_input} is not a number.")


def main():
    # CALL fahrenheit()
    fahrenheit()
    # Program completion message
    print("Thanks for Playing!")


if __name__ == "__main__":
    main()
