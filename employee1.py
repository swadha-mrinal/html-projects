class person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class Employee(person):
          def __init__(self,name,idnumber,salery,post):
                self.salery = salery
                self.post = post
                person.__init__(self,name,idnumber)
a = Employee('swadha',24560167,9000,"manager")
a.display()