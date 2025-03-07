from fastapi import FastAPI
from pydantic import BaseModel
from model import predict
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite request-uri de la orice domeniu (poți restricționa la localhost)
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PUT, DELETE etc.
    allow_headers=["*"],  # Permite toate headerele
)

class InputData(BaseModel):
    values: list[float]
    # text: str

# @app.get("/")
# def read_root():
#     return {"message": "Hello from FastAPI!"}

# @app.post("/process")
# def process_data(data: InputData):
#     return {"processed_text": data.text.upper()}


@app.post("/predict")
def make_prediction(data: InputData):
    if len(data.values) != 10:
        return {"error": "Modelul așteaptă exact 10 valori"}
    
    result = predict(data.values)
    return {"prediction changed": result}


# preia din static frontendul
app.mount("/", StaticFiles(directory="static", html=True), name="static")
