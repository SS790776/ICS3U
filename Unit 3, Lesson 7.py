#Specifically, A pairs with T, and C pairs with G and vice versa.
def comp(S):
    #This function iterates through each element in string S. It has "new" as a variable to store the complement DNA. Once it encounters A, C, G, or T, it will add the corrosponding letter to the new variable.
    new = ''
    for x in S: #iterate through each element in S
        if x == "A":
            new = new + ("T") #if the letter is A, add T to the new string
        elif x == "C":
            new = new + ("G")#if the letter is C, add G to the new string
        elif x == "G":
            new = new + ("C")#if the letter is G, add C to the new string
        elif x == "T":
            new = new + ("A")#if the letter is T, add A to the new string
    return new
S = input("")

Complement = comp(S)

print(Complement)
