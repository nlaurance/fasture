import pluggy

fasture_job_impl = pluggy.HookimplMarker("fasture")
"""Marker to be imported and used in plugins (and for own implementations)"""

fasture_job_spec = pluggy.HookspecMarker("fasture")


@fasture_job_spec()
def fasture_job(json_payload: dict) -> dict:
    """Wrapper around a local function to make it a fasture job"""
