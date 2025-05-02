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

# Hugging Face API settings
HF_API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip2-opt-2.7b"
HF_TOKEN = os.getenv("HF_API_TOKEN")
if not HF_TOKEN:
    raise ValueError("HF_API_TOKEN environment variable is not set")

@app.get("/healthz")
async def health_check():
    return {"status": "healthy"}

@app.post("/analyze-diagram")
async def analyze_diagram(file: UploadFile = File(...)):
    try:
        print("Received file:", file.filename)
        contents = await file.read()
        prompt = "Describe this SysML Activity Diagram, focusing on system safety aspects relevant to aerospace engineering."
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        files = {"image": contents}
        data = {"inputs": prompt}
        response = requests.post(HF_API_URL, headers=headers, files=files, data=data)
        if response.status_code != 200:
            print("Hugging Face API error:", response.text)
            raise HTTPException(status_code=500, detail=f"Hugging Face API error: {response.text}")
        result = response.json()
        # BLIP-2 returns a dict with 'generated_text' key
        analysis = result.get("generated_text") or str(result)
        return JSONResponse(content={"analysis": analysis})
    except Exception as e:
        print("Error in /analyze-diagram:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "SysML Activity Diagram Analyzer API"} 