#FAQ
# В процессе выполнения дз окнчательно запутался в заданиях 1-3, но задание 4 вроде вбирает всё то,
# что нужно было сделать в заданиях 1-3, можете сразу к нему переходить (Обозначено как "TASK 4")



# 1 TASK
# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
# class Lecturer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#
# class Reviewer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
# 2 TASK
# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     def add_courses(self, course_name):
#         self.finished_courses.append(course_name)
#
#     def rate_lecturer(self, lecturer, course, grade):
#         if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
#             if course in lecturer.grades:
#                 lecturer.grades[course].append(grade)
#             else:
#                 lecturer.grades[course] = [grade]
#         else:
#             return 'Ошибка'
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
# class Reviewer(Mentor):
#     def __init__(self, name, surname):
#         super().init(name, surname)
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#
# class Lecturer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)

#TASk 3
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
# class Reviewer(Mentor):
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#     def __str__(self):
#         return f'Имя: {self.name}\nФамилия: {self.surname}'
#
#
# class Lecturer(Mentor):
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.grades = []
#
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
#     def __str__(self):
#         average_grade = sum(self.grades) / len(self.grades)
#         return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}'
#     def __lt__(self, other):
#         return self.average_grade() < other.average_grade()
#
#     def __gt__(self, other):
#         return self.average_grade() > other.average_grade()
# class Student:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.grades = []
#         self.courses_in_progress = []
#         self.completed_courses = []
#
#     def rate_lecturer(self, lecturer, course, grade):
#         if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
#             if course in lecturer.grades:
#                     lecturer.grades[course].append(grade)
#             else:
#                     lecturer.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#     def __str__(self):
#         average_grade = sum(self.grades) / len(self.grades)
#         courses_in_progress = ', '.join(self.courses_in_progress)
#         completed_courses = ', '.join(self.completed_courses)
#         return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {completed_courses}\n'
#
#
#     def __lt__(self, other):
#         return self.average_grade() < other.average_grade()
#
#     def __gt__(self, other):
#         return self.average_grade() > other.average_grade()
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
# some_reviewer = Reviewer('Some', 'Buddy')
# print(some_reviewer)
#
# some_lecturer = Lecturer('Some', 'Buddy')
# some_lecturer.grades = [9.8, 9.9, 10.0]
# print(some_lecturer)
#
# some_student = Student('Ruoy', 'Eman')
# some_student.grades = [9.9, 9.8, 9.9]
# some_student.courses_in_progress = ['Python', 'Git']
# some_student.completed_courses = ['Введение в программирование']
# print(some_student)
# some_lecturer1 = Lecturer('Some', 'Buddy')
# some_lecturer1.grades = [9.8, 9.9, 10.0]
#
# some_lecturer2 = Lecturer('Another', 'Lecturer')
# some_lecturer2.grades = [8.8, 9.5, 8.0]
#
# if some_lecturer1 > some_lecturer2:
#     print(f'{some_lecturer1} ,имеет более высокую среднюю оценку за лекции')
# else:
#     print(f'{some_lecturer2} ,имеет более высокую среднюю оценку за лекции')
#
#
# some_student1 = Student('Ruoy', 'Eman')
# some_student1.grades = [9.9, 9.8, 9.9]
# some_student1.courses_in_progress = ['Python']
# some_student1.completed_courses = ['Введение в программирование', 'Основы языка программирования Python', 'ООП и API']
# some_student2 = Student('Someone', 'Else')
# some_student2.grades = [8.5, 9.0, 8.7]
# some_student2.courses_in_progress = ['Python']
# some_student2.completed_courses = ['Введение в программирование', 'Основы языка программирования Python', 'ООП и API']
#
# if some_student1 > some_student2:
#     print(f'{some_student1} Имеет более высокую среднюю оценку за домашние задания')
# else:
#     print(f'{some_student2} Имеет более высокую среднюю оценку за домашние задания')

# TASK 4
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress and str(grade).isnumeric() and 0 < int(grade) < 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rating(self):
        grades_lst = sum(self.grades.values(), [])
        if grades_lst:
            return sum(grades_lst) / len(grades_lst)
        else:
            return 'Оценок нет'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self._average_rating() < other._average_rating()

    def __str__(self) -> str:
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {round(self._average_rating(), 1)}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rating(self):
        grades_lst = sum(self.grades.values(), [])
        if grades_lst:
            return sum(grades_lst) / len(grades_lst)
        else:
            return 'Оценок нет'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self._average_rating() < other._average_rating()

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self._average_rating(), 1)}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress
                and str(grade).isnumeric() and 0 < int(grade) < 11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_rating_student_course(students: list[Student], course):
    sum_rating = 0
    number_of_ratings = 0
    for student in students:
        if course in student.grades:
            sum_rating += sum(student.grades[course])
            number_of_ratings += len(student.grades[course])
    if number_of_ratings:
        print(f'Средняя оценка по курсу {course} у студентов: {round(sum_rating / number_of_ratings, 1)}.')
    else:
        print(f'Оценок по курсу {course} нет')


def average_rating_lecturer_course(lecturers: list[Lecturer], course):
    sum_rating = 0
    number_of_ratings = 0
    for lecture in lecturers:
        sum_rating += sum(lecture.grades.get(course))
        number_of_ratings += len(lecture.grades.get(course))
    if number_of_ratings:
        print(f'Средняя оценка по курсу {course} у лекторов: {round(sum_rating / number_of_ratings, 1)}.')
    else:
        print(f'Оценок по курсу {course} нет')


student_1 = Student('Лупа', 'Пупин')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Безопасность информации']
student_1.finished_courses += ['Java']

student_2 = Student('Пупа', 'Лупин')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Безопасность информации']

reviewer_1 = Reviewer('Биба', 'Бобов')
reviewer_1.courses_attached += ['Безопасность информации']
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Боба', 'Бибов')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

lecturer_1 = Lecturer('Сан', 'Санов')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Безопасность информации']

lecturer_2 = Lecturer('Иван', 'Иванченко')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Безопасность информации', 9)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'Java', 10)

student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Безопасность информации', 9)
student_1.rate_hw(lecturer_1, 'Python', 8)

student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Безопасность информации', 8)
student_2.rate_hw(lecturer_2, 'Python', 9)

print(student_1)

print(reviewer_1)

print(lecturer_1)

print(student_1 > student_2)

print(lecturer_1 > lecturer_2)

average_rating_student_course([student_1, student_2], 'Python')

average_rating_lecturer_course([lecturer_1, lecturer_2], 'Python')