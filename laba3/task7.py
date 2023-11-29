book = ["Maus","Fun Home","Watchmen","Barbaris"]

author = ["Lapina Podatko", "Poline Dmitro", "Polianna Dmitro", "Lapina Podatko"]

# book_author = dict(zip(book, author))

# title = input()
# print(list(book_author[title]))

hash = {}
for i in range (len(book)):
    hash[book[i]] = author[i]

print(hash[input()])

# class Node(Generic[K, V]):
#     key: K
#     value: V 
#     next_ptr: Optional['Node[K, V]'] = None

# class HashTable(Generic[K,V]):

#     def __init__(self, capacity: int) -> None:
#         self._size: int = 0
#         self._capacity: int = capacity
#         self._table: ctypes.Array[Optional[Node[K, V]]] = (capacity * ctypes.py_object)()

#         for i in range(0, capacity):
#             self._table[i] = None

#     def _hash(self, key: K) -> int:
#         h = hash(key)
#         return (self._capacity - 1) & (h ^ (h >> 16))
    
#     def _resolve_put_collision(self, key: K, value: V, index: int) -> None:
#         self._table[index] = Node(
#             key=key, value=value, next_ptr=self._table[index])
#         print(f"Collision: (index: {index}, key: {key}, value: {value})")


# incert(12,200) вставляет в хэш 200 с ключём 12
# hash(12) = 12%(количество бакетов) добавляет ключ 12 в ячейку с индексом остатка от деления на 10
# search(12) ищет в хэше объект под ключём 12 тобишь 200

# hash.incert(12,200) вставляет хэш 200 с ключём 12 в ячейку хэш таблицы с индексом 12%(количество бакетов)
# hash.erase(9) удаляет все данные из ячейки с индексом 9%(количество бакетов) с ключём 9

# load_factor = size(кол-во всех эл-ов)/bucket_size(кол-во бакетов)    если около 0.7 значит надо перезаписать хэш таблицу,
# выделив большее количество бакетов
# hash.find(9) ищет в хэш таблице элемент с ключём 9 в ячейке с индексом 9%(количество бакетов)

