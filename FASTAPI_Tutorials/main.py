from fastapi import FastAPI

app= FastAPI() #made fastapi object

# for endpoint u have to define route
@app.get("/") 
def hello():
    return {'message' : 'Helloworld'}


@app.get("/about")

def about():
    return {'message': ' campusx is an education platform where u can learn AI.'}