from pydantic import BaseModel

# nested models
# first see the issue below, then i will also show the solution


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    Name: str
    age: int
    address: Address


ad = {"city": "Faislabad", "state": "punjab", "pin": "38000"}
add1 = Address(**ad)

p1d = {"Name": "Inshal", "age": 32, "address": add1}

p1 = Patient(**p1d)

print(p1)

# advantages:
# better organization of related data(e.g , vitals, address, insurance).
# Resuability: use vitals in multiple models(e.g Patient, MedicalBoard).
# Readability: Easier for developers and API consumers to understand.
# Validation: Nested models are validated automatically-no extra work needed.
