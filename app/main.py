from fastapi import FastAPI
from app.routers.rtr_response import response_router
app = FastAPI()

app.include_router(response_router)

@app.get('/')
def root():
    return {
        "hello": "world",
        "About": "This is a simple LLM gen AI project using Mistral from hugging face",
        "Author": "auxghlann",
    }

