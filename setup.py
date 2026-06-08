from setuptools import setup, find_packages

setup(
    name="calculator-package",
    version="1.0.0",
    author="Your Name",
    description="A simple calculator for CI/CD learning",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
