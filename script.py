class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def greet(self):
        print(
            f"hello, my name is {self.name} and I'm {self.age} years old. I'm a {self.job}"
        )

    def __repr__(self):
        return f"name : {self.name}\nage : {self.age}\njob : {self.job}"
