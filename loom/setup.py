"""Setup configuration for LOOM."""

from setuptools import setup, find_packages

setup(
    name="loom",
    version="0.1.0",
    description="LOOM - Visual Agent Editor Foundation for GAIA Ecosystem",
    author="GAIA Ecosystem",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ]
    },
)
