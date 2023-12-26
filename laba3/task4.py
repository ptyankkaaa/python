value = ["bag", "bame2", "came333", "dame4444", "eame55555", "fame666666", "game7777777", "hame888888888", "iame999999999", "game10000000000", "kame111111111111"]


def prime_hash_index(s, size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    prime_dict = dict(zip(alphabet, primes))  # Создаем словарь, сопоставляющий буквы с простыми числами
    sum_hash = sum(prime_dict[letter.lower()] for letter in s if letter.lower() in prime_dict)  # Вычисляем сумму простых чисел для каждой буквы в строке
    return sum_hash % size  # Возвращаем остаток от деления суммы на размер хеша
