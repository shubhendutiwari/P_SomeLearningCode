"""Write a function (def is_valid_pin(pin_code)) which should return whether or not a string represents
 a valid Indian pin  code. Consider a valid pin code is any string consisting of exactly 6 digits."""


pin: str = input("Please enter PIN code")


def is_valid_pin(pin_code):
    return len(pin_code) == 6 and all(p in '0123456789' for p in pin)


if is_valid_pin(pin):
    print(pin + " is a valid PIN")

else:
    print(pin + " is an invalid PIN")
