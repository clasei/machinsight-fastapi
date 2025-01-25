from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()

# ---------------------------------
# @app.get("/") kept for debugging
@app.get("/")
def home():
    return {"message": "FastAPI Spreadsheet Import Service is Running"}

# Run the server with: uvicorn main:app --reload (install with: pip install uvicorn)
# ---------------------------------

@app.post("/import")
async def import_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    data = df.to_dict(orient="records")  # converts to JSON format
    return {"data": data}  # returns structured JSON

