#!/usr/bin/env python3

class Person:
    # Class body goes here
    def __init__(self, name = "Person"):
        self.name = name

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

#call 
p1 = Person("Guido")
p1.talk()
p1.walk()



    #Instance method definition
 
