from setuptools import setup, find_packages

setup(
    name="onemind-atak",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "nats-py>=2.6.0",
        "requests>=2.31.0",
    ],
    python_requires=">=3.10",
)
