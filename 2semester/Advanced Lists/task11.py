from collections import Counter


def find_duplicates(input_list):
    counts = Counter(input_list)
    duplicates = [num for num, count in counts.items() if count > 1]
    return duplicates


input_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
output_list = find_duplicates(input_list)
print("Output:", output_list)
