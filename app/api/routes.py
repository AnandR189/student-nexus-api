from fastapi import APIRouter
from app.models.schemas import Folder

# We use APIRouter to keep our routes organized
router = APIRouter()

# This is a temporary list to store our folders in memory (until we connect Firebase)
mock_database = []

@router.post("/folders/")
def create_folder(folder: Folder):
    mock_database.append(folder)
    return {"message": "Folder created successfully!", "data": folder}

@router.get("/folders/")
def get_all_folders():
    return mock_database