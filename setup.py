#!/usr/bin/env python3
"""
Setup script for the Fake Bank Application
"""

from setuptools import setup, find_packages

setup(
    name="fake-bank",
    version="1.0.0",
    description="Professional fake bank interface for scam baiting",
    author="Bank Development Team",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "Flask>=2.0.0",
    ],
    include_package_data=True,
    package_data={
        "bank": ["templates/*", "static/*"],
    },
    entry_points={
        "console_scripts": [
            "fake-bank=bank.app:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
