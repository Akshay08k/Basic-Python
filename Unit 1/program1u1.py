# x = 10
# y = 5
# print("Before Swapping x = ", x, "y = ", y)

# x = x + y

# y = x - y

# x = x - y

# print("After Swapping x = ", x, "y = ", y)


class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

# Using duck typing to call the speak method on different objects
def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
duck = Duck()

print(animal_speak(dog))  # Output: Woof!
print(animal_speak(cat))  # Output: Meow!
print(animal_speak(duck))  # Output: Quack!
