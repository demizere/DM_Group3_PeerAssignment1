list_1 = list(map(str, input("Enter elements that will be contained in your first list: ").split()))
list_2 = list(map(str, input("Enter elements that will be contained in your second list: ").split()))
print("List_1:", list_1, "List_2:", list_2)


# Checks the truth value of B ⊆ A
def check_truth_value():
    for item in list_2:
        if item in list_1:
            check = True
        else:
            check = False
            break
    return check


print(check_truth_value())


# A list representing the set A - B
def Check_difference():
    item_not = []
    for i in range(len(list_1)):
        for item in list_1:
            if item not in list_2:
                item_not.append(item)
        return item_not


print(Check_difference())


# A list representing the set A * B
def cartesian_product():
    res = []
    for item in list_1:
        for element in list_2:
            res.append([item, element])
    return res


print(cartesian_product())
