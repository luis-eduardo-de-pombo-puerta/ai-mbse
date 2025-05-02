from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
import openai
import base64
from typing import Optional
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

# Initialize OpenAI client (new API)
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/healthz")
async def health_check():
    return {"status": "healthy"}

@app.post("/analyze-diagram")
async def analyze_diagram(file: UploadFile = File(...)):
    try:
        print("Received file:", file.filename)
        contents = await file.read()
        
        # Convert image to base64
        base64_image = base64.b64encode(contents).decode('utf-8')
        
        # Prepare the prompt
        prompt = "Describe this SysML Activity Diagram, focusing on system safety aspects relevant to aerospace engineering."
        
        # Call OpenAI API (new API)
        response = openai_client.chat.completions.create(
            model="gpt-4-vision",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1000
        )
        
        # Extract the analysis from the response
        analysis = response.choices[0].message.content
        
        return JSONResponse(content={"analysis": analysis})
    
    except Exception as e:
        print("Error in /analyze-diagram:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "SysML Activity Diagram Analyzer API"} 