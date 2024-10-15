#Specifically, A pairs with T, and C pairs with G and vice versa.
def comp(S):
    new = ""
    for x in S:
        if x == "A":
            new + "T"
        elif x == "C":
            new + "G"
        elif x == "G":
            new + "C"
        elif x == "T":
            new + "A"
    return new
S = input("")

new = comp(S)
print(new)
