value = ["aame1", "bame2", "came333", "dame4444", "eame55555", "fame666666", "game7777777", "hame888888888", "iame999999999", "game10000000000", "kame111111111111"]

def hash4(inp_value, len):
    sum_index = 0
    for i in inp_value:
        sum_index += hash4_letter_index(i)
    return sum_index % len


def hash4_letter_index(letter):
    letter = letter.lower()
    if ord(letter) - ord('a') != 0:
        return 2 * (ord(letter) - ord('a') + 1) - 1
    else:
        return 2


def print_h4():
    for i in value:
        print(f'Индекс для {i} после хэширования {hash4(i, len(value))}')
    print("\n")

print_h4()
