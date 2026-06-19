from pydantic import BaseModel, EmailStr, HttpUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

# now what field_validator was doing, it was applying on single field, but what if fields depend on each other for example
# person with age greater than 0 must have special phone number, now here comes the model_validator to perform this kind of
# operations.


# step1: developing baseModel
class Patient(BaseModel):
    # In some cases, some fields can be required and some can be optiona

    # Type validation
    name: str
    email: EmailStr
    linkedIn: HttpUrl
    age: int
    weight: float
    married: bool

    allergies: Optional[List[str]] = None
    contact_det: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and "emergency" not in self.contact_det:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return self


def insert_into_data3(patient: Patient):
    print("name: ", patient.name)
    print("age: ", patient.age)
    print("weight: ", patient.weight)
    print("married: ", patient.married)
    print("email: ", patient.email)
    # print("allergies:", ", ".join(patient.allergies))

    print("allergies:", patient.allergies)
    print("contact_det: ", patient.contact_det)
    print("Inserted into DataBase")


# step2: now make pydantic object
Patient_info = {
    "name": "inshal",
    "email": "inshal@hdfc.com",
    # "email": "inshal@gmail.com",
    "linkedIn": "http://linkedicom/12",
    "age": 61,
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust1", "dust2", "dust3", "dust4", "dust5"],
    "contact_det": {
        "ali": "123455678",
        "ahmad": "987654321",
        "emergency": "123456788765",
    },
}

patient1 = Patient(**Patient_info)
insert_into_data3(patient1)


# now you can see, change just in Patient class, the data type, the changes will reflect to all the functions using it.
