from setuptools import setup, find_packages

setup(
    name="blog",
    version="0.0.1",
    description="Hi this is my blog package",
    py_modules=["blog"],
    packages=find_packages(),
    extra_require={
        "dev": [
            "pytest>=7.2.1",
            "black>=23.1.0",
            "bandit>=1.7.4",
            "flake8>=6.0.0",
            "isort>=5.12.0",
            
        ]
    }
)