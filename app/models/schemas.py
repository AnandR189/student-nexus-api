from pydantic import BaseModel
from typing import List, Optional

# This defines what a single Task looks like
class Task(BaseModel):
    title: str
    is_completed: bool = False
    
    
# This defines a Folder
class Folder(BaseModel):
    name: str
    tasks: List[Task] = []  # A folder can have a list of tasks
    subfolders: List["Folder"] = [] # A folder can have a list of OTHER folders!

# This special line helps Python understand that a Folder can contain itself
Folder.model_rebuild()