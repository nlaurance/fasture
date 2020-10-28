from fasture import specs
import time


def some_func(one, two):
    """This takes time to compute"""
    time.sleep(25)
    return one + two


@specs.fasture_job_impl
def fasture_job(json_payload: dict) -> dict:
    """Show this as summary in openAPI
    and the rest as long description
    """
    # some validation
    res = some_func(**json_payload)
    return res
