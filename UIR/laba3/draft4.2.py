book = ["Tom", "Bob", "Kevin", "Dmitriy", "Slava", "Robert", "Alblack", "Alex", "Andrew", "bag"]


def letterIndex(letter):
    letter = letter.lower()
    if ord(letter) - ord('a') != 0:
        return 2 * (ord(letter) - ord('a') + 1) - 1
    else:
        return 2


def hashFunction(inputValue, lenght):
    sumIndex = 0
    for i in inputValue:
        sumIndex += letterIndex(i)
    return sumIndex % lenght


def main():
    for i in book:
        print(f'Индекс для {i} посде хэширования {hashFunction(i, len(book))}')


if __name__ == "__main__":
    main()
