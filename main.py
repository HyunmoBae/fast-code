from fastapi import FastAPI
from starlette.responses import PlainTextResponse

app = FastAPI()

@app.get("/health")
async def health_check():
    return PlainTextResponse("건강합니다", status_code=200)
