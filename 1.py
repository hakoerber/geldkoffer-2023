# s = so, w = wie
l = "swssssswswwwssssswwsssswswwssswwswwswsssswwsswsw"

# we have 48 "bits"
# those are 6 x 8 bits that each decode via ASCII to a char

# convert s/w to bits
l = [0 if c == "s" else 1 for c in l]

# chunk into 8 bit chunks
l = [l[i:i + 8] for i in range(0,len(l),8)]

# convert the 8 bits chunks into integers
l = [int("".join([str(b) for b in c]), 2) for c in l]

# convert from int to char via ascii
l = [chr(c) for c in l]

# concat and print the result
result = "".join(l)
print(result)
