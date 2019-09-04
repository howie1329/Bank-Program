Student = {}

class Students():
    grade_level = 12
    gradeAvg = 78

    def __init__(self, name):
        self.name = name

    def view(self):
        print(self.grade_level)
        print(self.gradeAvg)
        print(self.name)

    def change(self):
        self.grade_level = 10
        print(self.grade_level)

f = open("demo.txt", "x")
f.write("This was fun")
f.close()

Thomas = Students('Thomas')
Thomas.view()
Thomas.change()
Thomas.view()
# print(Students('Thomas').view())
Student['01'] = Students('Howard')
Student['01'].view()
# print(Student['01'].view())