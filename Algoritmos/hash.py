# Algoritmo para converir un numero en valor "hash"
# Juan Pablo
# Maria Jose
# Andrea
# Daniel Ruiz

def AddToHash(key):
    key = str(key).replace("","-").split("-")
    i = 0
    while len(key) > i:
        if key[i] == "":
            key.pop(i)
        else:
            i += 1
    
    lock = ""
    for i in range(len(key)):
        aux = int(key[i])*47
        if aux > 100:
            lock = lock + str(aux)
        elif aux == 0:
            lock = lock + "000"
        else:
            lock = lock + "0" + str(aux)
    
    lock = int(lock)*14
    return lock
k = [1132,
2011,
1111,
2000,
2014,
1101,
2009,
1100,
1105,
1133
]
hash = []
for i in range(len(k)):
    hash.append(AddToHash(k[i]))

print("Lista de llaves Hash: ")
for i in range(len(hash)):
    print("k" + str(i+1) + ":",hash[i])