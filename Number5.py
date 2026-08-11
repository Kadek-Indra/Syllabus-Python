import itertools

alphabet = "abc"
all_possibilities = (itertools.permutations(alphabet))
result = ["".join(item) for item in all_possibilities]

print(result)