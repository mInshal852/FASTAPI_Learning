from fastapi import FastAPI, Path, HTTPException,Query
import json

app = FastAPI()


def load_data():
    with open("patients.json",'r') as f:
        data=json.load(f)
        return data
    
@app.get('/')
def hello():
    return {'message': 'Patient Management System'}

@app.get('/about')
def about():
    return {'message': 'Doctors can now manage patients easilxy'}


@app.get('/view')
def view():
    data=load_data()
    
    return data


### ya path ka andr dots batatin ky ya path paramters is required

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description="ID of the patient in the db",example="P001")):
    patient_id = patient_id.upper()
    
    # =load all the patients
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error':'patient not found'}
    raise HTTPException(status_code=404,detail="Patient Not found")
    
    
@app.get('/sort')
def sort_patients(sort_by : str = Query(...,description='Sort on the basis of height, weight,bmi'),order: str=Query('asc',description='sort in asc or desc order')):
    
    valid_fields=['height','weight','bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=404,detail=f'Invalid field, select from {valid_fields}')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=404,detail='Invalid field, select btw asc or desc')
    
    data= load_data()
    
    sort_order= True if order == 'desc' else False
    
    sorted_data= sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)
    
    return sorted_data    
        