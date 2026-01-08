from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Chatbot Backend API")

# Define the structure of the incoming request
class UserQuery(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_endpoint(query: UserQuery):
    """
    Receives a prompt and returns a generated response.
    Replace the logic inside with your LLM (OpenAI, Gemini, etc.)
    """
    user_text = query.prompt
    
    # Mock AI Logic: In a real app, you'd call your model here
    bot_response = f"Backend received: '{user_text}'. I am your FastAPI assistant!"
    
    return {"response": bot_response}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    