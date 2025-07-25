from dotenv import load_dotenv
from fastapi import FastAPI, Request
from mangum import Mangum
from app.main import app

handler = Mangum(app)

load_dotenv()

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Webhook received:", data)
    return {"status": "ok"}

handler = Mangum(app)
