from setuptools import setup, find_packages

setup(
    name="tracerx",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tracerx=tracerx.__main__:main"
        ]
    },
    install_requires=[
        "scapy>=2.4.5",
        "requests>=2.28.0"
    ],
    python_requires=">=3.10"
)
