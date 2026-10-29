from fastapi import FastAPI, Path, HTTPException, Query
import json

with open('patient.json', 'r') as f:
    data = json.load(f)

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., title="Patient ID", example="P001", description="The unique identifier for a patient")):
    # load all patient data 

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., title="Sort By", description="Sort patient records by specific fields", example="height"), order: str = Query('asc', title="Order", description="ascending or descending", example="asc")):

    valid_fields = ['height', 'weight', 'bmi']
    # handle wrong inputs rather than valid_fields
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field choose from {valid_fields}")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f"Invalid order value. Choose from 'asc' or 'desc'")

    # sort the data based on the specified field and order
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=(order == 'desc'))
    return sorted_data              