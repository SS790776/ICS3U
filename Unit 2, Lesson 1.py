print("Marking System")
print("----------------------------------")
grade = int(input("Please enter your grade: "))

if grade >= 80 and grade <= 100:
    print("A")
    print("Amazing! :D")
elif grade < 80 and grade >= 70:
    print("B")
    print("Great! :)")
elif grade < 70 and grade >= 60:
    print("C")
    print("OK :)")
elif grade < 60 and grade >= 50:
        print("D")
        print("Let's keep working on it!")
elif grade < 50 and grade >=0:
    print("F")
    print("See me after school")
else:
    print("not a valid grade")
