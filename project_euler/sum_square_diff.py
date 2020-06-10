####################################
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.
####################################

# Get the squares of 1-100 and sum them up
sum1 = 0
sum2 = 0
for i in range(1,101,1):
    sum1 = sum1 + i ** 2

# Get the sum of 1-100
for j in range(1,101,1):
    sum2 = sum2 + j

# Get the difference
diff = (sum2 ** 2) - sum1

print(diff)
