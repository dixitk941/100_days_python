class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
       return f"hello,my name is {self.name} and i am {self.age} year old"
person=person("karan " , 19)

print(person.greet())