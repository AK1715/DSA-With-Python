class Employee:
    # empId = 1
    # name = 'Akshay'
    # salary = 50000

    # @classmethod
    # def f1(cls):
    #     print('ID:-' , cls.empId, 'Name:-' , cls.name, 'salary:-', cls.salary)

    def __init__(self, empid=None, name=None, salary=None):
        self.empid = empid
        self.name = name
        self.salary= salary

    def setEmpid(self,empid):
        self.empid=empid

    def setName(self,name):
        self.name=name

    def setSalary(self,salary):
        self.salary=salary

    def getEmpid(self):
        return self.empid
    
    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary


e1=Employee()
e2=Employee(1,'akshay',100)
e1.setEmpid(2)
e1.setName('akshay')
e1.setSalary(20)
print(e1.getEmpid(),e1.getName(),e1.getSalary())
print(e2.getEmpid(),e2.getName(),e2.getSalary())

# t1 = Employee(15,'kajal',40000)
# print(t1.empId,t1.name,t1.salary)
# Employee.f1()