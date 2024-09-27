print("Marking System")
print("----------------------------------")
grade = int(input("Please enter your grade: "))
#if greater than or equal to 80, but also less than or equal to 100, print "A" and "Amazing! :D". If not, then move onto the next line.
if grade >= 80 and grade <= 100:
    print("A")
    print("Amazing! :D")
#if greater than or equal to 70, but also less than 80, print "B" and "Great! :)". If not, then move onto the next line.
elif grade < 80 and grade >= 70:
    print("B")
    print("Great! :)")
#if greater than or equal to 60, but also less than 70, print "C" and "OK :)" If not, then move onto the next line.
elif grade < 70 and grade >= 60:
    print("C")
    print("OK :)")
#if greater than or equal to 50, but also less than 60, print "C" and "Let's keep working on it!" If not, then move onto the next line.
elif grade < 60 and grade >= 50:
        print("D")
        print("Let's keep working on it!")
#if greater than or equal to 0, but also less than 50, print "F" and "See me after school" If not, then move onto the next line.
elif grade < 50 and grade >=0:
    print("F")
    print("See me after school")
#if any other number is entered, then print "not a valid grade"
else:
    print("not a valid grade")
