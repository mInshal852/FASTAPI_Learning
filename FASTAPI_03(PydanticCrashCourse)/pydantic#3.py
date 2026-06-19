from pydantic import BaseModel


# step1: developing baseModel
class Patient(BaseModel):
    # now define schema
    # type validation
    name: str
    age: int

    # data validation can also be done here


def insert_into_data3(patient: Patient):
    print("name: ", patient.name)
    print("age: ", patient.age)
    print("Inserted into DataBase")


# step2: now make pydantic object
Patient_info = {"name": "inshal", "age": 22}

patient1 = Patient(**Patient_info)
insert_into_data3(patient1)


# now you can see, change just in Patient class, the data type, the changes will reflect to all the functions using it.
