import requests # <-- to send HTTP requests
from fastapi import FastAPI, UploadFile, File
import pandas as pd
import os # <-- built-in Python module to access environment variables

app = FastAPI()

NODE_SERVER_URL = os.getenv("NODE_SERVER_URL", "http://127.0.0.1:5005/upload-data") 

# ---------------------------------
# @app.get("/") kept for debugging
@app.get("/")
def home():
    return {"message": "FastAPI Spreadsheet Import Service is Running"}

# Run the server with: uvicorn main:app --reload (install with: pip install uvicorn)
# ---------------------------------

# ---------------------------------
@app.post("/import")
async def import_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    # replace NaN values to avoid JSON issues
    df.fillna(0, inplace=True)

    # convert to JSON
    data = df.to_dict(orient="records")

    # send data to Node.js server
    try:
        response = requests.post(NODE_SERVER_URL, json=data)
        response.raise_for_status()
        return {"message": "Data sent to Express successfully!", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": "Failed to send data to server", "details": str(e)}
