from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["jobs"])
async def list_all_registered_jobs():
    return {"message": "jobi"}


@router.get("/{job_name}", tags=["jobs"])
async def get_specific_job(job_name: str):
    return {"message": "jobi"}
