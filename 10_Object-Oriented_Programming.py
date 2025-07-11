#-------Object Oriented Programming------

#student.py

class Student:
    def __init__(self,name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)
    
   """  @property
    def name(self):
        return self._name """
    
    """ @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name """
    
   """  #Getter
    @property
    def house(self):
        return self._house """
    
   """  #Setter
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff","Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house """
        
    

    def main():
        student = Student.get()
        print(student)
    



if __name__ == "__main__":
    main()
    

#type.py

print(type(50))



#hat.py
import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff","Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls,name):
        print(name, "is in", random.choice(cls.houses))
    
        


Hat.sort("Harry")


#wizard.py


class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name
        ...
class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house
    
    ...
    
class Professor(Wizard):
    def __init__(self,name, subject):
        super().__init__(name)
        self.subject = subject
        ...
        

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus",  "Defense Against the Dark Arts")


# Vault.py

class Vault:
    def __init__(self, galleons=0,sickles=0,knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self,other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
        

potter = Vault(100,50,25)
print(potter)

weasley = Vault(25,50,100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = potter + weasley
print (total)
