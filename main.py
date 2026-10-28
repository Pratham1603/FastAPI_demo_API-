from fastapi import FastAPI
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