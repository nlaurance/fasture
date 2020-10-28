from typing import Any

from pydantic import BaseModel
from datetime import datetime


class Task(BaseModel):
    uid: str = None
    job_name: str = None
    created_at: datetime = datetime.utcnow()
    completed_at: datetime = None
    state: str = "PENDING"
    result: Any = None
