class Course:
    def __init__(self, code, name, intake):
        self.__code = code
        self.__name = name
        self.__intake = intake

    def set_code(self, code):
        if len(code) == 6:
            self.__code = code
            return True
        else:
            return False

    def __str__(self):
        return f'The student intake for {self.__name} ({self.__code}) is {self.__intake}'


c = Course('ITDF08', 'Diploma in Financial Informatics', '70')
print(c)
