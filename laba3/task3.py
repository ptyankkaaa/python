value = ["aame1", "bame2", "came333", "dame4444", "eame55555", "fame666666", "game7777777", "hame888888888", "iame999999999", "game10000000000", "kame111111111111"]

def first_symbol(key):
    return key[0]

hash3 = {}
for key in value:
    hash3[key] =  first_symbol(key)

print(hash3)
