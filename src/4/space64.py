from base64 import b64decode
import re
from itertools import combinations_with_replacement

import PIL.Image


def check_candidate(candidate_pair):
    with open("../files/space64.txt", "r") as f:
        data = f.readlines()
        space64_encoded = data[0]

        [char1, char2] = candidate_pair
        base64_encoded = space64_encoded.replace("\u200c", char1).replace("\u200b", char2)
        image_string = b64decode(base64_encoded)

        with open("../files/space64.png", "wb") as f2:
            f2.write(image_string)

        try:
            PIL.Image.open("../files/space64.png", "r")
            print("halleluja XXXXXXXX")
            return True
        except:
            return False


def check_for_single_char():
    letters = "abcdefghijklmnopqrstuvwxyz+/"
    lower_and_upper = letters.lower() + letters.upper()

    # Iterate over each combination
    for (char1, char2) in combinations_with_replacement(list(lower_and_upper), 2):
        print("check for", char1, char2)
        result = check_candidate((char1, char2))

        if result:
            print("=========>", char1, char2)
            break


check_for_single_char()
