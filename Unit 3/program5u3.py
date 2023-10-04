class student:
    marks = 75

    @classmethod
    def display_marks(cls,name):
        print("{} scored {} marks".format(name,cls.marks))


student.display_marks("Ram")
student.display_marks("Shayam")