import random

# Define a Singleton pattern because... reasons!
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, filename):
        self.filename = filename

    def fetch_data(self):
        with open(self.filename, 'r') as file:
            data = file.readlines()
        return data

# Using the Factory Pattern to get names because why not?
class RandomizerFactory:
    @staticmethod
    def get_randomizer():
        return Randomizer()

class Randomizer:
    def __init__(self):
        self.db = DatabaseConnection("users.txt")

    def get_names(self):
        return self.db.fetch_data()

# Decorator for over-optimizing the names.
def over_optimized_shuffle(func):
    def wrapper(*args, **kwargs):
        names = func(*args, **kwargs)
        for _ in range(1000):  # Because shuffling once is just too mainstream.
            random.shuffle(names)
        return names
    return wrapper

@over_optimized_shuffle
def get_random_names():
    randomizer = RandomizerFactory.get_randomizer()
    return [name.strip() for name in randomizer.get_names()]

def main():
    print("\nRandomized Order:")
    for index, name in enumerate(get_random_names(), 1):
        print(f"{index}. {name}")

if __name__ == "__main__":
    main()
