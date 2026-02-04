"""Setup configuration for MNEMIS."""

from setuptools import setup, find_packages

setup(
    name="mnemis",
    version="0.1.0",
    description="MNEMIS - Cross-Project Memory System for GAIA Ecosystem",
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
