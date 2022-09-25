def gradingStudents(grades):
    new_grades = []
    
    for grade in grades:
        mutlipleGrade = (grade - (grade % 5) +5)
        if grade < 40:
            if 40 - grade < 3:
                new_grades.append(40)
            else:
                new_grades.append(grade)
        else:
            if mutlipleGrade - grade < 3:
                new_grades.append(mutlipleGrade)
            else:
                new_grades.append(grade)
    return new_grades


grades = [73,67,38,33]
print(gradingStudents(grades))