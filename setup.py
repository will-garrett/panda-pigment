from setuptools import setup, find_packages

setup(
    name="panda-pigment",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "ipython",
    ],
    author="William",
    author_email="",
    description="A Python library for styling pandas DataFrames with beautiful, customizable themes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/will-garrett/panda-pigment",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 
