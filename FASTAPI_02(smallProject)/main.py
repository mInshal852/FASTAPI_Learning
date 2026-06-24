from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Optional, Literal
import json

app = FastAPI()


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
        return data


@app.get("/")
def hello():
    return {"message": "Patient Management System"}


@app.get("/about")
def about():
    return {"message": "Doctors can now manage patients easilxy"}


@app.get("/view")
def view():
    data = load_data()

    return data


### ya path ka andr dots batatin ky ya path paramters is required


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ..., description="ID of the patient in the db", example="P001"
    )
):
    patient_id = patient_id.upper()

    # =load all the patients
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error':'patient not found'}
    raise HTTPException(status_code=404, detail="Patient Not found")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight,bmi"),
    order: str = Query("asc", description="sort in asc or desc order"),
):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=404, detail=f"Invalid field, select from {valid_fields}"
        )
    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=404, detail="Invalid field, select btw asc or desc"
        )

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order
    )

    return sorted_data


# before seeing this creating patient process go through projectinfo


# 3 step total
# 1. client sent data to the server
# 2. validate data -> using pydantic model
# 3. if validated correctly insert into the json file of the patient


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Enter id of patient", example="P001")]
    name: Annotated[
        Optional[str],
        Field(..., description="Please enter the patient name", example="Inshal"),
    ]
    city: Annotated[str, Field(..., description="Enter city name", example="Lahore")]
    age: Annotated[int, Field(..., strict=True, gt=0, lt=120)]
    gender: Annotated[
        Literal["male", "female"], Field(..., description="choose the gender")
    ]
    height: float = Field(
        ..., description="Enter values greater then zero", strict=True, gt=0
    )
    weight: float = Field(
        ..., description="Enter values greater then zero", strict=True, gt=0
    )
    # now verdict and bmi will not be given by user it will be computed by us
    computed_field()

    @property
    def bmi(self) -> float:
        return round((self.weight / (self.height) ** 2), 2)

    computed_field()

    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi >= 18.5 and self.bmi <= 24.9:
            return "Normalweight"
        elif self.bmi >= 25.0 and self.bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"
