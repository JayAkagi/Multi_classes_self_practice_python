from lib.animal import Animal
from lib.zoo import Zoo

lion = Animal("Lion", "ROAR")
tiger = Animal("Tiger", "RAWR")
fox = Animal("Fox", "Hyiyahiyahihiwaa")
flamingo = Animal("Flamingo", "pwonk")
eagle = Animal("Eagle", "WaaaaeiiK")

city_zoo = Zoo()

city_zoo.add_animal(lion)
city_zoo.add_animal(fox)
city_zoo.add_animal(eagle)

city_zoo.all_sound()
