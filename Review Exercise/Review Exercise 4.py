import itertools

lst = ['A', 'B', 'C', 'D', 'E']

perms = list(itertools.permutations(lst))
combs = list(itertools.combinations(lst, 2))

print("Permutations using itertools:", perms)
print("Combinations using itertools:", combs)