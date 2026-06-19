from pydantic import BaseModel, EmailStr, HttpUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated


# step1: developing baseModel
class Patient(BaseModel):
    # In some cases, some fields can be required and some can be optiona

    # Type validation
    name: str
    email: EmailStr
    linkedIn: HttpUrl
    age: int
    weight: float  # kg
    height: float  # in meters
    married: bool

    allergies: Optional[List[str]] = None
    contact_det: Dict[str, str]


def insert_into_data3(patient: Patient):
    print("name: ", patient.name)
    print("age: ", patient.age)
    print("weight: ", patient.weight)
    print("married: ", patient.married)
    print("email: ", patient.email)
    # print("allergies:", ", ".join(patient.allergies))
    print("bmi is: ", patient.calculate_bmi)

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
    "height": 1.72,
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
