class User:
    def __init__(self, email, firstname, lastname):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return self.firstname + ' ' + self.lastname


# Part (a) Create teacher class, initializer and methods
class Teacher(User):
    def __init__(self, email, firstname, lastname):
        super().__init__(email, firstname, lastname)
        self.students = {}

    def get_name(self):
        return f'{super().get_name()} (Teacher)'

    def add_studemt(self, student):
        self.students[student.email] = student


# Part (b) Create Student class, initializer
class Student(User):
    def __init__(self, email, firstname, lastname):
        super().__init__(email, firstname, lastname)
        self.group = ''


# Part (c) Implement assign_students() Function
def assign_students(teacher, group, class_size):
    stud_num = 1

    while stud_num <= class_size:
        email = input(f'What is the email of student {stud_num}: ')
        first_name = input(f'What is the first name of student {stud_num}: ')
        last_name = input(f'What is the last name of student {stud_num}: ')

        stud = Student(email, first_name, last_name)
        stud.group = group

        teacher.add_studemt(stud)

        stud_num += 1

    print(f'{class_size} students assigned to {teacher.get_name()}')


# Test program
group = 'IT1901'
class_size = 3
teacher = Teacher('john@mail.com', 'John', 'Woo')
assign_students(teacher, group, class_size)
