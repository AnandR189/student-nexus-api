from fastapi import FastAPI
from app.api.routes import router as folder_router

app = FastAPI(title="Student Nexus API")

# This "includes" the routes we just wrote
app.include_router(folder_router)

@app.get("/")
def root():
    return {"message": "Welcome Anand! Your routes are now connected."}