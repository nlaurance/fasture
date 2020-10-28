from fasture import specs


async def another_func(one, two):
    return one + 2 * two


@specs.fasture_job_impl
async def fasture_job(json_payload: dict) -> dict:
    """This wrapped should really document"""
    res = await another_func(**json_payload)
    return {"result": res}
