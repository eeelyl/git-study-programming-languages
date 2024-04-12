def n_max(n, lst): return sorted(lst, reverse=True)[:n]


lst = [81, 52, 45, 10, 3, 2, 96]

print(n_max(3, lst))
