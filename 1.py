class myclass:
    def init(self,name,age):
        self.name__=name
        self.age__=age
    def get_name(self):
        return self.name__
    def get_age(self):
        return self.age__    

class Animal:
    def init(self,name):
        self.name__=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("woof!!!")
def make_sound(animal):
    animal.speak()
dog=Dog()
make_sound(dog)
    