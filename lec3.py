
# 3.4 Comprehensions

# List Comprehension:
# Method 1:
# Create a list with all even integers from 0 to 1 million
evens = []
for x in range(1_000_000 + 1):
    if x % 2 == 0:
        evens.append(x)

print(evens[:10])
# Method 2:
# Create a list with all even integers from 0 to 1 million
evens = [x for x in range(1_000_000 + 1) if x % 2 == 0]
print(evens[:10])