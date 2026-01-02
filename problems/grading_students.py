import math

def gradingStudents(grades):
    n = len(grades)
    for i in range(n):
        g = grades[i]
        if g < 38:
            continue
        mult = math.ceil(g / 5) * 5
        if abs(g - mult) < 3:
            grades[i] = mult
    return grades 

a = [4, 73, 67, 38, 33]

print(gradingStudents(a))  # Output: [4, 75, 67, 40, 33]