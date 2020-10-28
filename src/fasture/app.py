import functools
import inspect
import logging
from concurrent.futures import ProcessPoolExecutor

from fastapi import FastAPI

from fasture import models
from fasture import task_db
from fasture.plugin_mgr import get_plugin_manager
from fasture.routers import jobs, tasks

log = logging.getLogger(__name__)

executor = ProcessPoolExecutor(max_workers=2)

app = FastAPI()


@app.get("/", description="why not", include_in_schema=False)
async def root():
    return {"message": "Hello World"}


app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
# app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])



{"one": 11, "two": 22}


def make_future(long_running, job_name):
    log.info("registering %s", job_name)

    @functools.wraps(long_running)
    async def wrapped(params: dict) -> dict:
        log.info("Queuing %s", job_name)
        future = executor.submit(long_running, params)
        task = models.Task(
            job_name=job_name,
            future=future,
        )
        uid = task_db.store_task(task)
        future.add_done_callback(task.future_callback)
        return {"task_uid": uid}

    return wrapped


def register_dynamic_routes():
    pm = get_plugin_manager()
    for plugin in pm.get_plugins():
        log.info(pm.get_name(plugin))

        job_name = pm.get_name(plugin)
        doc = plugin.fasture_job.__doc__
        summary = description = ""
        if doc:
            summary, *description = doc.split("\n")
            description = inspect.cleandoc("\n".join(description))

        app.add_api_route(
            f"/launch/{job_name}",
            # plugin.fasture_job,
            make_future(plugin.fasture_job, job_name),
            summary=summary,
            description=description,
            methods=["POST"],
            tags=["jobs"],
        )


register_dynamic_routes()


@app.on_event("shutdown")
def shutdown_event():
    log.info("Shutting down executor")
    app.extra["executor"].shutdown(wait=True)
