from dataclasses import dataclass

# dictionary
person_dict = {"name": "Emily", "id": 1}


# class
class Person:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Person(name={self.name}, id={self.id})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.id == other.id


person_class = Person(id=2, name="Jacob")


# dataclass
@dataclass
class DataPerson:
    id: int
    name: str


person_dataclass = DataPerson(3, "Calvin")


@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def __post_init__(self):
        if self.price < 0:
            raise ValueError(f"Price for {self.name} cannot be negative.")
        if self.quantity < 0:
            raise ValueError("Quantity must be at least 0.")


if __name__ == "__main__":
    print(person_dict)  # string representation of a dictionary
    print(person_class)  # uses __repr__ method
    print(person_dataclass)  # auto-generated __repr__ method
    print(person_dataclass == DataPerson(3, "Calvin"))  # True
    print(person_dataclass.id)  # Accessing attribute with dot notation
    # print(person_dataclass.idont) # AttributeError because the attribute does not exist
    # This will work fine because price and quantity are valid
    bread = Product("Sourdough", 5.50, 10)
    # This will immediately raise a ValueError
    milk = Product("Milk", -2.00, 5)
