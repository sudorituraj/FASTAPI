'''
steps to create APi
1.import, 2. Instance, 3.Functions, 4. Path
'''



from fastapi import FastAPI

# Create an instance of the FastAPI class

app = FastAPI()

# Define a path operation decorator for the root URL ("/")
@app.get("/")


def index():
    return {"Data":{"Name":"RITU RAJ"}}

@app.get("/about")

def about():
    return {"Data":{"About Page"}}