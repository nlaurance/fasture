"""Setup for fasture."""

from distutils.core import setup
from setuptools import find_packages


setup(
    name="fasture",
    description="Rest API in front of local tasks",
    version="0.1",
    author="Nicolas Laurance",
    author_email="nicolas.laurance at gmail.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["fastapi", "pluggy"],
    extras_require={
        "dev": ["black"],
        "test": ["pytest"],
    },
)
