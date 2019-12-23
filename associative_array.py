#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: Dec 2019
# This program uses an associative array


def unicode_conversion(single_letter):
    # This function splits words into letters
    # -into numbers and puts them in a list.
    unicode_hex = {}
    unicode_hex['A'] = "41"
    unicode_hex['B'] = "42"
    unicode_hex['C'] = "43"
    unicode_hex['D'] = "44"
    unicode_hex['E'] = "45"
    unicode_hex['F'] = "46"
    unicode_hex['G'] = "47"
    unicode_hex['H'] = "48"
    unicode_hex['I'] = "49"
    unicode_hex['J'] = "4a"
    unicode_hex['K'] = "4b"
    unicode_hex['L'] = "4c"
    unicode_hex['M'] = "4d"
    unicode_hex['N'] = "4e"
    unicode_hex['O'] = "4f"
    unicode_hex['P'] = "50"
    unicode_hex['Q'] = "51"
    unicode_hex['R'] = "52"
    unicode_hex['S'] = "53"
    unicode_hex['T'] = "54"
    unicode_hex['U'] = "55"
    unicode_hex['V'] = "56"
    unicode_hex['W'] = "57"
    unicode_hex['X'] = "58"
    unicode_hex['Y'] = "59"
    unicode_hex['Z'] = "5a"
    unicode_hex['a'] = "61"
    unicode_hex['b'] = "62"
    unicode_hex['c'] = "63"
    unicode_hex['d'] = "64"
    unicode_hex['e'] = "65"
    unicode_hex['f'] = "66"
    unicode_hex['g'] = "67"
    unicode_hex['h'] = "68"
    unicode_hex['i'] = "69"
    unicode_hex['j'] = "6a"
    unicode_hex['k'] = "6b"
    unicode_hex['l'] = "6c"
    unicode_hex['m'] = "6d"
    unicode_hex['n'] = "6e"
    unicode_hex['o'] = "6f"
    unicode_hex['p'] = "70"
    unicode_hex['q'] = "71"
    unicode_hex['r'] = "72"
    unicode_hex['s'] = "73"
    unicode_hex['t'] = "74"
    unicode_hex['u'] = "75"
    unicode_hex['v'] = "76"
    unicode_hex['w'] = "77"
    unicode_hex['x'] = "78"
    unicode_hex['y'] = "79"
    unicode_hex['z'] = "7a"
    unicode_hex[' '] = "20"

    if single_letter in unicode_hex.keys():
        return unicode_hex[single_letter]
    else:
        return -1


def main():
    # this function uses an associative array
    words = input("Please enter a word or phrase: ")
    for single_letter in words:
        answer = unicode_conversion(single_letter)
        print(single_letter, answer)


if __name__ == "__main__":
    main()
