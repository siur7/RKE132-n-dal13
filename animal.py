class Animal:
    def __init__(self, pet_name):
        self.name = pet_name
        self.ears = 2
        self.legs = 4
    
    def sees(self, other):
        print(f"{self.name} sees {other.name}.")

class Cat(Animal):
    def __init__(self, cat_name):
        super().__init__(cat_name)
        self.hunger = 0

    def meow(self):
        print(f"{self.name}: Meow!")
    def hiss(self):
        print(f"{self.name}: Hiss!")
    def purr(self):
        print(f"{self.name} is purring.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

        self.hunger = self.hunger + 1
        if self.hunger >= 10:
            print(f"{self.name} is hungry!")
            self.meow()
    def cat_sees(self, other):
        super().sees(other)

        if isinstance(other, Dog):
            self.hiss()
        elif isinstance(other, Cat):
            self.purr()

class Dog(Animal):
    def __init__(self, dog_name):
        super().__init__(dog_name)
        self.hunger = 0

    def bark(self):
        print(f"{self.name}: Woof!")

    def wag_tail(self):
        print(f"{self.name} is wagging its tail.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

        self.hunger = self.hunger + 1
        if self.hunger >= 10:
            print(f"{self.name} is hungry!")
            self.bark()

    def dog_sees(self, other):
        super().sees(other)

        if isinstance(other, Cat):
            self.bark()
        elif isinstance(other, Dog):
            self.wag_tail()