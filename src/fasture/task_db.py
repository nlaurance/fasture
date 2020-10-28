import uuid
import logging
from fasture.models import Task

log = logging.getLogger(__name__)

DB = {}


def get_task_by_id(uid: str):
    log.info("get task %s", uid)
    return DB.get(uid)


def store_task(task: Task):
    task.uid = uuid.uuid4().hex
    log.info("store task %s", task.uid)
    DB[task.uid] = task
    return task.uid
