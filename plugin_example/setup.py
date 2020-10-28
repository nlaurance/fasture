from setuptools import setup

setup(
    name="fasture-usage",
    version="0.2",
    install_requires="fasture",
    entry_points={
        "fasture": [
            "name_for_job_in_route = plugin",
            "name_for_async_job_in_route = async_plugin",
        ]
    },
    py_modules=[
        "plugin",
        "async_plugin",
    ],
)
