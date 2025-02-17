#!/usr/bin/env python3

class Dog:
    # Class body goes here

    def __init__(self, name="dog"):
        self.name = name

    def bark(self):
        print("Woof!")

    def sit(self):
        print(f"The {self.name} is sitting.")


#finish by calling
dog1 = Dog("Dog")
dog1.bark()

    #Instance method definition
