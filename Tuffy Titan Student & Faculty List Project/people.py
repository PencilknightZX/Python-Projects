
class Person:
    """ Person Class """

    def __init__(self, /, first_name, last_name):
        """ """
        self.first_name = first_name
        self.last_name = last_name

class Faculty(Person):
    """ Faculty Class """

    def __init__(self, /, first_name, last_name ,department):
        """ """
        super().__init__(first_name, last_name)
        self.department = department
        #print("Hello I am Faculty:",self.first_name, self.last_name)
        #print("My Dept is:", self.department)
        
class Student(Person):
    """ Student Class """

    def __init__(self, /, first_name, last_name):
        """ """
        super().__init__(first_name, last_name)
        #print("Hello I am student:",self.first_name, self.last_name)

    def set_class(self, /, class_year):
        """ sets the class year for student """
        self.class_year = class_year
        
    def set_major(self, /, major):
        """ sets a major for student """
        self.major = major

    def set_advisor(self, /, Faculty):
        """ sets a Faculty object as an advisor for a student object"""
        self.advisor = Faculty






