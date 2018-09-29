class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get(self):
        print(self.name+"si sitting now")

class Cat(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)

my_dog = Cat('xiaohong',14)
my_dog.get()