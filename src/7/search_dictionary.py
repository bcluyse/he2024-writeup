def find_occurrences(string, char):
    indices = []
    for i in range(len(string)):
        if string[i] == char:
            indices.append(i)
    return indices


def find_matches(pattern: list[str]):
    for letter in pattern:
        matches = find_occurrences(pattern, letter)
        if len(matches) > 1:
            print(letter, matches)


def all_letters_match(candidate, *positions):
    first_occ = candidate[positions[0]]
    for position in positions:
        if candidate[position] != first_occ:
            return False

    return True


def check_20_30_35(candidate):
    # abdzfgbzgfjkz
    if len(candidate) != 13:
        return

    if all_letters_match(candidate, 1, 6) and all_letters_match(candidate, 4, 9):
        if all_letters_match(candidate, 5, 8) and all_letters_match(candidate, 3, 7, 12):
            print(candidate)


def check_9_28(candidate):
    # pqryprqtupzpsxypxy

    if len(candidate) == 18 and all_letters_match(candidate, 0, 4, 9, 11, 15):
        print(candidate)


def check_11_16(candidate):
    # tupzpsxypxyqpzpvewzsxy
    if len(candidate) == 22 and all_letters_match(candidate, 2, 4, 8, 12, 14):
        print(candidate)


def check_12_15(candidate):
    # rtupzpsxypxyqpzpvewzsxy
    if len(candidate) == 23 and all_letters_match(candidate, 3, 5, 9, 13, 15):
        print(candidate)


def check_22_35(candidate):
    # xyqprsypsrtupzp

    if len(candidate) == 15 and all_letters_match(candidate, 3, 7, 12, 14) and all_letters_match(candidate, 4,
                                                                                                 9) and all_letters_match(
        candidate, 5,
        8):
        print(candidate)


def check_17(candidate):
    # wvavupqvpqrvavxeyaupq

    if len(candidate) == 21 and all_letters_match(candidate, 1, 3, 7, 11, 13) and all_letters_match(candidate, 2, 12,
                                                                                                    17):
        print(candidate)


def check_18(candidate):
    # vavupqvpqrvavxeyaupq

    if len(candidate) == 20 and all_letters_match(candidate, 0, 2, 6, 10, 12) and all_letters_match(candidate, 1, 11,
                                                                                                    16):
        print(candidate)


def check_32(candidate):
    # pqrvstqvtswxvavupqvpqrvav

    if len(candidate) == 25 and all_letters_match(candidate, 3, 7, 12, 14, 18, 22, 24) and all_letters_match(candidate,
                                                                                                             0, 16, 19):
        print(candidate)


def check_34(candidate):
    # pqrvstqvtswxvavupqvpqrvavye

    if len(candidate) == 27 and all_letters_match(candidate, 3, 7, 12, 14, 18, 22, 24) and all_letters_match(candidate,
                                                                                                             0, 16, 19):
        print(candidate)


def has_unique_letters(*letters):
    set_letters = set(letters)
    if len(set_letters) == len(letters):
        return True


def find_workable_sentence(cds: list[str]):
    cd1s = set()
    for cd in cds:
        # pqr_stq_tsvw_a_upq_pqr_a_xeyaupq
        # xeyaupq
        if len(cd) != 7 or cd[1] != 'e':
            continue

        x = cd[0]
        y = cd[2]
        a = cd[3]
        u = cd[4]
        p = cd[5]
        q = cd[6]

        if not has_unique_letters(x, y, u, p, q, a, 'e', 'h'):
            continue

        for cd2 in cds:
            # pqr

            if len(cd2) != 3 or cd2[0] != p or cd2[1] != q:
                continue

            r = cd2[2]
            if not has_unique_letters(x, y, u, p, q, a, r, 'e', 'h'):
                continue

            for cd3 in cds:
                # upq
                if len(cd3) != 3 or cd3[0] != u or cd3[1] != p or cd3[2] != q:
                    continue

                cd1s.add(cd)
                print(cd, cd2, cd3)

    print(cd1s)


with open("../files/short_dict.txt", "r") as file:
    candidates = file.read().splitlines()
    # for candidate in candidates:
    #     check_20_30_35(candidate)
    #     check_9_28(candidate)
    #     check_11_16(candidate)
    #     check_12_15(candidate)
    #     check_22_35(candidate)
    #     check_17(candidate)
    #     check_18(candidate)
    #     check_32(candidate)
    #     check_34(candidate)
    # find_workable_sentence(candidates)

# find_matches('pqrmstqmtswxm')
