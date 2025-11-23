from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="Bookie Audiobook API")

class TextToSpeechRequest(BaseModel):
    text: str
    voice_id: str = "default_voice_id"

@app.get("/")
async def root():
    return {"message": "Bookie Audiobook API is running"}

@app.post("/generate-audio")
async def generate_audio(request: TextToSpeechRequest):
    """
    Stub for ElevenLabs integration.
    In a real implementation, this would call the ElevenLabs API.
    """
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        # For now, we just log a warning if no key is present, 
        # but in production we might want to enforce it.
        print("Warning: ELEVENLABS_API_KEY not set.")
    
    # Mock response
    return {
        "status": "success",
        "message": f"Generating audio for text: {request.text[:20]}...",
        "voice_id": request.voice_id
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
