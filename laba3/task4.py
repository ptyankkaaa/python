book = ["a", "b", "e", "Dmitriy", "Slava", "Robert", "Alblack", "Alex", "Andrew", "bag"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
prime_dict = dict(zip(alphabet, primes))  # Создаем словарь, сопоставляющий буквы с простыми числами


def letterIndex(letter):
    letter = letter.lower()
    a = 0
    for i in letter:
        a += prime_dict[letter]
    return a


def hashFunction(inputValue, lenght):
    sumIndex = 0
    for i in inputValue:
        sumIndex += letterIndex(i)
    return sumIndex % lenght


def main():
    for i in book:
        print(f'Индекс для {i} после хэширования {hashFunction(i, len(book))}')


if __name__ == "__main__":
    main()