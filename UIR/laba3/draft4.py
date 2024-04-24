# value = ["aame1", "bame2", "came333", "dame4444", "eame55555", "fame666666", "game7777777", "hame888888888", "iame999999999", "game10000000000", "kame111111111111"]

value = ["bag"]


def prime_hash_index(s, size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    prime_dict = dict(zip(alphabet, primes))  # Создаем словарь, сопоставляющий буквы с простыми числами
    sum_hash = sum(prime_dict[letter.lower()] for letter in s if letter.lower() in prime_dict)  # Вычисляем сумму простых чисел для каждой буквы в строке
    return sum_hash % size  # Возвращаем остаток от деления суммы на размер хеша

# def hash4(inp_value, len):
#     sum_index = 0
#     for i in inp_value:
#         sum_index += hash4_letter_index(i)
#     return sum_index % len


# def hash4_letter_index(letter):
#     letter = letter.lower()
#     if ord(letter) - ord('a') != 0:
#         return 2 * (ord(letter) - ord('a') + 1) - 1
#     else:
#         return 2


def print_h4():
    for i in value:
        print(f'Индекс для {i} после хэширования {prime_hash_index(i, len(value))}')
    print("\n")

print_h4()
