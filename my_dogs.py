# my_dogs.py
import dog # we need to specify exactly what we want

my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()

my_dog2 = dog.Dog("Joe", "SuperDog")
my_dog2.bark()

my_dog3 = dog.Dog("Brownie", "SuperDog")
my_dog3.bark()

my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)
print(my_dog2.name)

