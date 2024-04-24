value = ["aame1", "bame2", "came333", "dame4444", "eame55555", "fame666666", "game7777777", "hame888888888", "iame999999999", "game10000000000", "kame111111111111"]


def always_one(name):
    return 1

hash1 = {}
for i in value:
    hash1[i] = always_one(i)

print(hash1)


