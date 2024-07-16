employee1_name = "Fatih Serdar"
employee1_age = 25
employee1_address = "123 Main Street, Chicago, IL"

# ortak özelliklere sahip nesnlerin birlikte yazıldığı yer
class Employee(object):
    """
    attribute : özellikler (yaş,isim,adres vb...)
    behaviour : davranışlar (nesneye özgü yaptığı işler, yazılımcının kod yazması gibi)
    """
    pass

employee1 = Employee()

#%% Attribute
class Footballer:
    football_club = "Barcelona"
    age = 30

f1 = Footballer()
print(f1.age, f1.football_club)
f1.football_club = "Real Madrid"
print(f1.age, f1.football_club)

#%% Methods
class Square(object):
    edge = 5 # meter
    area = 0
    def area1(self): # self ile classa ait variableler kullanılır
        self.area = self.edge*self.edge
        print( f"Area: ", self.area)
s1 = Square()
print(s1)
print(s1.edge)
print(s1.area1())

s1.edge = 7
s1.area1()

#%% Methods vs Functions
# Methodlar class içinde fonksiyonlar class dışında kullanılır.
class Emp(object):
    age = 25
    salary = 1000
    def ageSalaryRatio(self): # method
        print(self.age / self.salary)
def ageSalaryRatios(age, salary): # fonskiyon
    print(age / salary)
e1 = Emp()
e1.ageSalaryRatio()
ageSalaryRatios(32,3200)

#%% initializer or contructor

class Animal(object):
    def __init__(self, age, name):
        self.name = name
        self.age = age
    def getAge(self):
        return self.age
    def getName(self):
        print( self.name)
a1 = Animal(5,"cat")
a2 = Animal(5,"dog")
a3 = Animal(3,"bird")


