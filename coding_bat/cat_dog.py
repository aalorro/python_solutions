####################################
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
####################################

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    count1 = 0
    count2 = 0
    for i in range(len(str)):
        if str[i:i + 3] == "cat":
            count1 += 1

    for n in range(len(str)):
        if str[n:n + 3] == "dog":
            count2 += 1

    if count1 == count2:
        return True
    else:
        return False
