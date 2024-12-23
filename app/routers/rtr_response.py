from app.core.mistral import Mistral
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Create Router
response_router = APIRouter(prefix="/chat")

# Create BaseModel
class Prompt(BaseModel):
    input: str


@response_router.post("/response")
def generate_response(prompt: Prompt) -> dict:
    try:
        client: Mistral = Mistral()
        output:str = client.generate_response(prompt.input)

        if output:
            return {
                "status_code": 200,
                "response": output
            }

        else:
            raise HTTPException(status_code=400, detail="Bad Request")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    


