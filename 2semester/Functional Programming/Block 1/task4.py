from functools import reduce

input_string = "6 -1 3 -5 -15 4 1 9 8 6 -3 -4 12 -10 7"

numbers = list(map(int, input_string.split()))

positive_numbers = list(filter(lambda x: x > 0, numbers))

negative_numbers = list(filter(lambda x: x < 0, numbers))

sorted_positive_numbers = sorted(positive_numbers)

sorted_negative_numbers = sorted(negative_numbers)

sorted_numbers = sorted_positive_numbers + sorted_negative_numbers

output_string = ' '.join(map(str, sorted_numbers))

print(output_string)
