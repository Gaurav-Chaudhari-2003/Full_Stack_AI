# 1)Student Grade Checker
#  Topics: If-Else, Elif, Comparison Operators, Logical Operators, String
#  Problem:
#  Ask the user to enter marks (0–100).
#  If marks
# ≥
#  90 →
#  Print “A Grade”
#  70–89 →
#  Print “B Grade”
#  50–69 →
#  Print “C Grade”
#  Else →
#  Print “Fail”

marks = int(input("Enter the marks: "))

if marks >= 90:
    print("A Grade")
elif 70 <= marks < 90:
    print("B Grade")
elif 50 <= marks < 70:
    print("C Grade")
else:
    print("Fail")