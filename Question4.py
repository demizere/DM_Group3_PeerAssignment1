A = set()
R = []


# checking if R is a relation on A
def relationship():
    if len(R) == len(set(R)):
        print('R is a set')
        for pair in R:
            if pair[0] not in A or pair[1] not in A:
                print("R is not a subset of A X A because the following relation is in R but not in A X A: "
                      + str(pair))

                print("R is not a relation on A")
                return False

        print('R is a subset of A X A')
        print('R is a relationship on A')
        return True
    else:
        print('R is not a set')


# checking if R across A is reflexive
def is_reflexive():
    for n in A:
        if (n, n) not in R:
            return "R is not reflexive: " + str(n)

    return "R is reflexive across A"


# checking if R across A is symmetric
def is_symmetric():
    for pair in R:
        if (pair[1], pair[0]) not in R:
            return 'R is  not symmetric: ' + str(pair)

    return "R is symmetric"


# checking if R across A is transitive
def is_transitive():
    for n1 in R:
        for n2 in R:
            if n1[1] == n2[0]:
                if (n1[0], n2[1]) not in R:
                    return "R is not transitive: " + str(n1) + str(n2)

    return "R is transitive"


def main(set_input, list_input):
    global A
    A = set_input
    global R
    R = list_input
    if relationship():
        print(is_reflexive())
        print(is_symmetric())
        print(is_transitive())


# calling the main function with the set and list as arguments
main({1, 2, 3, 4}, [(2, 1), (1, 1), (3, 3), (4, 2), (2, 2), (3, 2), (2, 3), (3, 1), (4, 3)])
