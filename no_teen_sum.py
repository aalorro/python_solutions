########################
# Given 3 int values, a b c, return their sum.
# However, if any of the values is a teen -- in the range 13..19 inclusive -- then that
# value counts as 0, except 15 and 16 do not count as a teens.
########################

#no_teen_sum(1, 2, 3) → 6
#no_teen_sum(2, 13, 1) → 3
#no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    if a == 15 or a == 16 or a < 13:
        a = a
    else:
        a = 0

    if b == 15 or b == 16 or b < 13:
        b = b
    else:
        b = 0

    if c == 15 or c == 16 or c < 13:
        c = c
    else:
        c = 0

    return a + b + c