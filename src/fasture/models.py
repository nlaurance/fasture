from dataclasses import dataclass
from datetime import datetime
from concurrent.futures import Future
from typing import Any


@dataclass
class Task:
    job_name: str
    created_at: datetime = datetime.utcnow()
    uid: str = None
    completed_at: datetime = None
    result: Any = None
    future: Future = None

    @property
    def state(self):
        with self.future._condition:
            return self.future._state

    def future_callback(self, future):
        print("Done")
        self.completed_at = datetime.utcnow()
        self.result = future.result()
