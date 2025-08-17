class customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Customer Name: {self.name}, Age: {self.age}"
    def __repr__(self):
        return f"Customer({self.name}, {self.age})"
    def __eq__(self, other):
        if isinstance(other, customer):
            return self.name == other.name and self.age == other.age
        return False
    def __lt__(self, other):
        if isinstance(other, customer):
            return self.age < other.age
        return False
    def __le__(self, other):
        if isinstance(other, customer):
            return self.age <= other.age
        return False
    def __gt__(self, other):
        if isinstance(other, customer):
            return self.age > other.age
        return False