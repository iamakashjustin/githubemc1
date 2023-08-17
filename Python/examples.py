class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
     

class Manager(Employee):
    def __init__(self,department):
          self.department=department

    def display(self):
        print(self.name,self.salary,self.department)

m1=Manager("CSE")
m1.display()
  


