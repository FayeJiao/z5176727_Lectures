
# Tuples
# The objects a tuple refers to are fixed when the tuple is created.
# There is no way to add or remove elements
# ---there is no tuple method equivalent of list's append and pop methods.

# Create a tuple with two elements
tup = (1, 2)

# unpack the tuple into two variables:
(a, b) = tup

# print
print(f"`a` is {a} and `b` is {b}")
# The following lines would be treated equivalently by Python:
a, b, c = 1, True, "word"
a, b, c = (1, True, "word")
(a, b, c) = 1, True, "word"
(a, b, c) = (1, True, "word")