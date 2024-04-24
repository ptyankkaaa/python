value = ["aame1", "bame2", "came333", "dame4444", "eame55555", "fame666666", "game7777777", "hame888888888", "iame999999999", "game10000000000", "kame111111111111"]

def lenght_string(name):
    return len(name)

hash2 = {}
for name in value:
    hash2[name] = lenght_string(name)

print(hash2)
