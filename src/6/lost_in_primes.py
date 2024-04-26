import requests
from enum import Enum
import re
import os


class Type(Enum):
    ProbablyPrime = 1
    Unknown = 2


def get_list_url(prime_type, perpage=100, mindig=27000, start=0):
    return f"http://factordb.com/listtype.php?t={prime_type}&mindig={mindig}&perpage={perpage}&start={start}&download=1"


def find_id_url(input_string):
    pattern = r'index.php\?id=[0-9]+'
    matches = re.findall(pattern, input_string)
    return f"http://factordb.com/{matches[0]}"


def get_id_url(number):
    response = requests.get(f"http://factordb.com/index.php?query={number}")
    text = response.text
    return find_id_url(text)


def find_candidates(prime_type, start, end, perpage=100, mindig=27000):
    pattern = re.compile('^[01]+$')
    original_start = start
    candidates = []
    while start <= end:
        output = requests.get(get_list_url(start=start, perpage=perpage, prime_type=prime_type, mindig=mindig))
        options = output.text.split('\n')
        for number in options:
            matched = re.match(pattern, number)
            if matched:
                cd = get_id_url(number)
                candidates.append(get_id_url(number))
                print("=========> possible candidate", cd)

                if re.match("000000", number) and re.match("1111111", number):
                    print("=======================> SERIOUS CANDIDATE FOUND", cd)

        start += perpage
        print(f"Progress {(start - original_start) / (end - original_start)}", len(options))
    return candidates


for dig in [27000, 30490, 50160]:
    group1 = find_candidates(prime_type=Type.ProbablyPrime.value, start=0, end=50000, perpage=500, mindig=dig)
    print("==================== done with", dig)

# for dig in [27000, 27020, 27040, 27060, 27080, 27100, 27122, 27146, 27175, 27205]:
#     group1 = find_candidates(prime_type=Type.Unknown.value, start=0, end=50000, perpage=500, mindig=dig)
#     print("==================== done with", dig)

