class Dog:
    def __init__(self, color, breed, size):
        self.color = color
        self.breed = breed
        self.size = size

    def __str__(self):
        return f"Dog(color='{self.color}', breed='{self.breed}', size='{self.size}')"

# Instantiate the Dog class 3 times
dog1 = Dog("brown", "labrador", "large")
dog2 = Dog("black", "golden retriever", "medium")
dog3 = Dog("white", "poodle", "small")

# Display all properties
print(dog1)
print(dog2)
print(dog3)

# Modify the properties
dog1.color = "gray"
dog2.breed = "german shepherd"
dog3.size = "extra small"

# Display all properties again
print(dog1)
print(dog2)
print(dog3)
