from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def healthcheck():
    return {"message": "Shopify MVP webhook listener is online."}

@app.post("/webhook")
async def handle_webhook(request: Request):
    payload = await request.json()
    print("Received payload:", payload)
    return {"status": "ok"}
