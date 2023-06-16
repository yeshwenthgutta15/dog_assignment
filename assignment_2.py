class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
# haveing the function description ‘description()'
    def description(self):
        print("Name:", self.name)
        print("Age:", self.age)
# haveing the function ‘get_info()’ 
    def get_info(self):
        print("Coat Color:", self.coat_color)
# Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. 
# It should have at least two methods of its own.
class tommysthedog(Dog):

    def play_fetch(self):
        print("tommy the dog is playing fetch!")
    def Snore(self):
        print("tommy the dog is snoring!")

class goldenretriver(Dog):

    def Barking(self):
        print("goldenretriver is Barking!")
    def sleeping(self):
        print("goldenretriver is sleeping!")

# Create objects and implement the above functionalities.
dog1 = Dog("hero", 3, "yellow")
dog1.description()
dog1.get_info()
print()

dog2 = tommysthedog("sammy", 5, "Brown")
dog2.description()
dog2.get_info()
dog2.play_fetch()
dog2.Snore()
print()

dog3 = goldenretriver("lucy", 2, "pink")
dog3.description()
dog3.get_info()
dog3.Barking()
dog3.sleeping()
