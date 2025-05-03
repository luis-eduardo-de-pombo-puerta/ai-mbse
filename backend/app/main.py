from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
import requests
import base64
import traceback

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Grok API settings
GROK_API_URL = "https://api.grok.ai/v1/analyze"
GROK_API_KEY = os.getenv("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY environment variable is not set")

@app.get("/healthz")
async def health_check():
    return {"status": "healthy"}

@app.post("/analyze-diagram")
async def analyze_diagram(file: UploadFile = File(...)):
    try:
        print("Received file:", file.filename)
        contents = await file.read()
        prompt = "Describe this SysML Activity Diagram, focusing on system safety aspects relevant to aerospace engineering."
        headers = {"Authorization": f"Bearer {GROK_API_KEY}"}
        files = {"image": contents}
        data = {"prompt": prompt}
        response = requests.post(GROK_API_URL, headers=headers, files=files, data=data)
        if response.status_code != 200:
            print("Grok API error:", response.text)
            raise HTTPException(status_code=500, detail=f"Grok API error: {response.text}")
        result = response.json()
        analysis = result.get("analysis") or str(result)
        return JSONResponse(content={"analysis": analysis})
    except Exception as e:
        print("Error in /analyze-diagram:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "SysML Activity Diagram Analyzer API"} 