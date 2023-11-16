class Furniture:
    def __init__(self):
        self._typeOfWooed = "Teakwood"

class Chair(Furniture):
    def __init__(self):
        super().__init__()
        self.__numberOfLegs = 4

    def setWoodType(self, typeOfWood):
        self._typeOfWooed = typeOfWood

    def displayChairSpecification(self):
        print("This chair is made of {} and has {} legs.".format(self._typeOfWooed, self.__numberOfLegs))

chair = Chair()
print("Would you like to change the type of wood from Teakwood? Y/N")
userChoice = input()

if userChoice is 'Y':
    print("Enter the type of wood you would like your chair to be made of")
    typeOfWood = input()
    chair.setWoodType(typeOfWood)
chair.displayChairSpecification()