class Customer: 
    def __init__(self,id_customer, name, age) -> None:
        self.id_customer = id_customer
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Id customer: {self.id_customer}, name: {self.name}, age: {self.age}"