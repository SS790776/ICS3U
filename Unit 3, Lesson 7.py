#Specifically, A pairs with T, and C pairs with G and vice versa.
def comp(S):
    new = ''
    for x in S:
        if x == "A":
            new = new + ("T")
        elif x == "C":
            new = new + ("G")
        elif x == "G":
            new = new + ("C")
        elif x == "T":
            new = new + ("A")
    return new
S = input("")

Complement = comp(S)

print(Complement)
