import itertools

# Define the list
lst = ['A', 'B', 'C', 'D', 'E']

# Function to compute and print all combinations
def compute_combinations(lst):
    print("Combinations:")
    for r in range(1, len(lst) + 1):
        combinations = itertools.combinations(lst, r)
        for combo in combinations:
            print(combo)
    print()

# Function to compute and print all permutations
def compute_permutations(lst):
    print("Permutations:")
    for r in range(1, len(lst) + 1):
        permutations = itertools.permutations(lst, r)
        for perm in permutations:
            print(perm)
    print()

# Compute and print all combinations and permutations
compute_combinations(lst)
compute_permutations(lst)
