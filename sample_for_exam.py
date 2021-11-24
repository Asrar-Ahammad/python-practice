student_name=input('Enter student Name:')
marks={
    'Asrar':95,
    'John':94,
    'Harry':96

}
for student in marks:
    if student==student_name:
        print(student,':',marks[student])
        break
else:
    print('No entry found')
