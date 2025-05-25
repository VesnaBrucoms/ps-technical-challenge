#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="ps-challenge",
    version="0.0.1",
    install_requires=[
        "Flask==3.1.1",
        "pydantic==2.11.4",
        "flask-openapi3==4.1.0",
        "requests==2.32.3",
    ],
    packages=find_packages(exclude=["docs", "tests"]),
    author="Artoria Stevens",
    author_email="artoriastevens@gmail.com",
)
