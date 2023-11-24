from abc import ABC

class Animal(ABC):
    def __init__(self, nama):
        self.nama = nama
        
    def make_sound(self):
        pass
    
    def get_nama(self):
        return self.nama
    
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class Duck(Animal):
    def make_sound(self):
        return "Quack!"
    
class Zoo:
    def __init__(self):
        self.animals = []
               
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.get_nama()} added to the zoo")
        else:
            print("Invalid animal type")
            
    def make_all_sounds(self):
        for animal in self.animals:
            print(f"{animal.get_nama()} says {animal.make_sound()}")

dog = Dog("Buddy")
cat = Cat("Whiskers")
duck = Duck("Donald")

zoo = Zoo()
zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.add_animal(duck)

zoo.make_all_sounds()
