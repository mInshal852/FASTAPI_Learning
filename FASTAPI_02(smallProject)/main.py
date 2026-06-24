from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Optional, Literal
import json
from fastapi.responses import JSONResponse

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
    @computed_field()
    @property
    def bmi(self) -> float:
        bmi = round((self.weight / (self.height) ** 2), 2)
        return bmi

    @computed_field()
    @property
    def verdict(self) -> str:
        verdict = ""
        if self.bmi < 18.5:
            verdict = "Underweight"
        elif self.bmi >= 18.5 and self.bmi <= 24.9:
            verdict = "Normalweight"
        elif self.bmi >= 25.0 and self.bmi <= 29.9:
            verdict = "Overweight"
        else:
            verdict = "Obese"
        return verdict


# now we will design our endpoint, which will be using data from the request body with the help of this pydantic model


@app.post(  # try it in from fastAPI docs
    "/create"
)  # all the data coming from the request body will be directly given to our pydantic model for further validation.
def create_patient(patient: Patient):

    # load existing data
    data = load_data()
    print(data)
    # check if the patiend_id already exists

    patient.id = patient.id.upper()

    if patient.id in data:
        raise HTTPException(400, detail="patient already exists")
    # new patient added to json file

    # now the 'patient' is a Patient object we have to convert it into python dictionary
    print(patient)
    data[patient.id] = patient.model_dump(exclude="id")

    # save into the json file
    save_data(data)

    # now to tell patient the work has been done, what you will do is send a json response
    return JSONResponse(
        status_code=201, content={"message": "Patient created successfully."}
    )


def save_data(data):
    # Open the file "patients.json" in write ("w") mode.
    # If the file already exists, its old contents will be overwritten.
    # If the file does not exist, Python will create it.
    with open("patients.json", "w") as f:

        # Convert the Python object stored in 'data'
        # (e.g., a dictionary or list) into JSON format
        # and write it into the file represented by 'f'.
        json.dump(data, f)

    # When the 'with' block ends, the file is automatically closed.
