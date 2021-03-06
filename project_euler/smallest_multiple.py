#######################################
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder. What is the smallest positive number that
# is evenly divisible by all of the numbers from 1 to 20?
######################################


def isDivisible(num):
    for i in range(2,21):
        if num % i != 0:
            return False
    return True

num = 20
while True:
    if isDivisible(num):
        break
    num += 20

print(num)
