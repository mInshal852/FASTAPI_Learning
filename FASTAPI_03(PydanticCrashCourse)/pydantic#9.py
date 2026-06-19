from pydantic import BaseModel, Field
from typing import Annotated, Optional

# Serialization means converting a Pydantic model into another format
# such as a Python dictionary or JSON.
# first we will see exporting in dictionary then we will see exporting in json.


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    Name: str
    age: Annotated[Optional[int], Field(default=10)]
    address: Address


ad = {"city": "Faislabad", "state": "punjab", "pin": "38000"}
add1 = Address(**ad)

p1d = {"Name": "Inshal", "address": add1}

p1 = Patient(**p1d)

print(p1)

print("--------------------------------------------- \n\n")
# now converting it into dict
temp = p1.model_dump()
print(temp)
print(type(temp))


print("--------------------------------------------- \n\n")

# now converting into json

temp = p1.model_dump_json()
print(temp)
print(
    "the only difference  btw json and dict is that python is receiving json as string, see its type: ",
    type(temp),
)


# note:
# model_dump() returns a Python dictionary.
# model_dump_json() returns a JSON string.


# now these two also provide more flexibility

# like 'include', 'exclude'

# if someone says i want to include only name:
nammme = p1.model_dump(include="Name")
print(nammme)

# now if u want to exclude name and keep every thing
exnme = p1.model_dump(exclude="Name")
print(exnme)


# now if u want to exclude state
exstate = p1.model_dump(exclude={"address": ["state"]})
print(exstate)


#  now if u don't want to include the value which is not set by user, and you don't want default value to get export then:
exdefault = p1.model_dump(exclude_unset=True)
print(exdefault)
