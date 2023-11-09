from pprint import pprint
l = "swssssswswwwssssswwsssswswwssswwswwswsssswwsswsw"

count_so = sum([1 if c == "s" else 0 for c in l])
print(count_so)

count_wie = sum([1 if c == "w" else 0 for c in l])
print(count_wie)

l = [0 if c == "s" else 1 for c in l]

chunks = 3
digits_per_chunk = 2

size = int(len(l) / chunks)

l = [l[i:i + size] for i in range(0,len(l),size)]

pprint(l)
l = [[c[i:i + 8] for i in range(0,len(c),8)] for c in l]

pprint(l)

l = [["".join([str(b) for b in d]) for d in c] for c in l]

l = [[int(b, 2) for b in c] for c in l]

l = ["".join([chr(b) for b in c]) for c in l]

pprint(l)

