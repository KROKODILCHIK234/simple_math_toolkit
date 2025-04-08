from setuptools import setup, find_packages

setup(
    name="simple_math_toolkit",
    version="0.1.0",
    author="KROKODILCHIK234",
    author_email="ekonstantine2610@mail.ru",
    description="A simple toolkit for basic mathematical operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KROKODILCHIK234/simple_math_toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 