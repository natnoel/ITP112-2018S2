from employee import Employee
from student import Student


def is_valid_salary(salary):
    if salary > 0:
        return True
    return False


def is_valid_gpa(gpa):
    if gpa < 0:
        print('Cannot be less than 0')
        return False
    elif gpa > 4:
        print('Cannot be more than 4')
        return False
    return True


def is_valid_nric(nric):
    valid = False
    if len(nric) != 9:
        print('Length must be 9')
    elif nric[0] != 'S' and nric[0] != 'T':
        print('First character must be S or T')
    elif not nric[-1].isalpha():
        print('Last character must be a alphabetic letter')
    else:
        valid = True

    return valid


print(Employee('11', 'Eleven', 0))
print(Student('12', 'Twelve', 2))

empl_list = []
stud_list = []

option = 'Y'

while option.upper() != 'N':

    valid_nric = False
    while not valid_nric:
        nric = input('Enter NRIC: ')
        valid_nric = is_valid_nric(nric)

    name = input('Enter Name: ')

    type = 'z'
    while type.upper() != 'S' and type.upper() != 'E':
        type = input('Student or Emplouee? (S or E): ')

        if type.upper() != 'S' and type.upper() != 'E':
            print('Please enter S or E only')

    if type.upper() == 'E':
        salary = -1
        while not is_valid_salary(salary):
            salary = float(input('Enter Salary: $'))
            if not is_valid_salary(salary):
                print('Please pay him something')

        empl_list.append(Employee(nric, name, salary))

    elif type.lower() == 's':
        valid_gpa = False
        while not valid_gpa:
            gpa = float(input('Enter GPA: '))
            valid_gpa = is_valid_gpa(gpa)

        stud_list.append(Student(nric, name, gpa))

    valid_option = False
    while not valid_option:
        option = input('Do you wanna continue? (Y or N): ')
        valid_option = option.upper() == 'Y' or option.upper() == 'N'

        if not valid_option:
            print('Please enter Y or N only')

print("======== Student ==========")
for i in stud_list:
    print(i)
print("======== Employee ==========")
for j in empl_list:
    print(j)