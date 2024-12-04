student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = dict()
    
for student in student_scores.keys():
    
    score = student_scores[student]
    
    if score >= 91:
        grade = 'Outstanding'
    elif score >= 81 and score <= 90:
        grade = 'Exceeds Expectations'
    elif score >= 71 and score <= 80:
        grade = 'Acceptable'
    else:
        grade = 'Fail'
        
    student_grades[student] = grade
    
print(student_grades)