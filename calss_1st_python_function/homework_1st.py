def encryption(letter, key):
    # must be single alphabetic character
    if not letter.isalpha() or len(letter) != 1:
        return letter

    # convert to lowercase
    letter = letter.lower()

    # convert to numerical value 0-25
    # a=0, b=1, ----- z=25
    value = ord(letter) - 97

    # apply key, number of character to shift
    value = (value + key) % 26

    # return encryted letter
    return chr(value + 97)
