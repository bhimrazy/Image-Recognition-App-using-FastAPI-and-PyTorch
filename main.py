from typing import Optional
from fastapi import FastAPI,File,UploadFile,Request
import utils

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(file:UploadFile = File(...)):
    return utils.get_result(image_file=file)
    
