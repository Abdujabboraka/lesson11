class String:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)


    def __set__(self, instance, value):
        if isinstance(value, str):
            instance.__dict__[self.name] = value
        else:
            raise ValueError

class Integer:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__[self.name] = value
        else:
            raise TypeError


class Mylist:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if isinstance(value, list):
            instance.__dict__[self.name] = value
        else:
            raise TypeError
class Mybool:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if isinstance(value, bool):
            instance.__dict__[self.name] = value
        else:
            raise TypeError



class Myfloat:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if isinstance(value, float):
            instance.__dict__[self.name] = value
        else:
            raise TypeError


class User:
    username = String()
    first_name = String()
    last_name = String()
    age = Integer()
    groups = Mylist()
    status = Mybool()
    rating = Myfloat()

    def __init__(self,username: str , first_name: str , last_name: str, age : int, groups: list , status: bool, rating : float):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.groups = groups
        self.status = status
        self.rating = rating


    def get_info(self):
        return f"USER:\n    username: {self.username}\n    first name: {self.first_name}\n    last name: {self.last_name}\n    age: {self.age} years old!\n    groups: {self.groups}\n    status: {self.status}\n    rating: {self.rating}"




Abdujabbor = User(username="@academic_24",first_name="Abdujabbor",last_name="Tursunov",age=20,groups=["fn 24"],status=True,rating=100.5)

print(Abdujabbor.get_info())


