# ∀x ∈ X, ∃y ∈ Y such that y | x.
import random


def mainset(set1, set2):
    print(f"X= {set1}")
    print(f"y= {set2}")

    y = random.choice(set2)
    for a in range(len(set1)):
        if set1[a] % y == 0:
            print(f"{set1[a]}/{y} True")

        else:
            print(f"{set1[a]}/{y} False")


mainset([-3, 1, 0, -2, 3, 7, 10, 20], [-23, 2, -3, -10, 1, 3, 5])