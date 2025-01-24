from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI Spreadsheet Import Service is Running"}

# Run the server with: uvicorn main:app --reload (install with: pip install uvicorn)
