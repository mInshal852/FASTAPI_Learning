from pydantic import BaseModel, EmailStr, HttpUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

# now for data validation like custom data validation like age btw 0,60, so pydantic gives us Field function , can work on numerical data types as well as on string, it can also be used to add metadata.


# step1: developing baseModel
class Patient(BaseModel):
    # In some cases, some fields can be required and some can be optiona

    # Type validation
    name: str
    email: EmailStr
    linkedIn: HttpUrl
    age: int
    # weight: float = Field(gt=0)
    weight: float
    married: bool

    allergies: Optional[List[str]] = None
    contact_det: Dict[str, str]

    # data validation can also be done here

    @field_validator("name")
    @classmethod
    def transform_name(cls, name):
        return name.upper()

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domain = ["hdfc.com", "icici.com"]
        # abc@gmail.com
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domain:
            raise ValueError("Not a valid domain")

        return value

    @field_validator(
        "age", mode="before"
    )  # before means run this field validator before type validation, "after"
    # does it's opposite
    @classmethod
    def age_valid(cls, val):
        if 0 < val < 100:
            return val
        else:
            raise ValueError("put age value btw 0 and 100")


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
    "age": 60,
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust1", "dust2", "dust3", "dust4", "dust5"],
    "contact_det": {"ali": "123455678", "ahmad": "987654321"},
}

patient1 = Patient(**Patient_info)
insert_into_data3(patient1)


# now you can see, change just in Patient class, the data type, the changes will reflect to all the functions using it.
